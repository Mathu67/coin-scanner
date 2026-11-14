# 🪙 Coin-Scanner (Paper Trading)

Durchsucht alle 5 Minuten neue Solana-Memecoins und prüft offene Positionen alle 60 Sekunden. Durchsucht neue Solana-Memecoins (die gleichen, die du in Fomo siehst), filtert offensichtliche Rug Pulls raus und "kauft" jeden Treffer **simuliert** für 10 Fr. Es wird kein echtes Geld bewegt.

## Regeln

**Kaufen**, wenn alles zutrifft:
- Coin ist 6–72 Stunden alt
- Liquidität ≥ 25'000 $, Market Cap 100'000 $ – 20 Mio. $
- Volumen 24h ≥ 50'000 $, mindestens 150 Käufe und 75 Verkäufe (Verkaufen funktioniert also)
- Mint und Freeze Authority entzogen (Ersteller kann keine Coins drucken oder einfrieren)
- Liquidität zu ≥ 90 % gesperrt oder verbrannt
- Top-10-Wallets halten zusammen ≤ 25 %, kein Einzel-Wallet > 8 %, Insider ≤ 10 %, Ersteller ≤ 5 %
- RugCheck meldet kein "danger"-Risiko
- Höchstens 10 Käufe pro Tag

**Verkaufen** bei +300 % (4x).
**Abschreiben**, wenn der Coin tot ist: −95 % oder mehr, Liquidität unter 1'000 $ oder 1 Tag lang nicht auffindbar.
Pro Kauf und Verkauf werden je 4 % Gebühren/Slippage abgezogen (realistisch für Memecoins).
Zusätzlich läuft Regel B mit: bei 4x die Hälfte verkaufen, den Rest bis 20x oder bis der Kurs auf 50 % der Spitze fällt.
Regel C: bei 2x so viel verkaufen, dass der Einsatz zurück ist; der Rest läuft ohne Stop bis 20x oder bis er tot ist.
Kaputte Preise (Sprung über 20x in einer Minute ohne Bestätigung, oder MCap über 1 Mrd. $) werden ignoriert.
Bei jedem Lauf entsteht `data/auswertung.md` (Regel A, B und C, Trefferquote, Zielvergleich).

Am 1. jedes Monats kommt die **Monatsbilanz** für alle Coins, die im Vormonat gekauft wurden.

## 👥 Copy-Trader (Top-Fomo-Trader kopieren)

`copytrader.py` läuft im selben Workflow parallel zum Scanner. Er liest jede Minute die letzten
Trades der Trader in `data/copy/wallets.json` über die (inoffizielle) Fomo-Schnittstelle:
- Kauft ein Trader einen **neuen** Coin (mind. 20 $, Liquidität ≥ 5'000 $) → simulierter Kauf für 10 Fr. zum Kurs, den der Bot dann sieht (also etwas später als der Trader).
- Verkauft er einen Teil → gleicher Anteil wird verkauft. Unter 2 % seiner Menge → alles raus.
- 4 % Kosten pro Kauf und Verkauf. Tot wie beim Scanner (−95 %, Liquidität < 1'000 $, 24 h weg).
- Nur Solana-Trades. Coins, die er vor dem Start schon hatte, werden nicht kopiert.

Ergebnis: `data/copy/auswertung.md` (gesamt und pro Trader).

**Warum über Fomo und nicht die Blockchain?** Fomo handelt über eigene Sammel-Wallets. Die
Adressen in der App existieren auf Solana nicht (geprüft 14.11.2026, Solscan: 0 Transaktionen).

**Fomo-Login (einmalig, ca. 30 Tage gültig):** Fomo braucht einen Login. Der Bot erneuert ihn selbst,
braucht dafür aber zwei Secrets (Settings → Secrets and variables → Actions → New repository secret):
1. `FOMO_SCHLUESSEL`: irgendein langer Text (z. B. 30 zufällige Zeichen). Damit verschlüsselt der Bot
   den erneuerten Login in `data/copy/login.enc` (das Repo ist öffentlich).
2. `FOMO_REFRESH`: In Edge/Chrome ein **InPrivate-Fenster** öffnen (Ctrl+Shift+N), auf fomo.family
   einloggen, F12 → **Application/Anwendung** → **Cookies** → `https://fomo.family` → Zeile
   `privy-refresh-token` → Wert kopieren. Fenster danach einfach schliessen, **nicht ausloggen**.

⚠️ Wer diesen Wert hat, kommt in das Fomo-Konto. Nur verwenden, solange darauf kein Geld liegt.
Steht in der Auswertung „Fomo-Login fehlt oder ist abgelaufen“: Schritt 2 wiederholen.

**Trader-Liste erneuern:** Auf fomo.family einloggen, F12 → Console, `tools/fomo_top10.js` einfügen.
Nimmt die Top 10 der 30-Tage-Rangliste (mind. 20 Trades, handelt auf Solana) → in
`data/copy/wallets.json` einfügen.

## Einrichten

1. Repository **öffentlich** auf GitHub veröffentlichen (dann sind die Actions-Minuten unbegrenzt gratis).
2. Im Repo: **Settings → Actions → General → Workflow permissions → "Read and write permissions"** einschalten und speichern.
3. Im Tab **Actions** den Workflow "Coin-Scanner" aktivieren und einmal mit **Run workflow** starten.
4. Damit die Bilanz als E-Mail kommt: oben rechts im Repo auf **Watch → All Activity** stellen. Die Bilanz wird als Issue erstellt, und GitHub schickt dir jedes neue Issue per Mail.

Eine Zwischenbilanz bekommst du jederzeit über **Actions → Coin-Scanner → Run workflow → "Nur Zwischenbilanz" ✔**.

### Optional: direkt per Gmail statt über GitHub
Erstelle ein Google-App-Passwort (dafür muss die 2-Faktor-Anmeldung aktiv sein). Lege dann unter **Settings → Secrets and variables → Actions** diese Secrets an:
`SMTP_HOST` = `smtp.gmail.com`, `SMTP_USER` = deine Gmail-Adresse, `SMTP_PASS` = das App-Passwort.

## Einstellungen ändern
Alle Zahlen stehen ganz oben in `scanner.py` (Einsatz, Filter, Verkaufsregel).

## Wichtig
Die Filter sortieren **offensichtliche** Scams aus. Ob ein Coin steigt, können sie nicht vorhersagen, und raffinierte Rug Pulls kommen trotzdem durch. Genau das soll die Bilanz zeigen.
