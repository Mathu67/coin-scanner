"""
Copy-Trader (Paper Trading, kein echtes Geld)

Beobachtet die Trades der besten Fomo-Trader (Liste in data/copy/wallets.json) und
macht ihre Memecoin-Käufe simuliert nach:
  - Kauft ein Trader einen neuen Coin -> wir "kaufen" für 10 Fr. zum Kurs, den wir dann sehen.
  - Verkauft er einen Teil -> wir verkaufen denselben Anteil unserer Position.
  - Pro Kauf und Verkauf 4 % Kosten (wie beim Scanner).

Wie es funktioniert: Fomo handelt über eigene Sammel-Wallets, die Adressen in der App sind
auf der Blockchain nicht sichtbar (geprüft 14.11.2026). Darum liest der Bot jede Minute die
letzten Trades jedes Traders über die (inoffizielle) Fomo-Schnittstelle. Daraus führt er pro
Trader eine Menge pro Coin (nur Käufe ab Start). Mehr Coins = Kauf, weniger = Verkauf.

Login: Fomo verlangt einen Login. Nötig sind diese GitHub-Secrets:
  FOMO_REFRESH     Wert des Cookies "privy-refresh-token" (einmalig aus dem Browser kopiert)
  FOMO_SCHLUESSEL  beliebiger langer Text; damit wird ein erneuerter Login verschlüsselt
                   in data/copy/login.enc gespeichert (das Repo ist öffentlich!)
Der Bot holt sich damit jede Stunde selbst einen frischen Zugang (wie die App).
"""

import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------- Einstellungen
EINSATZ_CHF = 10.0
GEBUEHR_PCT = 4.0
CHECK_INTERVALL_S = 30       # alle 30 s alle Trader abfragen
TOP_N = 100                  # so viele Trader der 30-Tage-Rangliste beobachten
MIN_TRADES = 20              # Leute mit 1–2 Glückstreffern raus
LISTE_ERNEUERN_H = 24        # Rangliste einmal pro Tag neu holen
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
    "11111111111111111111111111111111",              # SOL (nativ)
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
LOGIN_FILE = BASIS / "login.enc"
RPC = os.getenv("SOLANA_RPC") or "https://api.mainnet-beta.solana.com"
FOMO_API = "https://prod-api.fomo.family"
FOMO_CHAINS = "1,56,143,4663,8453,1399811149"
SOLANA_ID = 1399811149
PRIVY_URL = "https://privy.fomo.family/api/v1/sessions"
PRIVY_HEADERS = {   # so wie die Fomo-Web-App (Privy react-auth) es selbst macht
    "privy-app-id": "cm6h485o300n3zj9yl6vpedq7",
    "privy-client-id": "client-WY5gFSayQjxnQhG4rP6SnwPAyPZWZpNRhJ6b9rzMnYwqH",
    "privy-client": "react-auth:3.48.0",
    "origin": "https://fomo.family",
    "referer": "https://fomo.family/",
    "content-type": "application/json",
    "accept": "application/json",
}
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
    trader = [w for w in daten.get("trader", []) if w.get("fomo_id") and w.get("aktiv", True)]
    for w in trader:
        w["wallet"] = w["fomo_id"]   # interner Schlüssel (alte Felder heissen noch "wallet")
    return trader


def lade_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"bestand": {}, "positionen": []}


def speichere_state(state):
    BASIS.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------- Fomo-Login
class FomoLogin:
    """Holt mit dem Refresh-Cookie jede Stunde einen frischen Zugang (Access-Token, 1 h gültig)."""

    def __init__(self):
        self.token = None
        self.exp = 0.0
        self.fehler = ""
        self.schluessel = (os.getenv("FOMO_SCHLUESSEL") or "").strip()
        kandidaten = [self._lade_gespeichert(), os.getenv("FOMO_REFRESH")]
        self.kandidaten = []
        for k in kandidaten:
            k = (k or "").strip().strip('"')
            if k and k not in self.kandidaten:
                self.kandidaten.append(k)

    def vorhanden(self):
        return bool(self.kandidaten)

    def _fernet(self):
        from cryptography.fernet import Fernet
        return Fernet(base64.urlsafe_b64encode(hashlib.sha256(self.schluessel.encode()).digest()))

    def _lade_gespeichert(self):
        if not self.schluessel or not LOGIN_FILE.exists():
            return None
        try:
            return self._fernet().decrypt(LOGIN_FILE.read_bytes()).decode()
        except Exception as e:
            print(f"  ! login.enc nicht lesbar ({e.__class__.__name__}), nehme Secret FOMO_REFRESH")
            return None

    def _speichere(self, refresh):
        if not self.schluessel:
            print("  ! Fomo hat den Login erneuert, aber FOMO_SCHLUESSEL fehlt -> kann ihn nicht sichern")
            return
        BASIS.mkdir(parents=True, exist_ok=True)
        LOGIN_FILE.write_bytes(self._fernet().encrypt(refresh.encode()))
        print("  Login erneuert und verschlüsselt gespeichert")
        if os.getenv("GITHUB_ACTIONS"):
            befehl = ("git add data/copy/login.enc && git commit -qm 'Copy-Trader: Login erneuert' "
                      "&& (git pull -q --rebase -X theirs origin main || (git rebase --abort; false)) && git push -q")
            try:
                subprocess.run(befehl, shell=True, check=True, timeout=120, cwd=Path(__file__).parent)
            except Exception as e:
                print(f"  ! login.enc nicht gepusht: {e!r}")

    def erneuern(self):
        for rt in list(self.kandidaten):
            try:
                r = requests.post(PRIVY_URL, headers={**HEADERS, **PRIVY_HEADERS},
                                  cookies={"privy-refresh-token": rt},
                                  json={"refresh_token": "deprecated"}, timeout=25)
                j = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
            except (requests.RequestException, ValueError) as e:
                self.fehler = f"Privy nicht erreichbar: {e}"
                continue
            if r.ok and j.get("token"):
                self.token = j["token"]
                try:
                    teil = self.token.split(".")[1]
                    self.exp = json.loads(base64.urlsafe_b64decode(teil + "=" * (-len(teil) % 4)))["exp"]
                except Exception:
                    self.exp = time.time() + 3000
                neu = r.cookies.get("privy-refresh-token")
                if not neu:
                    m = re.search(r"privy-refresh-token=([^;,\s]+)", r.headers.get("set-cookie", ""))
                    neu = m.group(1) if m else None
                if neu and neu != rt:
                    self._speichere(neu)
                    rt = neu
                self.kandidaten = [rt]
                self.fehler = ""
                return True
            self.fehler = f"Privy {r.status_code}: {j.get('error') or r.text[:120]}"
            print(f"  ! Login-Erneuerung fehlgeschlagen: {self.fehler}")
        return False

    def header(self):
        if not self.token or time.time() > self.exp - 300:
            self.erneuern()
        return {"authorization": f"Bearer {self.token}"} if self.token else {}


LOGIN = None


def fomo_get(pfad, tries=3):
    """GET auf die Fomo-Schnittstelle, gibt responseObject zurück oder None."""
    for i in range(tries):
        h = LOGIN.header() if LOGIN else {}
        if not h:
            return None
        try:
            r = requests.get(FOMO_API + pfad, timeout=25, headers={
                **HEADERS, **h, "x-supported-chains": FOMO_CHAINS,
                "origin": "https://fomo.family", "referer": "https://fomo.family/"})
            if r.status_code in (401, 403, 431):
                LOGIN.token = None   # Zugang abgelaufen -> beim nächsten Versuch erneuern
                continue
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(3 * (i + 1))
                continue
            r.raise_for_status()
            return r.json().get("responseObject")
        except (requests.RequestException, ValueError) as e:
            print(f"  ! Fomo {pfad}: {e}")
            time.sleep(2 * (i + 1))
    return None


# ---------------------------------------------------------------- Daten holen
def bestand(w, state):
    """{mint: Menge} der Coins, die der Trader seit Beobachtungsstart gekauft hat, oder None bei Fehler.

    Liest die letzten 25 Trades über Fomo und rechnet neue Trades in die Mengen ein.
    """
    fid = w["fomo_id"]
    ro = fomo_get(f"/v2/users/{fid}/swaps")
    if ro is None:
        return None
    swaps = ro.get("swaps") or []
    gesehen = state.setdefault("gesehen", {})
    menge = state.setdefault("menge", {}).setdefault(fid, {})
    if fid not in gesehen:
        gesehen[fid] = [s["id"] for s in swaps]   # Start: alte Trades nur merken
        return {}
    alte = set(gesehen[fid])
    neu = [s for s in swaps if s["id"] not in alte]
    if len(swaps) >= 25 and len(neu) == len(swaps):
        print(f"  ! {w['name']}: über 25 neue Trades in einer Minute, ältere fehlen")
    jetzt_ts = time.time()
    verz = state.setdefault("verzoegerung", [])
    for s in reversed(neu):   # älteste zuerst
        try:   # wie alt ist der Trade, wenn wir ihn sehen?
            alter = jetzt_ts - datetime.fromisoformat(s["createdAt"].replace("Z", "+00:00")).timestamp()
            if 0 <= alter < 3600:
                verz.append(round(alter, 1))
        except (KeyError, ValueError, AttributeError):
            pass
        if s.get("inNetworkId") != SOLANA_ID or s.get("outNetworkId") != SOLANA_ID:
            continue
        ein, aus = s.get("inTokenAddress"), s.get("outTokenAddress")
        if ein and ein not in BASIS_MINTS and ein in menge:      # Coin weggegeben = Verkauf
            menge[ein] = max(0.0, menge[ein] - float(s.get("inHumanAmount") or 0))
            if menge[ein] <= 0:
                del menge[ein]
        if aus and aus not in BASIS_MINTS:                        # Coin bekommen = Kauf
            menge[aus] = menge.get(aus, 0.0) + float(s.get("outHumanAmount") or 0)
    del verz[:-2000]
    gesehen[fid] = ([s["id"] for s in neu] + gesehen[fid])[:300]
    return dict(menge)


def aktualisiere_liste(state, wallets):
    """Top-N der 30-Tage-Rangliste holen (einmal pro Tag) und in wallets.json schreiben."""
    stand = state.get("liste_stand")
    if wallets and stand and (jetzt() - datetime.fromisoformat(stand)).total_seconds() < LISTE_ERNEUERN_H * 3600:
        return wallets
    roh, ids = [], set()
    for pfad in ["/v2/leaderboard/30d", "/v2/leaderboard/30d?limit=200", "/v2/leaderboard/30d?page=2",
                 "/v2/leaderboard/30d?offset=100", "/v2/leaderboard/30d?page=3"]:
        ro = fomo_get(pfad)
        liste = ro if isinstance(ro, list) else ((ro or {}).get("leaderboard")
                                                  or next((v for v in (ro or {}).values() if isinstance(v, list)), []))
        neu = [u for u in liste if u.get("id") and u["id"] not in ids]
        ids.update(u["id"] for u in neu)
        roh += neu
        print(f"  Rangliste {pfad}: {len(liste)} Einträge, {len(neu)} neu")
        if len(roh) >= TOP_N * 1.5:
            break
        time.sleep(0.5)
    gut = sorted([u for u in roh if not u.get("isRestricted") and (u.get("numTrades") or u.get("swapCount") or 0) >= MIN_TRADES],
                 key=lambda u: -(u.get("pnl30d") or 0))[:TOP_N]
    if not gut:
        print("  ! Rangliste nicht lesbar, behalte alte Liste")
        return wallets
    trader = [{"name": u.get("userHandle") or u.get("displayName") or u["id"][:8], "fomo_id": u["id"],
               "pnl30d_usd": round(u.get("pnl30d") or 0), "trades": u.get("numTrades") or u.get("swapCount")}
              for u in gut]
    BASIS.mkdir(parents=True, exist_ok=True)
    WALLETS_FILE.write_text(json.dumps({
        "hinweis": f"Top {TOP_N} der Fomo-Rangliste 30 Tage (mind. {MIN_TRADES} Trades), holt der Bot einmal pro Tag selbst. "
                   "'aktiv': false = nicht mehr kopieren.",
        "stand": jetzt().isoformat(timespec="seconds"), "trader": trader}, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8")
    state["liste_stand"] = jetzt().isoformat(timespec="seconds")
    print(f"  Rangliste erneuert: {len(trader)} Trader (von {len(roh)} geladen)")
    return lade_wallets()


def beobachtete(state, wallets):
    """Liste + Trader, die rausgefallen sind, aber noch offene Positionen haben (nur noch deren Verkäufe)."""
    ids = {w["fomo_id"] for w in wallets}
    extra = {}
    for p in offene(state):
        if p["wallet"] not in ids and p["wallet"] not in extra:
            extra[p["wallet"]] = {"name": p["trader"], "fomo_id": p["wallet"], "wallet": p["wallet"], "nur_verkauf": True}
    return wallets + list(extra.values())


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
        b = bestand(w, state)
        time.sleep(0.1)
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
            neu_gemerkt = state.setdefault("_neu_gemerkt", 0) + 1
            state["_neu_gemerkt"] = neu_gemerkt
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
        for mint, menge in (b.items() if not w.get("nur_verkauf") else []):
            if alt.get(mint, 0) > 0 or offene(state, trader=w["name"], mint=mint):
                continue
            p = paare.get(mint)
            if not p:
                continue
            preis, liq = preis_von(p)
            if not preis or liq < MIN_LIQ_USD or menge * preis < MIN_KAUF_USD:
                continue
            kaufe(state, w, mint, p, menge, preis, liq)

    if state.pop("_neu_gemerkt", 0):
        print("  Neue Trader: alte Trades gemerkt (werden nicht kopiert)")

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
        z.append("**Noch keine Trader eingetragen** (data/copy/wallets.json).\n")
    if LOGIN is not None and (not LOGIN.vorhanden() or LOGIN.fehler):
        z.append(f"**⚠️ Fomo-Login fehlt oder ist abgelaufen** ({LOGIN.fehler or 'Secret FOMO_REFRESH fehlt'}). "
                 "Neu holen: siehe README, Abschnitt Copy-Trader.\n")
    v = sorted(state.get("verzoegerung", []))
    if v:
        q = lambda f: v[min(len(v) - 1, int(len(v) * f))]
        z.append(f"**Verzögerung** (wie alt ein Trade ist, wenn der Bot ihn sieht; Abfrage alle {CHECK_INTERVALL_S} s): "
                 f"schnellster {v[0]:.0f} s, Median {q(0.5):.0f} s, 90 % unter {q(0.9):.0f} s ({len(v)} Trades gemessen). "
                 f"Liegt der schnellste weit über 0 s, braucht Fomo selbst so lange, dann bringt schnelleres Abfragen nichts.\n")
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
    if len(ps) > 1:
        bester = max(ps, key=pos_wert)
        w2 = wert - pos_wert(bester)
        e2 = einsatz - EINSATZ_CHF
        z.append(f"**Ohne den besten Coin** ({bester['name']}): {fr(w2 - e2)} ({(w2 / e2 - 1) * 100:+.1f} %). "
                 "Ist das deutlich schlechter, hängt alles an einem Glückstreffer.\n")
    if len(ps) < 30:
        z.append("_Unter 30 Käufen: noch kein Urteil möglich._\n")

    z.append("## Pro Trader\n\nSortiert nach Ergebnis. \"ohne Besten\" = Ergebnis ohne seinen besten Coin "
             "(aussagekräftig erst ab ca. 5 Käufen).\n\n"
             "| Trader | Käufe | offen | Einsatz | Wert | Ergebnis | ohne Besten | bester Coin |\n"
             "|---|---|---|---|---|---|---|---|")
    namen = sorted({p["trader"] for p in ps})
    zeilen = []
    for n in namen:
        tp = [p for p in ps if p["trader"] == n]
        e = len(tp) * EINSATZ_CHF
        v = sum(pos_wert(p) for p in tp)
        best = max(tp, key=pos_wert)
        ohne = f"{((v - pos_wert(best)) / (e - EINSATZ_CHF) - 1) * 100:+.0f} %" if len(tp) > 1 else "–"
        zeilen.append((v - e, f"| {n} | {len(tp)} | {sum(1 for p in tp if p['status'] == 'offen')} | "
                              f"{fr(e)} | {fr(v)} | {(v / e - 1) * 100:+.0f} % | {ohne} | "
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
    global LOGIN
    state = lade_state()
    wallets = lade_wallets()
    LOGIN = FomoLogin()
    if "--auswertung" in sys.argv:
        print(auswertung_text(state, wallets))
        return
    if not LOGIN.vorhanden() or not LOGIN.erneuern():
        print(f"Kein gültiger Fomo-Login: {LOGIN.fehler or 'Secret FOMO_REFRESH fehlt'} – nichts zu tun.")
        schreibe_auswertung(state, wallets)
        return
    wallets = aktualisiere_liste(state, wallets)
    if not wallets:
        print("Keine Trader (Rangliste nicht lesbar, wallets.json leer) – nichts zu tun.")
        schreibe_auswertung(state, wallets)
        return
    print(f"Fomo-Login ok. Beobachte {len(wallets)} Trader (+ Verkäufe von Rausgefallenen mit offenen Positionen)")

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
            wallets = aktualisiere_liste(state, wallets)
            durchgang(state, beobachtete(state, wallets))
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
