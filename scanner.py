"""
Coin-Scanner (Paper Trading) – Solana Memecoins

Was er macht (läuft über GitHub Actions, im Dauerlauf mit Kurs-Check alle 60 Sekunden):
  1. Sammelt neue/aktive Solana-Coins (DexScreener + RugCheck).
  2. Prüft sie gegen Anti-Rugpull-Filter.
  3. "Kauft" jeden Treffer simuliert für 10 Fr.
  4. Verfolgt jede Position GLEICHZEITIG mit drei Verkaufsregeln:
       A: alles bei +300 % (4x) verkaufen.
       B: bei 4x nur die Hälfte verkaufen, den Rest laufen lassen
          (Verkauf bei 20x oder wenn der Kurs 50 % unter seine Spitze fällt).
       C: bei 2x so viel verkaufen, dass der Einsatz (10 Fr.) zurück ist, den Rest
          ohne Stop laufen lassen (Verkauf bei 20x, sonst bis er tot ist).
     Tot ist ein Coin bei -95 %, < 1'000 $ Liquidität oder 1 Tag nicht auffindbar.
  5. Schreibt bei jedem Lauf data/auswertung.md (A gegen B, Trefferquote, Zielvergleich).
  6. Schickt am Monatsanfang die Monatsbilanz (als GitHub-Issue -> E-Mail,
     oder direkt per SMTP, falls eingerichtet).

Es wird KEIN echtes Geld bewegt. Alles ist Simulation.
"""

import json
import os
import smtplib
import subprocess
import sys
import time
from datetime import datetime, timezone
from email.mime.text import MIMEText
from pathlib import Path

import requests

# ---------------------------------------------------------------- Einstellungen
EINSATZ_CHF = 10.0          # simulierter Einsatz pro Coin
GEBUEHR_PCT = 4.0           # realistischere Kosten pro Trade (Kauf UND Verkauf): Swap-Gebühr,
                            # Priority-Fee, Slippage bei dünner Liquidität
TAKE_PROFIT_X = 4.0         # 4x = +300 % -> verkaufen
MAX_KAEUFE_PRO_TAG = 10     # Schutz, falls der Markt komplett heiss läuft

# Regel B: bei 4x die Hälfte verkaufen, den Rest laufen lassen
B_TEIL_ANTEIL = 0.5         # so viel wird bei 4x verkauft
B_REST_ZIEL_X = 20.0        # Rest wird bei 20x verkauft ...
B_TRAILING = 0.5            # ... oder wenn der Kurs auf 50 % seiner Spitze fällt

# Regel C: bei 2x den Einsatz rausnehmen, Rest läuft ohne Stop
C_AUSLOESER_X = 2.0         # ab hier wird der Einsatz zurückgeholt
C_REST_ZIEL_X = 20.0        # Rest wird bei 20x verkauft, sonst läuft er, bis er tot ist

# Regel D (ab 7.11.2026): Verluste früh begrenzen, Gewinner ohne Deckel laufen lassen
D_START = "2026-11-07T10:30:00+00:00"   # nur Coins, die ab hier gekauft werden (kein Schätzen)
D_STOP_X = 0.6              # vor dem Teilverkauf: alles raus, wenn der Kurs auf 0.6x fällt (-40 %)
D_ZEIT_STOP_H = 48          # nach 48 h ohne Teilverkauf und unter Einstieg: alles raus (blutet sonst aus)
D_AUSLOESER_X = 2.0         # bei 2x den Einsatz zurückholen (wie C)
D_TRAIL_AB_X = 5.0          # Rest: Trailing-Stop erst, wenn er mal 5x erreicht hat ...
D_TRAILING = 0.5            # ... dann verkaufen, sobald er auf 50 % seiner Spitze fällt (kein 20x-Deckel)

# Kursverlauf pro Coin (data/verlauf/<mint>.csv), damit man Regeln später exakt nachrechnen kann
VERLAUF_SCHRITT = 0.05      # neuer Punkt, wenn sich der Kurs um 5 % bewegt hat ...
VERLAUF_MAX_MIN = 15        # ... oder spätestens alle 15 Minuten

# Plausibilitäts-Filter gegen kaputte Preise (z.B. Rocco am 7.11.2026: 49'677x in einer Minute)
PLAUSI_SPRUNG_X = 20.0      # Preis mehr als 20x über dem letzten Check -> erst beim nächsten Check glauben
PLAUSI_MAX_MCAP_USD = 1_000_000_000   # Marktkapitalisierung über 1 Mrd. $ -> Preis ignorieren

# Positionen mit nachweislich falschen Preisdaten: werden einmalig zurückgesetzt
KORREKTUR_MINTS = {
    "HZbiEpF2oM658EpjNRRqxharz5L9Ddm8akpSH2R5pump": "Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026",
}

# Zielvergleich in der Auswertung: "Was wäre gewesen, wenn alles bei Nx verkauft worden wäre?"
ZIEL_VERGLEICH = [2, 3, 4, 5, 10, 20]

# Coins mit diesen Wörtern im Namen/Symbol werden im Detail protokolliert,
# damit man später sieht, ob der Bot sie gesehen und warum er sie gekauft/abgelehnt hat.
SCHLAGWORTE = ["gta", "grand theft", "rockstar", "claude", "anthropic"]

# "Tot"-Regeln (eine reicht)
TOT_LIQ_USD = 1_000         # Liquidität unter 1'000 $
TOT_WERT_ANTEIL = 0.05      # Kurs ist 95 % oder mehr unter dem Einstieg
TOT_FEHLT_STUNDEN = 24      # Coin 24 Stunden am Stück nicht mehr auffindbar

# Takt (im Dauerlauf, siehe SCAN_DAUER_MIN)
CHECK_INTERVALL_S = 60      # offene Positionen: Kurs alle 60 Sekunden prüfen
SCAN_INTERVALL_MIN = 5      # nach neuen Coins suchen: alle 5 Minuten
CHECKPOINT_MIN = 15         # Zwischenstand ins Repo sichern (bei GitHub Actions)

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
    return {"positionen": [], "beobachtet": {}, "abgelehnt": {}, "letzte_bilanz": None,
            "schlagwort_log": {}}


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
def wert(pos, preis, anteil=1.0):
    """Wert eines Anteils der Position inkl. Kauf- und Verkaufsgebühr."""
    f = 1 - GEBUEHR_PCT / 100
    return EINSATZ_CHF * anteil * f * (preis / pos["einstieg_preis"]) * f


def stelle_b_sicher(pos):
    """Regel B pro Position anlegen (auch für Positionen aus älteren Läufen)."""
    if "b" in pos:
        return pos["b"]
    if pos["status"] == "offen":
        pos["b"] = {"status": "offen", "teil": False, "erloes_teil": 0.0}
    else:  # alte, schon geschlossene Position: B übernimmt das Ergebnis von A
        pos["b"] = {"status": pos["status"], "teil": False, "erloes_teil": 0.0,
                    "erloes": pos.get("erloes", 0.0), "grund": pos.get("grund", "")}
    return pos["b"]


def stelle_c_sicher(pos):
    """Regel C pro Position anlegen. Bei älteren Positionen rückwirkend aus dem bisherigen
    Höchststand geschätzt (2x erreicht = Einsatz genau bei 2x zurückgeholt)."""
    if "c" in pos:
        return pos["c"]
    c = {"status": "offen", "teil": False, "erloes_teil": 0.0, "anteil_teil": 0.0}
    hx = pos.get("hoechst_x", 1.0)
    tot = pos["status"] == "tot" or stelle_b_sicher(pos)["status"] == "tot"
    if "letzter_x" in pos:  # Position lief schon vor Regel C
        c["rueckwirkend"] = True
    if hx >= C_AUSLOESER_X:
        voll = wert(pos, pos["einstieg_preis"] * C_AUSLOESER_X)
        a = min(1.0, EINSATZ_CHF / voll)
        c.update(teil=True, anteil_teil=round(a, 4), erloes_teil=round(voll * a, 4),
                 teil_x=C_AUSLOESER_X)
        if hx >= C_REST_ZIEL_X:
            rest = wert(pos, pos["einstieg_preis"] * C_REST_ZIEL_X, 1 - a)
            c.update(status="verkauft", erloes=round(c["erloes_teil"] + rest, 4),
                     grund=f"Rest bei {C_REST_ZIEL_X:.0f}x (rückwirkend)")
        elif tot:
            c.update(status="tot", erloes=c["erloes_teil"], grund="Rest tot (rückwirkend)")
    elif tot:
        c.update(status="tot", erloes=pos.get("erloes", 0.0), grund=pos.get("grund", "tot"))
    pos["c"] = c
    return c


def stelle_d_sicher(pos):
    """Regel D pro Position anlegen. Ältere Coins (vor D_START) sind bewusst nicht dabei:
    Ob ein Stop-Loss gegriffen hätte, hängt von der Reihenfolge der Kurse ab, die fehlt."""
    if "d" in pos:
        return pos["d"]
    if pos["gekauft"] < D_START:
        pos["d"] = {"status": "nicht dabei"}
    else:
        pos["d"] = {"status": "offen", "teil": False, "erloes_teil": 0.0, "anteil_teil": 0.0,
                    "spitze_x": 1.0}
    return pos["d"]


def notiere_verlauf(pos, x, liq):
    """Hängt einen Kurspunkt an data/verlauf/<mint>.csv an (nur bei Bewegung oder alle 15 Min.)."""
    v = pos.setdefault("verlauf_letzt", {})
    t = time.time()
    lx = v.get("x")
    if lx and abs(x / lx - 1) < VERLAUF_SCHRITT and t - v.get("t", 0) < VERLAUF_MAX_MIN * 60:
        return
    pfad = STATE_FILE.parent / "verlauf" / f"{pos['mint']}.csv"
    try:
        pfad.parent.mkdir(exist_ok=True)
        neu = not pfad.exists()
        with pfad.open("a", encoding="utf-8") as f:
            if neu:
                f.write("zeit,x,liq_usd\n")
            f.write(f"{jetzt().strftime('%Y-%m-%dT%H:%M:%S')},{x:.5g},{liq:.0f}\n")
        pos["verlauf_letzt"] = {"x": x, "t": t}
    except OSError as e:
        print(f"  ! Verlauf nicht geschrieben: {e!r}")


def korrigiere_daten(state):
    """Setzt Positionen mit nachweislich falschen Preisdaten einmalig zurück auf 'offen'."""
    for pos in state["positionen"]:
        grund = KORREKTUR_MINTS.get(pos["mint"])
        if not grund or pos.get("korrigiert"):
            continue
        for k in ("erloes", "grund", "geschlossen"):
            pos.pop(k, None)
        pos.update(status="offen", letzter_preis=pos["einstieg_preis"], letzter_x=1.0,
                   hoechst_x=1.0, korrigiert=grund)
        pos["b"] = {"status": "offen", "teil": False, "erloes_teil": 0.0}
        pos.pop("c", None)
        print(f"  * {pos['symbol']} korrigiert: {grund}")


def preis_plausibel(pos, p, preis):
    """Filtert kaputte Preise: absurde Marktkapitalisierung oder ein Riesensprung in einer Minute,
    der beim nächsten Check nicht bestätigt wird."""
    mcap = p.get("marketCap") or p.get("fdv") or 0
    if mcap > PLAUSI_MAX_MCAP_USD:
        print(f"  ? {pos['symbol']}: Preis ignoriert (MCap {mcap:,.0f} $ unplausibel)")
        return False
    letzter = pos.get("letzter_preis") or pos["einstieg_preis"]
    if preis > letzter * PLAUSI_SPRUNG_X:
        v = pos.get("verdacht_preis")
        if v and 0.5 * v <= preis <= 2 * v:
            pos.pop("verdacht_preis", None)
            return True  # zweimal hintereinander gesehen -> glauben
        pos["verdacht_preis"] = preis
        print(f"  ? {pos['symbol']}: Sprung auf {preis / pos['einstieg_preis']:.0f}x, warte auf Bestätigung")
        return False
    pos.pop("verdacht_preis", None)
    return True


def update_positionen(state):
    korrigiere_daten(state)
    offen = []
    for p in state["positionen"]:
        b = stelle_b_sicher(p)
        c = stelle_c_sicher(p)
        d = stelle_d_sicher(p)
        if "offen" in (p["status"], b["status"], c["status"], d["status"]):
            offen.append(p)
    if not offen:
        return
    paare = hole_paare({p["mint"] for p in offen})
    for pos in offen:
        b = pos["b"]
        c = pos["c"]
        d = pos["d"]
        p = paare.get(pos["mint"])
        if not p or not p.get("priceUsd"):
            seit = pos.setdefault("fehlt_seit", jetzt().isoformat())
            if (jetzt() - datetime.fromisoformat(seit)).total_seconds() >= TOT_FEHLT_STUNDEN * 3600:
                if pos["status"] == "offen":
                    schliesse(pos, "tot", 0.0, "nicht mehr auffindbar")
                if b["status"] == "offen":
                    schliesse_b(pos, "tot", 0.0, "nicht mehr auffindbar")
                if c["status"] == "offen":
                    schliesse_c(pos, "tot", c["erloes_teil"], "nicht mehr auffindbar")
                if d["status"] == "offen":
                    schliesse_d(pos, "tot", d["erloes_teil"], "nicht mehr auffindbar")
            continue
        pos.pop("fehlt_seit", None)
        pos.pop("fehlt", None)
        preis = float(p["priceUsd"])
        liq = (p.get("liquidity") or {}).get("usd") or 0
        if not preis_plausibel(pos, p, preis):
            continue
        x = preis / pos["einstieg_preis"]
        pos["letzter_preis"] = preis
        pos["letzter_x"] = round(x, 4)
        pos["hoechst_x"] = max(pos.get("hoechst_x", 1.0), x)
        pos["tiefst_x"] = min(pos.get("tiefst_x", 1.0), x)
        notiere_verlauf(pos, x, liq)

        # ---- Regel A: alles bei 4x verkaufen
        if pos["status"] == "offen":
            if x >= TAKE_PROFIT_X:
                schliesse(pos, "verkauft", wert(pos, preis), f"+{(x - 1) * 100:.0f}%")
            elif liq < TOT_LIQ_USD:
                schliesse(pos, "tot", wert(pos, preis), f"Liquidität {liq:.0f}$")
            elif x <= TOT_WERT_ANTEIL:
                schliesse(pos, "tot", wert(pos, preis), f"{(x - 1) * 100:.0f}%")

        # ---- Regel B: bei 4x die Hälfte verkaufen, Rest laufen lassen
        if b["status"] == "offen":
            if not b["teil"] and x >= TAKE_PROFIT_X:
                b["teil"] = True
                b["erloes_teil"] = round(wert(pos, preis, B_TEIL_ANTEIL), 4)
                b["teil_x"] = round(x, 3)
                b["spitze_preis"] = preis
                print(f"  ~ {pos['symbol']}: B verkauft Hälfte bei {x:.1f}x ({fr(b['erloes_teil'])})")
            if b["teil"]:
                b["spitze_preis"] = max(b["spitze_preis"], preis)
                rest = wert(pos, preis, 1 - B_TEIL_ANTEIL)
                if x >= B_REST_ZIEL_X:
                    schliesse_b(pos, "verkauft", b["erloes_teil"] + rest, f"Rest bei {x:.0f}x")
                elif preis <= b["spitze_preis"] * B_TRAILING:
                    schliesse_b(pos, "verkauft", b["erloes_teil"] + rest,
                                f"Trailing-Stop (Spitze {b['spitze_preis'] / pos['einstieg_preis']:.1f}x, "
                                f"jetzt {x:.1f}x)")
                elif liq < TOT_LIQ_USD or x <= TOT_WERT_ANTEIL:
                    schliesse_b(pos, "tot", b["erloes_teil"] + rest, f"Rest tot ({x:.2f}x)")
            elif liq < TOT_LIQ_USD:
                schliesse_b(pos, "tot", wert(pos, preis), f"Liquidität {liq:.0f}$")
            elif x <= TOT_WERT_ANTEIL:
                schliesse_b(pos, "tot", wert(pos, preis), f"{(x - 1) * 100:.0f}%")

        # ---- Regel C: bei 2x Einsatz rausnehmen, Rest ohne Stop bis 20x oder tot
        if c["status"] == "offen":
            if not c["teil"] and x >= C_AUSLOESER_X:
                voll = wert(pos, preis)
                a = min(1.0, EINSATZ_CHF / voll)
                c.update(teil=True, anteil_teil=round(a, 4), erloes_teil=round(voll * a, 4),
                         teil_x=round(x, 3))
                print(f"  ~ {pos['symbol']}: C holt Einsatz bei {x:.1f}x raus ({a * 100:.0f} % verkauft)")
            if c["teil"]:
                rest = wert(pos, preis, 1 - c["anteil_teil"])
                if x >= C_REST_ZIEL_X:
                    schliesse_c(pos, "verkauft", c["erloes_teil"] + rest, f"Rest bei {x:.0f}x")
                elif liq < TOT_LIQ_USD or x <= TOT_WERT_ANTEIL:
                    schliesse_c(pos, "tot", c["erloes_teil"] + rest, f"Rest tot ({x:.2f}x)")
            elif liq < TOT_LIQ_USD:
                schliesse_c(pos, "tot", wert(pos, preis), f"Liquidität {liq:.0f}$")
            elif x <= TOT_WERT_ANTEIL:
                schliesse_c(pos, "tot", wert(pos, preis), f"{(x - 1) * 100:.0f}%")

        # ---- Regel D: Stop bei 0.6x, Zeit-Stop 48 h, Einsatz bei 2x raus, Rest mit Trailing ab 5x
        if d["status"] == "offen":
            d["spitze_x"] = max(d.get("spitze_x", 1.0), x)
            alter_h = (jetzt() - datetime.fromisoformat(pos["gekauft"])).total_seconds() / 3600
            if not d["teil"] and x >= D_AUSLOESER_X:
                voll = wert(pos, preis)
                a = min(1.0, EINSATZ_CHF / voll)
                d.update(teil=True, anteil_teil=round(a, 4), erloes_teil=round(voll * a, 4),
                         teil_x=round(x, 3))
                print(f"  ~ {pos['symbol']}: D holt Einsatz bei {x:.1f}x raus ({a * 100:.0f} % verkauft)")
            if d["teil"]:
                rest = wert(pos, preis, 1 - d["anteil_teil"])
                if d["spitze_x"] >= D_TRAIL_AB_X and x <= d["spitze_x"] * D_TRAILING:
                    schliesse_d(pos, "verkauft", d["erloes_teil"] + rest,
                                f"Trailing-Stop (Spitze {d['spitze_x']:.1f}x, jetzt {x:.1f}x)")
                elif liq < TOT_LIQ_USD or x <= TOT_WERT_ANTEIL:
                    schliesse_d(pos, "tot", d["erloes_teil"] + rest, f"Rest tot ({x:.2f}x)")
            elif liq < TOT_LIQ_USD:
                schliesse_d(pos, "tot", wert(pos, preis), f"Liquidität {liq:.0f}$")
            elif x <= D_STOP_X:
                schliesse_d(pos, "verkauft", wert(pos, preis), f"Stop-Loss bei {x:.2f}x")
            elif alter_h >= D_ZEIT_STOP_H and x < 1.0:
                schliesse_d(pos, "verkauft", wert(pos, preis), f"Zeit-Stop nach {alter_h:.0f} h ({x:.2f}x)")


def schliesse(pos, status, erloes, grund):
    pos["status"] = status
    pos["erloes"] = round(erloes, 4)
    pos["grund"] = grund
    pos["geschlossen"] = jetzt().isoformat()
    print(f"  -> {pos['symbol']}: A {status} ({grund}), Erlös {fr(erloes)}")


def schliesse_b(pos, status, erloes, grund):
    b = pos["b"]
    b["status"] = status
    b["erloes"] = round(erloes, 4)
    b["grund"] = grund
    b["geschlossen"] = jetzt().isoformat()
    print(f"  -> {pos['symbol']}: B {status} ({grund}), Erlös {fr(erloes)}")


def schliesse_c(pos, status, erloes, grund):
    c = pos["c"]
    c["status"] = status
    c["erloes"] = round(erloes, 4)
    c["grund"] = grund
    c["geschlossen"] = jetzt().isoformat()
    print(f"  -> {pos['symbol']}: C {status} ({grund}), Erlös {fr(erloes)}")


def schliesse_d(pos, status, erloes, grund):
    d = pos["d"]
    d["status"] = status
    d["erloes"] = round(erloes, 4)
    d["grund"] = grund
    d["geschlossen"] = jetzt().isoformat()
    print(f"  -> {pos['symbol']}: D {status} ({grund}), Erlös {fr(erloes)}")


def notiere_schlagwort(state, mint, p, entscheid):
    """Protokolliert Coins mit Schlagwörtern (z. B. GTA) samt Entscheidung des Bots."""
    bt = p.get("baseToken") or {}
    text = f"{bt.get('name', '')} {bt.get('symbol', '')}".lower()
    if not any(w in text for w in SCHLAGWORTE):
        return
    log = state.setdefault("schlagwort_log", {})
    liq = (p.get("liquidity") or {}).get("usd") or 0
    alter_h = (time.time() * 1000 - (p.get("pairCreatedAt") or 0)) / 3_600_000
    e = log.setdefault(mint, {"symbol": bt.get("symbol", "?"), "name": bt.get("name", ""),
                              "url": p.get("url", ""), "zuerst_gesehen": jetzt().isoformat(),
                              "verlauf": []})
    e["zuletzt_gesehen"] = jetzt().isoformat()
    e["entscheid"] = entscheid
    e["alter_h"] = round(alter_h, 1)
    e["liquiditaet_usd"] = round(liq)
    e["mcap_usd"] = round(p.get("marketCap") or p.get("fdv") or 0)
    if not e["verlauf"] or e["verlauf"][-1] != entscheid:
        e["verlauf"] = (e["verlauf"] + [entscheid])[-8:]


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
            notiere_schlagwort(state, mint, p, f"Markt-Filter: {grund}")
            if grund == "zu alt":
                beob.pop(mint, None)
            continue
        ok, grund = sicherheits_check(mint)
        sym = (p.get("baseToken") or {}).get("symbol", "?")
        if not ok:
            print(f"  x {sym}: {grund}")
            notiere_schlagwort(state, mint, p, f"Sicherheits-Filter: {grund}")
            abgelehnt[mint] = {"zeit": jetzt().isoformat(), "grund": grund, "symbol": sym}
            beob.pop(mint, None)
            continue
        notiere_schlagwort(state, mint, p, "GEKAUFT (simuliert)")
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
            "tiefst_x": 1.0,
            "letzter_x": 1.0,
            "status": "offen",
            "b": {"status": "offen", "teil": False, "erloes_teil": 0.0},
            "c": {"status": "offen", "teil": False, "erloes_teil": 0.0, "anteil_teil": 0.0},
            "d": {"status": "offen", "teil": False, "erloes_teil": 0.0, "anteil_teil": 0.0,
                  "spitze_x": 1.0},
            "info": grund,
        })
        beob.pop(mint, None)
        kaeufe_heute += 1
        print(f"  + GEKAUFT (simuliert) {sym} @ {preis}$ – {grund}")


# ---------------------------------------------------------------- Bilanz
def pos_wert(p):
    """Wert nach Regel A (alles bei 4x verkaufen)."""
    if p["status"] == "offen":
        return wert(p, p.get("letzter_preis", p["einstieg_preis"]))
    return p.get("erloes", 0.0)


def pos_wert_b(p):
    """Wert nach Regel B (Hälfte bei 4x, Rest laufen lassen)."""
    b = stelle_b_sicher(p)
    if b["status"] == "offen":
        preis = p.get("letzter_preis", p["einstieg_preis"])
        if b["teil"]:
            return b["erloes_teil"] + wert(p, preis, 1 - B_TEIL_ANTEIL)
        return wert(p, preis)
    return b.get("erloes", 0.0)


def pos_wert_c(p):
    """Wert nach Regel C (Einsatz bei 2x raus, Rest ohne Stop)."""
    c = stelle_c_sicher(p)
    if c["status"] == "offen":
        preis = p.get("letzter_preis", p["einstieg_preis"])
        if c["teil"]:
            return c["erloes_teil"] + wert(p, preis, 1 - c["anteil_teil"])
        return wert(p, preis)
    return c.get("erloes", 0.0)


def pos_wert_d(p):
    """Wert nach Regel D (Stop 0.6x, Zeit-Stop, Einsatz bei 2x raus, Trailing ab 5x)."""
    d = stelle_d_sicher(p)
    if d["status"] == "offen":
        preis = p.get("letzter_preis", p["einstieg_preis"])
        if d["teil"]:
            return d["erloes_teil"] + wert(p, preis, 1 - d["anteil_teil"])
        return wert(p, preis)
    return d.get("erloes", 0.0)


def mit_d(ps):
    return [p for p in ps if stelle_d_sicher(p)["status"] != "nicht dabei"]


def d_vergleich(ps):
    """Fairer Vergleich: alle vier Regeln nur auf den Coins, bei denen D dabei ist."""
    dp = mit_d(ps)
    if not dp:
        return [f"- Regel D (Stop 0.6x, Zeit-Stop {D_ZEIT_STOP_H} h, Einsatz bei 2x raus, Trailing ab "
                f"{D_TRAIL_AB_X:.0f}x): noch keine Coins (läuft für Käufe ab {D_START[:10]})"]
    e = len(dp) * EINSATZ_CHF
    z = [f"- Vergleich auf den **{len(dp)} Coins seit Start von Regel D** (Einsatz {fr(e)}):"]
    for name, fn in (("A", pos_wert), ("B", pos_wert_b), ("C", pos_wert_c), ("D", pos_wert_d)):
        _, _, g = ergebnis(dp, fn)
        z.append(f"  - {name}: **{vz(g)}** ({prozent(g, e)})")
    return z


def pos_wert_ziel(p, ziel_x):
    """Was wäre gewesen, wenn alles bei Nx verkauft worden wäre? (Näherung aus den Minutenpreisen)
    Erreicht der Coin das Ziel nie, zählt sein letzter bekannter Stand."""
    f = 1 - GEBUEHR_PCT / 100
    x = ziel_x if p.get("hoechst_x", 1.0) >= ziel_x else max(p.get("letzter_x", 1.0), 0.0)
    return EINSATZ_CHF * f * x * f


def ergebnis(ps, wertfn):
    einsatz = len(ps) * EINSATZ_CHF
    w = sum(wertfn(p) for p in ps)
    return einsatz, w, w - einsatz


def prozent(g, e):
    return f"{(g / e * 100 if e else 0):+.0f} %"


def vz(g):
    return f"{'+' if g >= 0 else ''}{fr(g)}"


def bilanz_text(state, monat):
    """monat = 'YYYY-MM'. Bewertet alle Coins, die in diesem Monat gekauft wurden."""
    alle = state["positionen"]
    mon = [p for p in alle if p["gekauft"][:7] == monat]
    for p in alle:
        stelle_b_sicher(p)
        stelle_c_sicher(p)

    e, w, g = ergebnis(mon, pos_wert)
    _, wb, gb = ergebnis(mon, pos_wert_b)
    _, wc, gc = ergebnis(mon, pos_wert_c)
    _, gwc, ggc = ergebnis(alle, pos_wert_c)
    ge, gw, gg = ergebnis(alle, pos_wert)
    _, gwb, ggb = ergebnis(alle, pos_wert_b)
    verkauft = [p for p in mon if p["status"] == "verkauft"]
    tot = [p for p in mon if p["status"] == "tot"]
    offen = [p for p in mon if p["status"] == "offen"]

    z = [f"# Coin-Scanner – Bilanz {monat}", "",
         "_Paper Trading – kein echtes Geld. Werte inkl. simulierter Gebühren._", "",
         "## Dieser Monat",
         f"- Gekaufte Coins: **{len(mon)}** → Einsatz **{fr(e)}**",
         f"- Regel A (alles bei 4x): **{vz(g)}** ({prozent(g, e)}) – "
         f"{len(verkauft)} verkauft, {len(tot)} tot, {len(offen)} offen",
         f"- Regel B (Hälfte bei 4x, Rest läuft): **{vz(gb)}** ({prozent(gb, e)})",
         f"- Regel C (Einsatz bei 2x raus, Rest ohne Stop): **{vz(gc)}** ({prozent(gc, e)})",
         *d_vergleich(mon), "",
         "## Gesamt seit Start",
         f"- {len(alle)} Coins, Einsatz {fr(ge)}",
         f"- Regel A: **{vz(gg)}** ({prozent(gg, ge)})",
         f"- Regel B: **{vz(ggb)}** ({prozent(ggb, ge)})",
         f"- Regel C: **{vz(ggc)}** ({prozent(ggc, ge)})",
         *d_vergleich(alle), ""]

    if mon:
        sortiert = sorted(mon, key=pos_wert, reverse=True)
        z += ["## Alle Coins dieses Monats", "",
              "| Coin | Status A | Wert A | Wert B | Wert C | Max. erreicht |", "|---|---|---|---|---|---|"]
        for p in sortiert:
            z.append(f"| [{p['symbol']}]({p['url']}) | {p['status']}"
                     f"{' – ' + p['grund'] if p.get('grund') else ''} | {fr(pos_wert(p))} | "
                     f"{fr(pos_wert_b(p))} | {fr(pos_wert_c(p))} | {p.get('hoechst_x', 1):.1f}x |")
    return "\n".join(z)


def auswertung_text(state):
    """Gesamtauswertung: Ist die Strategie profitabel? Wird bei jedem Lauf neu geschrieben."""
    alle = state["positionen"]
    for p in alle:
        stelle_b_sicher(p)
        stelle_c_sicher(p)
        stelle_d_sicher(p)
    n = len(alle)
    z = ["# Coin-Scanner – Auswertung", "",
         f"_Stand: {jetzt().strftime('%Y-%m-%d %H:%M')} UTC. Paper Trading, kein echtes Geld, "
         f"Werte inkl. {GEBUEHR_PCT:.0f} % Kosten pro Kauf und Verkauf._", ""]
    if not n:
        return "\n".join(z + ["Noch keine Coins gekauft."])

    start = min(p["gekauft"] for p in alle)
    tage = (jetzt() - datetime.fromisoformat(start)).total_seconds() / 86400
    e, wa, ga = ergebnis(alle, pos_wert)
    _, wb, gb = ergebnis(alle, pos_wert_b)
    _, wc, gc = ergebnis(alle, pos_wert_c)
    a_offen = sum(1 for p in alle if p["status"] == "offen")
    a_tot = sum(1 for p in alle if p["status"] == "tot")
    a_verk = sum(1 for p in alle if p["status"] == "verkauft")
    b_offen = sum(1 for p in alle if p["b"]["status"] == "offen")

    z += ["## Ergebnis", "",
          f"- Läuft seit **{tage:.1f} Tagen**, **{n} Coins** gekauft (Einsatz {fr(e)})",
          f"- Status Regel A: {a_verk} bei 4x verkauft, {a_tot} tot, {a_offen} noch offen",
          f"- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).", "",
          "| Regel | Wert heute | Ergebnis | Rendite |", "|---|---|---|---|",
          f"| A: alles bei 4x | {fr(wa)} | **{vz(ga)}** | {prozent(ga, e)} |",
          f"| B: Hälfte bei 4x, Rest läuft | {fr(wb)} | **{vz(gb)}** | {prozent(gb, e)} |",
          f"| C: Einsatz bei 2x raus, Rest ohne Stop | {fr(wc)} | **{vz(gc)}** | {prozent(gc, e)} |", ""]
    rw = sum(1 for p in alle if p["c"].get("rueckwirkend"))
    z += ["### Regel D: Verluste begrenzen, Gewinner laufen lassen", "",
          f"_Stop bei {D_STOP_X}x, nach {D_ZEIT_STOP_H} h raus wenn unter Einstieg, bei {D_AUSLOESER_X:.0f}x "
          f"Einsatz zurück, Rest ohne Deckel, Trailing-Stop {D_TRAILING * 100:.0f} % ab {D_TRAIL_AB_X:.0f}x. "
          "Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._", "",
          *d_vergleich(alle), ""]
    dg = [p for p in mit_d(alle) if p["d"]["status"] != "offen"]
    if dg:
        gruende = {}
        for p in dg:
            k = "tot" if p["d"]["status"] == "tot" else p["d"].get("grund", "").split(" ")[0]
            gruende[k] = gruende.get(k, 0) + 1
        z += ["D abgeschlossen: " + ", ".join(f"{k} {v}x" for k, v in sorted(gruende.items())), ""]
    if rw:
        z += [f"_Regel C gibt es seit 7.11.2026. Bei {rw} älteren Coins ist C rückwirkend aus dem "
              "Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._", ""]
    korr = [p for p in alle if p.get("korrigiert")]
    for p in korr:
        z += [f"_Korrigiert: {p['korrigiert']}. Position neu ab Einstieg bewertet._", ""]

    # nur abgeschlossene Coins (ohne offene) -> ehrlicher Blick
    zu = [p for p in alle if p["status"] != "offen"]
    if zu:
        ez, _, gz = ergebnis(zu, pos_wert)
        z += [f"Nur abgeschlossene Coins (Regel A, ohne offene): {len(zu)} Coins, "
              f"**{vz(gz)}** ({prozent(gz, ez)})", ""]

    # Trefferquoten
    def anteil(x):
        k = sum(1 for p in alle if p.get("hoechst_x", 1.0) >= x)
        return f"{k} von {n} ({k / n * 100:.0f} %)"

    z += ["## Wie oft steigt ein Coin?", "",
          f"- Mindestens 2x erreicht: {anteil(2)}",
          f"- Mindestens 4x erreicht: {anteil(4)}",
          f"- Mindestens 10x erreicht: {anteil(10)}",
          f"- Auf -95 % oder Liquidität weg (tot): {a_tot} von {n} ({a_tot / n * 100:.0f} %)", ""]

    # Zielvergleich
    z += ["## Was wäre bei anderen Verkaufszielen gewesen?", "",
          "_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, "
          "alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum "
          "tatsächlich beobachteten Kurs verkauft._", "",
          "| Verkaufsziel | Ergebnis | Rendite |", "|---|---|---|"]
    for ziel in ZIEL_VERGLEICH:
        _, _, gg = ergebnis(alle, lambda p, zx=ziel: pos_wert_ziel(p, zx))
        z.append(f"| alles bei {ziel}x | {vz(gg)} | {prozent(gg, e)} |")
    z.append("")

    # Abhängigkeit von Ausreissern
    sortiert = sorted(alle, key=pos_wert_b, reverse=True)
    top = sortiert[:5]
    flop = sortiert[-3:]
    gesamt_gewinn = sum(pos_wert_b(p) - EINSATZ_CHF for p in alle if pos_wert_b(p) > EINSATZ_CHF)
    z += ["## Beste und schlechteste Coins (Regel B)", "",
          "| Coin | Status | Wert B | Wert C | Max. erreicht |", "|---|---|---|---|---|"]
    for p in top + [q for q in flop if q not in top]:
        z.append(f"| [{p['symbol']}]({p.get('url', '')}) | A: {p['status']}, B: {p['b']['status']} | "
                 f"{fr(pos_wert_b(p))} | {fr(pos_wert_c(p))} | {p.get('hoechst_x', 1):.1f}x |")
    if gesamt_gewinn > 0 and sortiert:
        bester = pos_wert_b(sortiert[0]) - EINSATZ_CHF
        z += ["", f"Der beste Coin macht {bester / gesamt_gewinn * 100:.0f} % aller Gewinne aus "
                  "(hoher Wert = Ergebnis hängt an einem einzigen Treffer)."]
    z.append("")

    # Aussagekraft
    if n < 30:
        urteil = "**Zu wenige Coins für ein Urteil.** Unter 30 Coins entscheidet der Zufall."
    elif n < 100:
        urteil = "Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen."
    else:
        urteil = "Genug Coins für eine brauchbare Einschätzung (kein Beweis)."
    z += ["## Aussagekraft", "", urteil,
          "Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks "
          "würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins "
          "können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.", ""]

    # Schlagwörter
    log = state.get("schlagwort_log") or {}
    if log:
        z += ["## Coins mit Schlagwörtern (" + ", ".join(SCHLAGWORTE) + ")", "",
              "| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |",
              "|---|---|---|---|---|"]
        for m, e2 in sorted(log.items(), key=lambda kv: kv[1].get("zuerst_gesehen", ""), reverse=True)[:40]:
            z.append(f"| [{e2['symbol']}]({e2.get('url', '')}) {e2['name']} | {e2.get('entscheid', '')} | "
                     f"{e2.get('liquiditaet_usd', 0):,} $ | {e2.get('mcap_usd', 0):,} $ | "
                     f"{e2.get('zuerst_gesehen', '')[:10]} |".replace(",", "'"))
        z.append("")
    else:
        z += ["## Coins mit Schlagwörtern", "",
              f"Bisher kein Coin mit {', '.join(SCHLAGWORTE)} im Namen im Beobachtungsfeld gesehen.", ""]
    return "\n".join(z)


def schreibe_auswertung(state):
    pfad = STATE_FILE.parent / "auswertung.md"
    pfad.write_text(auswertung_text(state), encoding="utf-8")


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
def checkpoint(state):
    """Sichert den Stand zwischendurch ins Repo, damit bei einem Fehler nicht eine ganze Stunde fehlt."""
    if not os.getenv("GITHUB_ACTIONS"):
        return
    schreibe_auswertung(state)
    befehl = ("git add data && (git diff --cached --quiet || git commit -qm 'Scanner-Zwischenstand') "
              "&& (git pull -q --rebase -X theirs origin main || (git rebase --abort; false)) && git push -q")
    try:
        subprocess.run(befehl, shell=True, check=True, timeout=120, cwd=Path(__file__).parent)
        print("  (Zwischenstand gesichert)")
    except Exception as e:  # nicht schlimm, der Abschluss-Schritt versucht es nochmal
        print(f"  ! Zwischenstand nicht gesichert: {e!r}")


def lauf_einmal(state, scan):
    print("== Positionen aktualisieren")
    update_positionen(state)
    if scan:
        print("== Neue Coins scannen")
        scanne(state)


def main():
    state = lade_state()
    if "--auswertung" in sys.argv:  # nur anzeigen, nichts verändern
        print(auswertung_text(state))
        return
    if "--bilanz" in sys.argv:
        monat = jetzt().strftime("%Y-%m")
        sende(f"🪙 Coin-Scanner Zwischenstand {monat}", bilanz_text(state, monat))
    else:
        monat = monatsbilanz_faellig(state)
        if monat:
            sende(f"🪙 Coin-Scanner Monatsbilanz {monat}", bilanz_text(state, monat))
        # Dauerlauf: so viele Minuten lang laufen lassen (0 = nur ein Durchgang)
        dauer_s = float(os.getenv("SCAN_DAUER_MIN", "0") or 0) * 60
        start = time.time()
        if os.getenv("GITHUB_EVENT_NAME") == "schedule":
            # Spätestens um hh:03 UTC aufhören, auch wenn GitHub den Lauf verspätet gestartet hat.
            # So überlappt er nie mit dem nächsten Lauf (Start hh:07) -> keine wartenden/abgebrochenen Läufe.
            n = jetzt()
            bis = n.replace(minute=3, second=0, microsecond=0)
            if bis <= n:
                bis = datetime.fromtimestamp(bis.timestamp() + 3600, timezone.utc)
            dauer_s = min(dauer_s, max(60.0, (bis - n).total_seconds()))
            print(f"Dauerlauf bis {bis:%H:%M} UTC ({dauer_s / 60:.0f} Min.)")
        letzter_scan = 0.0
        letzter_check = time.time()
        while True:
            takt = time.time()
            scan = takt - letzter_scan >= SCAN_INTERVALL_MIN * 60
            try:
                lauf_einmal(state, scan)
                if scan:
                    letzter_scan = takt
            except Exception as e:  # ein Fehler darf den Dauerlauf nicht beenden
                print(f"  ! Fehler im Durchgang: {e!r}")
            speichere_state(state)
            if time.time() - letzter_check >= CHECKPOINT_MIN * 60:
                checkpoint(state)
                letzter_check = time.time()
            if time.time() - start + CHECK_INTERVALL_S >= dauer_s:
                break
            time.sleep(max(1.0, CHECK_INTERVALL_S - (time.time() - takt)))
    speichere_state(state)
    schreibe_auswertung(state)
    offen = sum(1 for p in state["positionen"] if p["status"] == "offen")
    print(f"Fertig. {len(state['positionen'])} Positionen total, {offen} offen.")


if __name__ == "__main__":
    main()
