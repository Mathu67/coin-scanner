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
Bei jedem Lauf entsteht `data/auswertung.md` (Regel A gegen B, Trefferquote, Zielvergleich).

Am 1. jedes Monats kommt die **Monatsbilanz** für alle Coins, die im Vormonat gekauft wurden.

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
