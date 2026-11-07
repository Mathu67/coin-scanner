"""
Regel-D-Varianten auf den echten Kursverläufen nachrechnen (data/verlauf/<mint>.csv).

    python backtest.py

Die Verläufe gibt es erst für Coins ab dem 7.11.2026. Unter ~100 Coins ist jedes Ergebnis nur
eine Tendenz, und wer viele Varianten testet, findet immer eine, die zufällig gut aussah.
"""
import csv
import itertools
import json
from datetime import datetime
from pathlib import Path

import scanner as S

DATA = Path(__file__).parent / "data"
F = 1 - S.GEBUEHR_PCT / 100


def lade_verlaeufe():
    state = json.loads((DATA / "state.json").read_text(encoding="utf-8"))
    out = []
    for pos in state["positionen"]:
        pfad = DATA / "verlauf" / f"{pos['mint']}.csv"
        if not pfad.exists():
            continue
        with pfad.open(encoding="utf-8") as f:
            reihe = [(datetime.fromisoformat(r["zeit"]), float(r["x"]), float(r["liq_usd"]))
                     for r in csv.DictReader(f)]
        if reihe:
            start = datetime.fromisoformat(pos["gekauft"][:19])
            out.append((pos["symbol"], start, reihe, pos["status"] == "offen"))
    return out


def simuliere(reihe, start, stop_x, zeit_h, ausloeser_x, trail_ab_x, trailing):
    """Wert einer Position (10 Fr. Einsatz) nach den Regeln; offene Enden zum letzten Kurs."""
    e = S.EINSATZ_CHF
    teil, anteil, erloes, spitze = False, 0.0, 0.0, 1.0
    x = 1.0
    for zeit, x, liq in reihe:
        spitze = max(spitze, x)
        if not teil and x >= ausloeser_x:
            voll = e * F * x * F
            anteil = min(1.0, e / voll)
            erloes, teil = voll * anteil, True
        if teil:
            if spitze >= trail_ab_x and x <= spitze * trailing:
                return erloes + e * (1 - anteil) * F * x * F
            if liq < S.TOT_LIQ_USD or x <= S.TOT_WERT_ANTEIL:
                return erloes + e * (1 - anteil) * F * x * F
        else:
            alter_h = (zeit - start).total_seconds() / 3600
            if liq < S.TOT_LIQ_USD or x <= stop_x or (alter_h >= zeit_h and x < 1.0):
                return e * F * x * F
    return erloes + e * (1 - anteil) * F * x * F


def main():
    v = lade_verlaeufe()
    if not v:
        print("Noch keine Kursverläufe in data/verlauf/.")
        return
    print(f"{len(v)} Coins mit Verlauf ({sum(o for *_, o in v)} noch offen, zum letzten Kurs bewertet)\n")
    gitter = itertools.product([0.5, 0.6, 0.7, 0.0], [24, 48, 1e9], [2.0, 3.0], [3.0, 5.0, 1e9], [0.5])
    zeilen = []
    for stop, zeit, ausl, trail_ab, trail in gitter:
        w = sum(simuliere(r, s, stop, zeit, ausl, trail_ab, trail) for _, s, r, _ in v)
        zeilen.append((w - len(v) * S.EINSATZ_CHF, stop, zeit, ausl, trail_ab))
    print("Gewinn Fr. | Stop | Zeit-Stop | Einsatz zurück bei | Trailing ab")
    for g, stop, zeit, ausl, trail_ab in sorted(zeilen, reverse=True):
        print(f"{g:+10.2f} | {stop or '-':>4} | {'-' if zeit > 1e8 else f'{zeit:.0f} h':>9} | "
              f"{ausl:.0f}x{'':16} | {'-' if trail_ab > 1e8 else f'{trail_ab:.0f}x'}")
    print("\nAktuelle Regel D: Stop 0.6, Zeit-Stop 48 h, Einsatz bei 2x, Trailing ab 5x.")


if __name__ == "__main__":
    main()
