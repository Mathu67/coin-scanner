"""
Coin-Scanner (Paper Trading) – Solana Memecoins

Was er macht (läuft stündlich über GitHub Actions):
  1. Sammelt neue/aktive Solana-Coins (DexScreener + RugCheck).
  2. Prüft sie gegen Anti-Rugpull-Filter.
  3. "Kauft" jeden Treffer simuliert für 10 Fr.
  4. Verfolgt alle Positionen: Verkauf bei +300 %, Abschreibung wenn der Coin tot ist.
  5. Schickt am Monatsanfang die Monatsbilanz (als GitHub-Issue -> E-Mail,
     oder direkt per SMTP, falls eingerichtet).

Es wird KEIN echtes Geld bewegt. Alles ist Simulation.
"""

import json
import os
import smtplib
import sys
import time
from datetime import datetime, timezone
from email.mime.text import MIMEText
from pathlib import Path

import requests

# ---------------------------------------------------------------- Einstellungen
EINSATZ_CHF = 10.0          # simulierter Einsatz pro Coin
GEBUEHR_PCT = 1.0           # simulierte Gebühren + Slippage pro Trade (Kauf und Verkauf)
TAKE_PROFIT_X = 4.0         # 4x = +300 % -> verkaufen
MAX_KAEUFE_PRO_TAG = 10     # Schutz, falls der Markt komplett heiss läuft

# "Tot"-Regeln (eine reicht)
TOT_LIQ_USD = 1_000         # Liquidität unter 1'000 $
TOT_WERT_ANTEIL = 0.05      # Kurs ist 95 % oder mehr unter dem Einstieg
TOT_FEHLT_CHECKS = 24       # Coin 24 Checks in Folge (~1 Tag) nicht mehr auffindbar

# Einstiegs-Filter (Markt)
MIN_ALTER_H = 6             # die ersten Stunden sind die gefährlichsten
MAX_ALTER_H = 72            # danach nicht mehr "neu"
MIN_LIQ_USD = 25_000
MIN_MCAP_USD = 100_000
MAX_MCAP_USD = 20_000_000
MIN_VOL_24H_USD = 50_000
MIN_BUYS_24H = 150
MIN_SELLS_24H = 75          # genug Verkäufe = Verkaufen ist offenbar möglich (kein Honeypot)

# Einstiegs-Filter (Sicherheit, RugCheck)
MAX_TOP10_PCT = 25.0        # Top-10-Holder (ohne Pools) zusammen
MAX_EINZEL_HOLDER_PCT = 8.0
MAX_INSIDER_PCT = 10.0
MAX_CREATOR_PCT = 5.0
MIN_LP_GESPERRT_PCT = 90.0

STATE_FILE = Path(__file__).parent / "data" / "state.json"
DEX = "https://api.dexscreener.com"
RUG = "https://api.rugcheck.xyz/v1"
HEADERS = {"User-Agent": "paper-coin-scanner/1.0"}


# ---------------------------------------------------------------- Hilfsfunktionen
def jetzt():
    return datetime.now(timezone.utc)


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


def lade_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"positionen": [], "beobachtet": {}, "abgelehnt": {}, "letzte_bilanz": None}


def speichere_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")


def fr(x):
    return f"{x:,.2f} Fr.".replace(",", "'")


# ---------------------------------------------------------------- Daten holen
def sammle_kandidaten():
    """Solana-Mints aus mehreren Quellen."""
    mints = set()
    for path in ("/token-profiles/latest/v1", "/token-boosts/latest/v1", "/token-boosts/top/v1"):
        for t in get_json(DEX + path) or []:
            if t.get("chainId") == "solana" and t.get("tokenAddress"):
                mints.add(t["tokenAddress"])
    for path in ("/stats/new_tokens", "/stats/recent", "/stats/verified"):
        for t in get_json(RUG + path) or []:
            if t.get("mint"):
                mints.add(t["mint"])
    return mints


def hole_paare(mints):
    """Bestes (liquidestes) Paar pro Mint. DexScreener erlaubt 30 Adressen pro Anfrage."""
    beste = {}
    mints = list(mints)
    for i in range(0, len(mints), 30):
        teil = ",".join(mints[i:i + 30])
        for p in get_json(f"{DEX}/tokens/v1/solana/{teil}") or []:
            mint = (p.get("baseToken") or {}).get("address")
            if mint not in mints:
                continue  # Coin ist nur die Gegenwährung in diesem Paar
            liq = (p.get("liquidity") or {}).get("usd") or 0
            if mint not in beste or liq > ((beste[mint].get("liquidity") or {}).get("usd") or 0):
                beste[mint] = p
        time.sleep(0.3)
    return beste


# ---------------------------------------------------------------- Filter
def markt_check(p):
    """Gibt (ok, grund) zurück."""
    alter_h = (time.time() * 1000 - (p.get("pairCreatedAt") or 0)) / 3_600_000
    liq = (p.get("liquidity") or {}).get("usd") or 0
    mcap = p.get("marketCap") or p.get("fdv") or 0
    vol = (p.get("volume") or {}).get("h24") or 0
    tx = (p.get("txns") or {}).get("h24") or {}
    if not p.get("priceUsd"):
        return False, "kein USD-Preis"
    if alter_h < MIN_ALTER_H:
        return False, "zu jung"
    if alter_h > MAX_ALTER_H:
        return False, "zu alt"
    if liq < MIN_LIQ_USD:
        return False, f"Liquidität {liq:.0f}$"
    if not (MIN_MCAP_USD <= mcap <= MAX_MCAP_USD):
        return False, f"MCap {mcap:.0f}$"
    if vol < MIN_VOL_24H_USD:
        return False, f"Volumen {vol:.0f}$"
    if (tx.get("buys") or 0) < MIN_BUYS_24H or (tx.get("sells") or 0) < MIN_SELLS_24H:
        return False, "zu wenig Trades"
    return True, "ok"


def sicherheits_check(mint):
    r = get_json(f"{RUG}/tokens/{mint}/report")
    time.sleep(1.0)
    if not r:
        return False, "kein RugCheck-Report"
    if r.get("rugged"):
        return False, "als Rugpull markiert"
    if r.get("mintAuthority"):
        return False, "Mint Authority aktiv"
    if r.get("freezeAuthority"):
        return False, "Freeze Authority aktiv"
    for risk in r.get("risks") or []:
        if (risk.get("level") or "").lower() == "danger":
            return False, f"Risiko: {risk.get('name')}"

    # Pool-/Locker-Adressen sammeln, damit sie nicht als "Wal" zählen
    pool = set()
    for addr, info in (r.get("knownAccounts") or {}).items():
        if (info.get("type") or "").upper() in ("AMM", "LOCKER"):
            pool.add(addr)
    lp_pcts = []
    for m in r.get("markets") or []:
        for k in ("pubkey", "liquidityA", "liquidityB", "liquidityAAccount", "liquidityBAccount"):
            v = m.get(k)
            if isinstance(v, str) and v:
                pool.add(v)
            elif isinstance(v, dict):  # Konto-Objekt: Adresse und Besitzer
                for kk in ("pubkey", "owner"):
                    if isinstance(v.get(kk), str):
                        pool.add(v[kk])
        lp = m.get("lp") or {}
        if lp.get("lpLockedPct") is not None:
            lp_pcts.append((lp.get("quoteUSD") or 0, lp["lpLockedPct"]))
    if not lp_pcts:
        return False, "keine LP-Infos"
    _, haupt_lp_pct = max(lp_pcts)  # grösster Pool
    if haupt_lp_pct < MIN_LP_GESPERRT_PCT:
        return False, f"LP nur {haupt_lp_pct:.0f}% gesperrt"

    holder = [h for h in (r.get("topHolders") or [])
              if h.get("address") not in pool and h.get("owner") not in pool]
    top10 = sum(h.get("pct") or 0 for h in holder[:10])
    maxi = max([h.get("pct") or 0 for h in holder] or [0])
    insider = sum(h.get("pct") or 0 for h in holder if h.get("insider"))
    if top10 > MAX_TOP10_PCT:
        return False, f"Top-10 halten {top10:.0f}%"
    if maxi > MAX_EINZEL_HOLDER_PCT:
        return False, f"ein Wallet hält {maxi:.0f}%"
    if insider > MAX_INSIDER_PCT:
        return False, f"Insider halten {insider:.0f}%"

    supply = ((r.get("token") or {}).get("supply")) or 0
    creator_pct = 100 * (r.get("creatorBalance") or 0) / supply if supply else 0
    if creator_pct > MAX_CREATOR_PCT:
        return False, f"Ersteller hält {creator_pct:.0f}%"
    return True, f"Top10 {top10:.0f}%, LP {haupt_lp_pct:.0f}% gesperrt"


# ---------------------------------------------------------------- Positionen
def wert(pos, preis):
    """Aktueller Wert inkl. Kauf- und Verkaufsgebühr."""
    f = 1 - GEBUEHR_PCT / 100
    return EINSATZ_CHF * f * (preis / pos["einstieg_preis"]) * f


def update_positionen(state):
    offen = [p for p in state["positionen"] if p["status"] == "offen"]
    if not offen:
        return
    paare = hole_paare({p["mint"] for p in offen})
    for pos in offen:
        p = paare.get(pos["mint"])
        if not p or not p.get("priceUsd"):
            pos["fehlt"] = pos.get("fehlt", 0) + 1
            if pos["fehlt"] >= TOT_FEHLT_CHECKS:
                schliesse(pos, "tot", 0.0, "nicht mehr auffindbar")
            continue
        pos["fehlt"] = 0
        preis = float(p["priceUsd"])
        liq = (p.get("liquidity") or {}).get("usd") or 0
        pos["letzter_preis"] = preis
        pos["hoechst_x"] = max(pos.get("hoechst_x", 1.0), preis / pos["einstieg_preis"])
        x = preis / pos["einstieg_preis"]
        if x >= TAKE_PROFIT_X:
            schliesse(pos, "verkauft", wert(pos, preis), f"+{(x - 1) * 100:.0f}%")
        elif liq < TOT_LIQ_USD:
            schliesse(pos, "tot", wert(pos, preis), f"Liquidität {liq:.0f}$")
        elif x <= TOT_WERT_ANTEIL:
            schliesse(pos, "tot", wert(pos, preis), f"{(x - 1) * 100:.0f}%")


def schliesse(pos, status, erloes, grund):
    pos["status"] = status
    pos["erloes"] = round(erloes, 4)
    pos["grund"] = grund
    pos["geschlossen"] = jetzt().isoformat()
    print(f"  -> {pos['symbol']}: {status} ({grund}), Erlös {fr(erloes)}")


def scanne(state):
    heute = jetzt().date().isoformat()
    kaeufe_heute = sum(1 for p in state["positionen"] if p["gekauft"].startswith(heute))
    bekannt = {p["mint"] for p in state["positionen"]}

    neu = sammle_kandidaten()
    beob = state["beobachtet"]
    for m in neu:
        beob.setdefault(m, jetzt().isoformat())
    # Beobachtungsliste nach 4 Tagen aufräumen
    grenze = time.time() - 4 * 86400
    for m in list(beob):
        if datetime.fromisoformat(beob[m]).timestamp() < grenze:
            del beob[m]
    abgelehnt = state["abgelehnt"]  # Sicherheits-Ablehnungen 7 Tage merken
    for m in list(abgelehnt):
        if datetime.fromisoformat(abgelehnt[m]["zeit"]).timestamp() < time.time() - 7 * 86400:
            del abgelehnt[m]

    kandidaten = [m for m in beob if m not in bekannt and m not in abgelehnt]
    print(f"Beobachte {len(kandidaten)} Coins")
    paare = hole_paare(kandidaten)

    for mint, p in paare.items():
        if kaeufe_heute >= MAX_KAEUFE_PRO_TAG:
            print("Tageslimit erreicht")
            break
        ok, grund = markt_check(p)
        if not ok:
            if grund == "zu alt":
                beob.pop(mint, None)
            continue
        ok, grund = sicherheits_check(mint)
        sym = (p.get("baseToken") or {}).get("symbol", "?")
        if not ok:
            print(f"  x {sym}: {grund}")
            abgelehnt[mint] = {"zeit": jetzt().isoformat(), "grund": grund}
            beob.pop(mint, None)
            continue
        preis = float(p["priceUsd"])
        state["positionen"].append({
            "mint": mint,
            "symbol": sym,
            "name": (p.get("baseToken") or {}).get("name", ""),
            "url": p.get("url", ""),
            "gekauft": jetzt().isoformat(),
            "einstieg_preis": preis,
            "einstieg_mcap": p.get("marketCap") or p.get("fdv"),
            "letzter_preis": preis,
            "hoechst_x": 1.0,
            "status": "offen",
            "info": grund,
        })
        beob.pop(mint, None)
        kaeufe_heute += 1
        print(f"  + GEKAUFT (simuliert) {sym} @ {preis}$ – {grund}")


# ---------------------------------------------------------------- Bilanz
def pos_wert(p):
    if p["status"] == "offen":
        return wert(p, p.get("letzter_preis", p["einstieg_preis"]))
    return p.get("erloes", 0.0)


def bilanz_text(state, monat):
    """monat = 'YYYY-MM'. Bewertet alle Coins, die in diesem Monat gekauft wurden."""
    alle = state["positionen"]
    mon = [p for p in alle if p["gekauft"][:7] == monat]

    def block(ps):
        einsatz = len(ps) * EINSATZ_CHF
        wert_jetzt = sum(pos_wert(p) for p in ps)
        return einsatz, wert_jetzt, wert_jetzt - einsatz

    e, w, g = block(mon)
    verkauft = [p for p in mon if p["status"] == "verkauft"]
    tot = [p for p in mon if p["status"] == "tot"]
    offen = [p for p in mon if p["status"] == "offen"]
    ge, gw, gg = block(alle)

    z = [f"# Coin-Scanner – Bilanz {monat}", "",
         "_Paper Trading – kein echtes Geld. Werte inkl. simulierter Gebühren._", "",
         "## Dieser Monat",
         f"- Gekaufte Coins: **{len(mon)}** → Einsatz **{fr(e)}**",
         f"- Bei +300 % verkauft: **{len(verkauft)}** ({fr(sum(p['erloes'] for p in verkauft))})",
         f"- Tot abgeschrieben: **{len(tot)}** (Restwert {fr(sum(p['erloes'] for p in tot))})",
         f"- Noch offen: **{len(offen)}** (aktueller Wert {fr(sum(pos_wert(p) for p in offen))})",
         f"- **Ergebnis: {'+' if g >= 0 else ''}{fr(g)}** "
         f"({(g / e * 100 if e else 0):+.0f} %)", "",
         "## Gesamt seit Start",
         f"- {len(alle)} Coins, Einsatz {fr(ge)}, Wert {fr(gw)} → "
         f"**{'+' if gg >= 0 else ''}{fr(gg)}** ({(gg / ge * 100 if ge else 0):+.0f} %)", ""]

    if mon:
        sortiert = sorted(mon, key=pos_wert, reverse=True)
        z += ["## Alle Coins dieses Monats", "",
              "| Coin | Status | Wert | Max. erreicht |", "|---|---|---|---|"]
        for p in sortiert:
            z.append(f"| [{p['symbol']}]({p['url']}) | {p['status']}"
                     f"{' – ' + p['grund'] if p.get('grund') else ''} | {fr(pos_wert(p))} | "
                     f"{p.get('hoechst_x', 1):.1f}x |")
    return "\n".join(z)


def sende(titel, text):
    """Per SMTP, falls eingerichtet – sonst als GitHub-Issue (GitHub mailt es dir)."""
    host, user, pw = os.getenv("SMTP_HOST"), os.getenv("SMTP_USER"), os.getenv("SMTP_PASS")
    an = os.getenv("MAIL_TO") or user
    if host and user and pw:
        msg = MIMEText(text, "plain", "utf-8")
        msg["Subject"], msg["From"], msg["To"] = titel, user, an
        with smtplib.SMTP_SSL(host, int(os.getenv("SMTP_PORT", "465"))) as s:
            s.login(user, pw)
            s.send_message(msg)
        print("Bilanz per E-Mail gesendet")
        return
    token, repo = os.getenv("GITHUB_TOKEN"), os.getenv("GITHUB_REPOSITORY")
    if token and repo:
        r = requests.post(f"https://api.github.com/repos/{repo}/issues",
                          headers={"Authorization": f"Bearer {token}",
                                   "Accept": "application/vnd.github+json"},
                          json={"title": titel, "body": text}, timeout=20)
        r.raise_for_status()
        print("Bilanz als Issue erstellt:", r.json().get("html_url"))
        return
    print(text)  # lokal: einfach anzeigen


def monatsbilanz_faellig(state):
    aktuell = jetzt().strftime("%Y-%m")
    letzte = state.get("letzte_bilanz")
    if letzte is None:  # erster Lauf: Startpunkt merken
        state["letzte_bilanz"] = aktuell
        return None
    if letzte != aktuell:
        y, m = map(int, aktuell.split("-"))
        vormonat = f"{y - 1}-12" if m == 1 else f"{y}-{m - 1:02d}"
        state["letzte_bilanz"] = aktuell
        return vormonat
    return None


# ---------------------------------------------------------------- Start
def main():
    state = lade_state()
    nur_bilanz = "--bilanz" in sys.argv
    if not nur_bilanz:
        print("== Positionen aktualisieren")
        update_positionen(state)
        print("== Neue Coins scannen")
        scanne(state)
        monat = monatsbilanz_faellig(state)
        if monat:
            sende(f"🪙 Coin-Scanner Monatsbilanz {monat}", bilanz_text(state, monat))
    else:
        monat = jetzt().strftime("%Y-%m")
        sende(f"🪙 Coin-Scanner Zwischenstand {monat}", bilanz_text(state, monat))
    speichere_state(state)
    offen = sum(1 for p in state["positionen"] if p["status"] == "offen")
    print(f"Fertig. {len(state['positionen'])} Positionen total, {offen} offen.")


if __name__ == "__main__":
    main()
