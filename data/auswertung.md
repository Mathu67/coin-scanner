# Coin-Scanner – Auswertung

_Stand: 2026-11-07 16:56 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **4.3 Tagen**, **62 Coins** gekauft (Einsatz 620.00 Fr.)
- Status Regel A: 2 bei 4x verkauft, 17 tot, 43 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 389.71 Fr. | **-230.29 Fr.** | -37 % |
| B: Hälfte bei 4x, Rest läuft | 481.48 Fr. | **-138.52 Fr.** | -22 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 486.59 Fr. | **-133.41 Fr.** | -22 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **12 Coins seit Start von Regel D** (Einsatz 120.00 Fr.):
  - A: **-27.28 Fr.** (-23 %)
  - B: **-27.28 Fr.** (-23 %)
  - C: **-28.85 Fr.** (-24 %)
  - D: **-28.37 Fr.** (-24 %)

D abgeschlossen: Stop-Loss 5x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 19 Coins, **-106.28 Fr.** (-56 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 10 von 62 (16 %)
- Mindestens 4x erreicht: 2 von 62 (3 %)
- Mindestens 10x erreicht: 1 von 62 (2 %)
- Auf -95 % oder Liquidität weg (tot): 17 von 62 (27 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -203.53 Fr. | -33 % |
| alles bei 3x | -244.89 Fr. | -39 % |
| alles bei 4x | -236.83 Fr. | -38 % |
| alles bei 5x | -218.39 Fr. | -35 % |
| alles bei 10x | -143.94 Fr. | -23 % |
| alles bei 20x | -51.78 Fr. | -8 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: offen | 55.66 Fr. | 44.06 Fr. | 8.6x |
| [0DAY](https://dexscreener.com/solana/6qlmg6pz7esjvz3i7mp4arqknlkdy4ncanzsu8nnnofa) | A: offen, B: offen | 23.01 Fr. | 21.44 Fr. | 2.5x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: offen, B: offen | 17.72 Fr. | 18.11 Fr. | 2.8x |
| [TrumpWars](https://dexscreener.com/solana/7ppuyh3b5f61zc6jcfjaftwthkwne1jgwhpddanlh8eo) | A: offen, B: offen | 17.28 Fr. | 17.91 Fr. | 3.7x |
| [AI](https://dexscreener.com/solana/j7zf2zipjlfctwtqxstq1ulaarxn3ljxhpiipkavexpp) | A: tot, B: tot | 0.03 Fr. | 0.03 Fr. | 1.0x |
| [AMD](https://dexscreener.com/solana/e9wpfxjqvwvdjkculu2xs742t6ehbn2cnzv2ps24fz14) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 56 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: zu jung | 0 $ | 2'506 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/2hmk1t2s972sl7tmbugr8uh67txctefy5s74j6oaacv4) GTA6 | Markt-Filter: Liquidität 1651$ | 1'651 $ | 1'614 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/4l7yip761fgodtciqvdcbsbqy2jjts2uu6w8a6rhqbxw) Jason Duval  | Markt-Filter: Liquidität 0$ | 0 $ | 2'514 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/cecxwx7qqt6jp4qa956vzpqyuhuqkmbvgsptxenxrcc9) GTA6 | Markt-Filter: Liquidität 1714$ | 1'714 $ | 1'644 $ | 2026-11-07 |
| [GTA6FLAM](https://dexscreener.com/solana/9q8scnfw3zcph1v33emxent1jvaccnw2rvo9d5r4dk63) GTA6Flamingo | Markt-Filter: Liquidität 0$ | 0 $ | 2'515 $ | 2026-11-07 |
| [GTA6DOG](https://dexscreener.com/solana/6d18zgikseb8qkrjadtlltv3ssgxiwhb7njstmjm1kut) GTA6Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'520 $ | 2026-11-07 |
| [MTA6](https://dexscreener.com/solana/fgfdumvdcglkcq4zeq11sgqhklbv3ew8pwybx1mum4ys) Monke GTA6 | Markt-Filter: Liquidität 1913$ | 1'913 $ | 1'772 $ | 2026-11-07 |
| [solana](https://dexscreener.com/solana/h71ihsvdcdoab21yxedbb4xddhqrivp6xzpq9doycchb) LUCIA GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 2'524 $ | 2026-11-07 |
| [GTAmid](https://dexscreener.com/solana/ajzgg3thcspk857xvjerzmwn5saptqyhyh6vb6ijqfkt) GTAmid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [ATM](https://dexscreener.com/solana/1ukbur4jm7vbzfa6anncn9gr2hkactfbl9yae7543xz) GTA6ATM | Markt-Filter: Liquidität 2320$ | 2'320 $ | 2'126 $ | 2026-11-07 |
| [ROCCO](https://dexscreener.com/solana/eenwnbco7lyuysb8r8omaqutz85jc52eizxmfcfzwko7) GTA6 DOGE | Markt-Filter: Liquidität 1791$ | 1'791 $ | 1'688 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/bwfwgjeu3nitww44w2caeocvzqdybxhjhdnmkbgefg71) Grand Theft Airlines | Markt-Filter: Liquidität 2678$ | 2'678 $ | 2'666 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/66litxo66tc7g8kyg52c5kyqnulosrul6qod4dcxczvt) Grand Theft Airlines | Markt-Filter: Liquidität 1794$ | 1'794 $ | 1'678 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/ee7tn5dh18dwgpe9ste5g2dxeh6h63sb5yyckjfkyazb) Grand Theft Animal 6 | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA6K9](https://dexscreener.com/solana/bodz7ruysgf65hhz2aypprdtxik9onerskwhplhrb4xx) GTA6DOG | Sicherheits-Filter: Top-10 halten 56% | 27'742 $ | 129'074 $ | 2026-11-07 |
| [Claude](https://dexscreener.com/solana/9ug8i5hzyctcjugpbvjvegb1duuwdkipaumshuqexhhc) Be Nice To Claude | Markt-Filter: Liquidität 1684$ | 1'684 $ | 1'625 $ | 2026-11-07 |
| [CHOP](https://dexscreener.com/solana/d6mch8n2sxvdctlssrvoss46iwqvneiakbstkqusc2h) GTA Chop | Markt-Filter: zu alt | 37'429 $ | 205'430 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/4xbsv7yftzzeaxdjk77sgteas1mehwbb73ghuwhvj8sg) Giga Titty Ass | Markt-Filter: Liquidität 1781$ | 1'781 $ | 1'674 $ | 2026-11-07 |
| [RICO](https://dexscreener.com/solana/8mzdl9h38zzyalwfkprtapp9kyroxqw2x8etsd5981ya) GTA6DOG | Markt-Filter: Liquidität 0$ | 0 $ | 2'626 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/coburtyqxtw3j3fbu6lkz8pftw1pkuk2qjd1fgjju9ae) Giga Titty Ass | Markt-Filter: Liquidität 1728$ | 1'728 $ | 1'647 $ | 2026-11-07 |
| [GTM](https://dexscreener.com/solana/gro4fjwsbkcbzhqlekfhsofxrsxoawowqyqe5ncqaw8e) Grand Theft Mini Woke City | Markt-Filter: Liquidität 0$ | 0 $ | 2'525 $ | 2026-11-07 |
| [INVEST](https://dexscreener.com/solana/j1z33dbp71pkjwv7p5fmitoegpcdj8d6f8lfmr5nxwgm) Claude Invest | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/5r5rcy8jfrrgmnzguxihso45jgw2zkz2kpvms1kvkvsd) Grand Tits of America | Markt-Filter: Liquidität 1759$ | 1'759 $ | 1'682 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/7m44bf1ekzq1e4vgbdprlg7qgkz3q5ywts9ysgdehjs4) Grand Theft Auto VI | Markt-Filter: Liquidität 7648$ | 7'648 $ | 10'277 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/94yvmuoerf6m9c2kin81bnumnztzjlaamewvpc58cahf) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 3'081 $ | 2026-11-07 |
| [Flower](https://dexscreener.com/solana/4ywqpvfxexrafavkdttjpq2d4qgbhx3nw2upayggrmwq) Claude Flower | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-06 |
| [AGTA](https://dexscreener.com/solana/6zcsr1bkk1va2utmy2elxvuw2ef8xurwxuyscz9anbye) gta6 anime | Markt-Filter: Liquidität 0$ | 0 $ | 2'507 $ | 2026-11-06 |
| [GTA 6 Coin](https://dexscreener.com/solana/7dmjqdaiu9pcwcpcjxlrxnqbonjkpc92kzfyrx7tmk1e) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 3'058 $ | 2026-11-06 |
| [MAYHEM](https://dexscreener.com/solana/2tsgelokaeajvegvrrt5ezreya5pthy3x2wstcqc3nfk) GTA MONEY | Markt-Filter: Liquidität 0$ | 0 $ | 2'827 $ | 2026-11-06 |
| [GTA](https://dexscreener.com/solana/6qd5k4vkgpsgsm9x1dqxjtby5ng6zcdkisnvfpfgyps4) Grab That Ass | Markt-Filter: Liquidität 0$ | 0 $ | 482'299 $ | 2026-11-06 |
| [GTA6](https://dexscreener.com/solana/fbtjdtkp5xawwhc35ayxhmgh4apyjv2jfrr3cmufztf9) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'705 $ | 2026-11-06 |
| [GTA 6 Coin](https://dexscreener.com/solana/faxavxgap2rkfdbyhy4x2kv9wnlhhpwaud2hgmkfi239) GTA6 | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-06 |
| [GTA 6 Coin](https://dexscreener.com/solana/caci57bhzxvf9mjzv9f4bgay22ukramr5jvvt7cxbn4q) GTA6 | Markt-Filter: Liquidität 1642$ | 1'642 $ | 1'602 $ | 2026-11-06 |
| [RICO](https://dexscreener.com/solana/61ov7wc7uovzheashdj2kuhnwdejc1bj9eake1vys59y) GTA6DOG | Markt-Filter: Liquidität 0$ | 0 $ | 1'210'365 $ | 2026-11-06 |
| [$GTA6](https://dexscreener.com/solana/4hrshzpbjeujtmucgn4rxftu6kmzkf5jcnjassd3kbhv) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 1'707 $ | 2026-11-06 |
| [GTAVI](https://dexscreener.com/solana/je6dddzzbjxya2r7jumlvsvfeudvboqvamkxsam7oqmh) GTA Vice Inu | Markt-Filter: Liquidität 0$ | 0 $ | 2'667 $ | 2026-11-06 |
| [$Anthropic](https://dexscreener.com/solana/cgxraubyfwqvfbvaiqhf12ppswkq7ppp8ddiccqcqyym) Anthropic Ai | Markt-Filter: Liquidität 0$ | 0 $ | 2'705 $ | 2026-11-06 |
