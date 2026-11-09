"""
Copy-Trader (Paper Trading, kein echtes Geld)

Beobachtet die Solana-Wallets der besten Fomo-Trader (Liste in data/copy/wallets.json) und
macht ihre Memecoin-Käufe simuliert nach:
  - Kauft ein Trader einen neuen Coin -> wir "kaufen" für 10 Fr. zum Kurs, den wir dann sehen.
  - Verkauft er einen Teil -> wir verkaufen denselben Anteil unserer Position.
  - Pro Kauf und Verkauf 4 % Kosten (wie beim Scanner).

Wie es funktioniert: Jede Minute werden die Token-Bestände jeder Wallet über die öffentliche
Solana-Schnittstelle (RPC) abgefragt und mit der letzten Minute verglichen. Mehr Coins = Kauf,
weniger Coins = Verkauf. Käufe und Verkäufe innerhalb derselben Minute sehen wir nicht
(die könnte man echt auch nicht kopieren).

Optional: Secret SOLANA_RPC (z. B. kostenloser Helius-Schlüssel) statt der öffentlichen RPC.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------- Einstellungen
EINSATZ_CHF = 10.0
GEBUEHR_PCT = 4.0
CHECK_INTERVALL_S = 60
CHECKPOINT_MIN = 15

# Was als echter Kauf zählt (sonst sind es Spam-Airdrops oder Kleinstbeträge)
MIN_KAUF_USD = 20.0          # der Trader muss für mindestens 20 $ gekauft haben
MIN_LIQ_USD = 5_000          # Coin muss handelbar sein
REST_SCHWELLE = 0.02         # verkauft er bis auf unter 2 % seines Höchstbestands -> alles raus

# "Tot" wie beim Scanner
TOT_LIQ_USD = 1_000
TOT_WERT_ANTEIL = 0.05
TOT_FEHLT_STUNDEN = 24
PLAUSI_SPRUNG_X = 20.0
PLAUSI_MAX_MCAP_USD = 1_000_000_000

# Diese Mints sind "Geld", keine Memecoins
BASIS_MINTS = {
    "So11111111111111111111111111111111111111112",   # wSOL
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
    "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",  # USDT
}
TOKEN_PROGRAMME = [
    "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",   # SPL Token
    "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb",   # Token-2022
]

BASIS = Path(__file__).parent / "data" / "copy"
WALLETS_FILE = BASIS / "wallets.json"
STATE_FILE = BASIS / "state.json"
AUSWERTUNG_FILE = BASIS / "auswertung.md"
RPC = os.getenv("SOLANA_RPC") or "https://api.mainnet-beta.solana.com"
DEX = "https://api.dexscreener.com"
HEADERS = {"User-Agent": "paper-copy-trader/1.0"}


# ---------------------------------------------------------------- Hilfsfunktionen
def jetzt():
    return datetime.now(timezone.utc)


def fr(x):
    return f"{x:,.2f} Fr.".replace(",", "'")


def rpc(methode, params, tries=4):
    for i in range(tries):
        try:
            r = requests.post(RPC, json={"jsonrpc": "2.0", "id": 1, "method": methode, "params": params},
                              headers=HEADERS, timeout=25)
            if r.status_code == 429:
                time.sleep(3 * (i + 1))
                continue
            r.raise_for_status()
            j = r.json()
            if "error" in j:
                print(f"  ! RPC-Fehler {methode}: {j['error']}")
                time.sleep(2 * (i + 1))
                continue
            return j["result"]
        except (requests.RequestException, ValueError) as e:
            print(f"  ! RPC {methode}: {e}")
            time.sleep(2 * (i + 1))
    return None


def get_json(url, tries=3):
    for i in range(tries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            if r.status_code == 429:
                time.sleep(5 * (i + 1))
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            print(f"  ! Fehler bei {url}: {e}")
            time.sleep(2 * (i + 1))
    return None


def lade_wallets():
    if not WALLETS_FILE.exists():
        return []
    daten = json.loads(WALLETS_FILE.read_text(encoding="utf-8"))
    return [w for w in daten.get("trader", []) if w.get("wallet") and w.get("aktiv", True)]


def lade_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"bestand": {}, "positionen": []}


def speichere_state(state):
    BASIS.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------- Daten holen
def bestand(wallet):
    """{mint: Menge} aller Tokens dieser Wallet, oder None bei Fehler."""
    ergebnis = {}
    for prog in TOKEN_PROGRAMME:
        r = rpc("getTokenAccountsByOwner", [wallet, {"programId": prog}, {"encoding": "jsonParsed"}])
        if r is None:
            return None
        for konto in r.get("value", []):
            info = konto["account"]["data"]["parsed"]["info"]
            mint = info["mint"]
            menge = float(info["tokenAmount"].get("uiAmountString") or 0)
            if mint not in BASIS_MINTS and menge > 0:
                ergebnis[mint] = ergebnis.get(mint, 0.0) + menge
        time.sleep(0.15)
    return ergebnis


def hole_paare(mints):
    """Liquidestes Paar pro Mint (DexScreener, 30 pro Anfrage)."""
    beste = {}
    mints = list(mints)
    for i in range(0, len(mints), 30):
        teil = ",".join(mints[i:i + 30])
        for p in get_json(f"{DEX}/tokens/v1/solana/{teil}") or []:
            mint = (p.get("baseToken") or {}).get("address")
            if mint not in mints:
                continue
            liq = (p.get("liquidity") or {}).get("usd") or 0
            if mint not in beste or liq > ((beste[mint].get("liquidity") or {}).get("usd") or 0):
                beste[mint] = p
        time.sleep(0.3)
    return beste


def preis_von(p):
    try:
        preis = float(p.get("priceUsd") or 0)
    except ValueError:
        return None, 0
    mcap = p.get("marketCap") or p.get("fdv") or 0
    if preis <= 0 or mcap > PLAUSI_MAX_MCAP_USD:
        return None, 0
    return preis, (p.get("liquidity") or {}).get("usd") or 0


# ---------------------------------------------------------------- Positionen
def offene(state, trader=None, mint=None):
    return [p for p in state["positionen"] if p["status"] == "offen"
            and (trader is None or p["trader"] == trader) and (mint is None or p["mint"] == mint)]


def kaufe(state, w, mint, p, menge_trader, preis, liq):
    netto = EINSATZ_CHF * (1 - GEBUEHR_PCT / 100)
    pos = {
        "trader": w["name"], "wallet": w["wallet"], "mint": mint,
        "name": (p.get("baseToken") or {}).get("symbol") or mint[:6],
        "gekauft": jetzt().isoformat(timespec="seconds"),
        "einstieg_usd": preis, "liq_kauf": round(liq),
        "anteil": 1.0,            # wie viel unserer Position noch offen ist
        "erloes": 0.0,            # schon verkauft (nach Kosten), in Fr.
        "trader_max": menge_trader,
        "netto_start": netto,
        "letzter_x": 1.0, "hoechst_x": 1.0, "tiefst_x": 1.0,
        "verkaeufe": [], "status": "offen", "grund": "",
        "zuletzt_gesehen": jetzt().isoformat(timespec="seconds"),
    }
    state["positionen"].append(pos)
    print(f"  + KAUF {pos['name']} wie {w['name']} @ {preis:.8g} $ (Liq {liq:,.0f} $)")


def verkaufe_anteil(pos, teil, x, grund):
    """teil = Anteil der ursprünglichen Position, der jetzt verkauft wird."""
    teil = min(teil, pos["anteil"])
    if teil <= 0:
        return
    pos["letzter_x"] = x
    pos["hoechst_x"] = max(pos["hoechst_x"], x)
    pos["tiefst_x"] = min(pos["tiefst_x"], x)
    erloes = pos["netto_start"] * teil * x * (1 - GEBUEHR_PCT / 100)
    pos["erloes"] += erloes
    pos["anteil"] -= teil
    pos["verkaeufe"].append({"zeit": jetzt().isoformat(timespec="seconds"), "teil": round(teil, 4),
                             "x": round(x, 4), "grund": grund})
    if pos["anteil"] <= 1e-6:
        pos["anteil"] = 0.0
        pos["status"] = "verkauft"
        pos["grund"] = grund
        pos["geschlossen"] = jetzt().isoformat(timespec="seconds")


def pos_wert(pos):
    """Aktueller Wert in Fr. (verkaufter Teil + offener Teil zum letzten Kurs, ohne Verkaufskosten)."""
    if pos["status"] == "tot":
        return pos["erloes"]
    return pos["erloes"] + pos["netto_start"] * pos["anteil"] * pos["letzter_x"] * (1 - GEBUEHR_PCT / 100)


# ---------------------------------------------------------------- Ein Durchgang
def durchgang(state, wallets):
    alle_mints = set(p["mint"] for p in offene(state))
    neue_bestaende = {}
    for w in wallets:
        b = bestand(w["wallet"])
        if b is None:
            print(f"  ! Bestand von {w['name']} nicht lesbar, überspringe")
            continue
        neue_bestaende[w["wallet"]] = b
        alt = state["bestand"].get(w["wallet"])
        if alt is None:
            continue  # erste Sicht: nur merken, nichts kopieren
        for mint, menge in b.items():
            if menge > alt.get(mint, 0) * 1.0001:
                alle_mints.add(mint)

    paare = hole_paare(alle_mints) if alle_mints else {}

    for w in wallets:
        b = neue_bestaende.get(w["wallet"])
        if b is None:
            continue
        alt = state["bestand"].get(w["wallet"])
        state["bestand"][w["wallet"]] = b
        if alt is None:
            print(f"  {w['name']}: {len(b)} Coins im Bestand gemerkt (alte werden nicht kopiert)")
            continue

        # Verkäufe: Bestand eines Coins, den wir mit ihm halten, ist gesunken
        for pos in offene(state, trader=w["name"]):
            vorher = alt.get(pos["mint"], 0)
            nachher = b.get(pos["mint"], 0)
            if nachher > pos["trader_max"]:
                pos["trader_max"] = nachher  # er hat nachgekauft
            if vorher <= 0 or nachher >= vorher * 0.999:
                continue
            p = paare.get(pos["mint"])
            preis, _ = preis_von(p) if p else (None, 0)
            x = preis / pos["einstieg_usd"] if preis else pos["letzter_x"]
            if nachher <= pos["trader_max"] * REST_SCHWELLE:
                verkaufe_anteil(pos, pos["anteil"], x, "Trader hat alles verkauft")
            else:
                verkaufe_anteil(pos, pos["anteil"] * (1 - nachher / vorher), x, "Trader verkauft Teil")
            print(f"  - VERKAUF {pos['name']} wie {w['name']} bei {x:.2f}x "
                  f"({'alles' if pos['status'] != 'offen' else 'Teil'})")

        # Käufe: neuer Coin (vorher 0) mit echtem Betrag
        for mint, menge in b.items():
            if alt.get(mint, 0) > 0 or offene(state, trader=w["name"], mint=mint):
                continue
            p = paare.get(mint)
            if not p:
                continue
            preis, liq = preis_von(p)
            if not preis or liq < MIN_LIQ_USD or menge * preis < MIN_KAUF_USD:
                continue
            kaufe(state, w, mint, p, menge, preis, liq)

    # Kurse aller offenen Positionen nachführen, Tote abschreiben
    for pos in offene(state):
        p = paare.get(pos["mint"])
        if not p:
            fehlt_h = (jetzt() - datetime.fromisoformat(pos["zuletzt_gesehen"])).total_seconds() / 3600
            if fehlt_h >= TOT_FEHLT_STUNDEN:
                pos["status"], pos["grund"] = "tot", f"{TOT_FEHLT_STUNDEN} h nicht auffindbar"
                pos["geschlossen"] = jetzt().isoformat(timespec="seconds")
            continue
        preis, liq = preis_von(p)
        if not preis:
            continue
        x = preis / pos["einstieg_usd"]
        if x > pos["letzter_x"] * PLAUSI_SPRUNG_X and not pos.get("sprung_wartet"):
            pos["sprung_wartet"] = True  # erst beim nächsten Check glauben
            continue
        pos.pop("sprung_wartet", None)
        pos["letzter_x"] = x
        pos["hoechst_x"] = max(pos["hoechst_x"], x)
        pos["tiefst_x"] = min(pos["tiefst_x"], x)
        pos["zuletzt_gesehen"] = jetzt().isoformat(timespec="seconds")
        if x <= TOT_WERT_ANTEIL or liq < TOT_LIQ_USD:
            pos["status"], pos["grund"] = "tot", "−95 % oder Liquidität weg"
            pos["geschlossen"] = jetzt().isoformat(timespec="seconds")


# ---------------------------------------------------------------- Auswertung
def auswertung_text(state, wallets):
    ps = state["positionen"]
    z = [f"# Copy-Trader – Auswertung (Paper Trading)\n",
         f"Stand: {jetzt():%d.%m.%Y %H:%M} UTC. Je Kauf {fr(EINSATZ_CHF)}, {GEBUEHR_PCT:g} % Kosten "
         f"pro Kauf und Verkauf. Verkauft wird, wenn der Trader verkauft (gleicher Anteil).\n"]
    if not wallets:
        z.append("**Noch keine Wallets eingetragen** (data/copy/wallets.json).\n")
    if not ps:
        z.append("Noch keine kopierten Käufe.\n")
        return "\n".join(z)
    einsatz = len(ps) * EINSATZ_CHF
    wert = sum(pos_wert(p) for p in ps)
    offen = sum(1 for p in ps if p["status"] == "offen")
    tot = sum(1 for p in ps if p["status"] == "tot")
    z.append(f"## Gesamt\n\n{len(ps)} Käufe ({offen} offen, {tot} tot). Einsatz {fr(einsatz)}, "
             f"Wert {fr(wert)} → **{fr(wert - einsatz)} ({(wert / einsatz - 1) * 100:+.1f} %)**. "
             f"Offene Positionen zum letzten Kurs bewertet.\n")
    if len(ps) < 30:
        z.append("_Unter 30 Käufen: noch kein Urteil möglich._\n")

    z.append("## Pro Trader\n\n| Trader | Käufe | offen | Einsatz | Wert | Ergebnis | bester Coin |\n"
             "|---|---|---|---|---|---|---|")
    namen = sorted({p["trader"] for p in ps})
    zeilen = []
    for n in namen:
        tp = [p for p in ps if p["trader"] == n]
        e = len(tp) * EINSATZ_CHF
        v = sum(pos_wert(p) for p in tp)
        best = max(tp, key=pos_wert)
        zeilen.append((v - e, f"| {n} | {len(tp)} | {sum(1 for p in tp if p['status'] == 'offen')} | "
                              f"{fr(e)} | {fr(v)} | {(v / e - 1) * 100:+.0f} % | "
                              f"{best['name']} ({fr(pos_wert(best))}) |"))
    z += [s for _, s in sorted(zeilen, reverse=True)]

    gewinn = sum(max(0, pos_wert(p) - EINSATZ_CHF) for p in ps)
    if gewinn > 0:
        top = max(ps, key=pos_wert)
        anteil = (pos_wert(top) - EINSATZ_CHF) / gewinn * 100
        z.append(f"\nGrösster Einzelgewinn: {top['name']} ({top['trader']}) = {anteil:.0f} % aller Gewinne.")

    z.append("\n## Letzte 30 Käufe\n\n| Zeit (UTC) | Trader | Coin | Status | jetzt/Ende | Höchst | Wert |\n"
             "|---|---|---|---|---|---|---|")
    for p in sorted(ps, key=lambda p: p["gekauft"], reverse=True)[:30]:
        z.append(f"| {p['gekauft'][5:16].replace('T', ' ')} | {p['trader']} | {p['name']} | {p['status']} | "
                 f"{p['letzter_x']:.2f}x | {p['hoechst_x']:.2f}x | {fr(pos_wert(p))} |")
    return "\n".join(z) + "\n"


def schreibe_auswertung(state, wallets):
    BASIS.mkdir(parents=True, exist_ok=True)
    AUSWERTUNG_FILE.write_text(auswertung_text(state, wallets), encoding="utf-8")


def checkpoint(state, wallets):
    if not os.getenv("GITHUB_ACTIONS"):
        return
    schreibe_auswertung(state, wallets)
    befehl = ("git add data/copy && (git diff --cached --quiet || git commit -qm 'Copy-Trader-Zwischenstand') "
              "&& (git pull -q --rebase -X theirs origin main || (git rebase --abort; false)) && git push -q")
    try:
        subprocess.run(befehl, shell=True, check=True, timeout=120, cwd=Path(__file__).parent)
        print("  (Zwischenstand gesichert)")
    except Exception as e:
        print(f"  ! Zwischenstand nicht gesichert: {e!r}")


# ---------------------------------------------------------------- Hauptprogramm
def main():
    state = lade_state()
    wallets = lade_wallets()
    if "--auswertung" in sys.argv:
        print(auswertung_text(state, wallets))
        return
    if not wallets:
        print("Keine Wallets in data/copy/wallets.json – nichts zu tun.")
        schreibe_auswertung(state, wallets)
        return
    print(f"Beobachte {len(wallets)} Wallets: {', '.join(w['name'] for w in wallets)}")

    dauer_s = float(os.getenv("SCAN_DAUER_MIN", "0") or 0) * 60
    if os.getenv("GITHUB_EVENT_NAME") == "schedule":
        n = jetzt()
        bis = n.replace(minute=3, second=0, microsecond=0)
        if bis <= n:
            bis = datetime.fromtimestamp(bis.timestamp() + 3600, timezone.utc)
        dauer_s = min(dauer_s, max(60.0, (bis - n).total_seconds()))
        print(f"Dauerlauf bis {bis:%H:%M} UTC ({dauer_s / 60:.0f} Min.)")
    start = time.time()
    letzter_check = time.time()
    while True:
        takt = time.time()
        try:
            durchgang(state, wallets)
        except Exception as e:
            print(f"  ! Fehler im Durchgang: {e!r}")
        speichere_state(state)
        if time.time() - letzter_check >= CHECKPOINT_MIN * 60:
            checkpoint(state, wallets)
            letzter_check = time.time()
        if time.time() - start + CHECK_INTERVALL_S >= dauer_s:
            break
        time.sleep(max(1.0, CHECK_INTERVALL_S - (time.time() - takt)))
    speichere_state(state)
    schreibe_auswertung(state, wallets)
    print(f"Fertig. {len(state['positionen'])} Käufe total, {len(offene(state))} offen.")


if __name__ == "__main__":
    main()
