# Coin-Scanner – Auswertung

_Stand: 2026-11-08 02:36 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **4.7 Tagen**, **68 Coins** gekauft (Einsatz 680.00 Fr.)
- Status Regel A: 3 bei 4x verkauft, 20 tot, 45 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 445.34 Fr. | **-234.66 Fr.** | -35 % |
| B: Hälfte bei 4x, Rest läuft | 516.55 Fr. | **-163.45 Fr.** | -24 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 538.46 Fr. | **-141.54 Fr.** | -21 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **18 Coins seit Start von Regel D** (Einsatz 180.00 Fr.):
  - A: **-12.18 Fr.** (-7 %)
  - B: **-10.63 Fr.** (-6 %)
  - C: **-15.25 Fr.** (-8 %)
  - D: **-37.83 Fr.** (-21 %)

D abgeschlossen: Stop-Loss 9x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 23 Coins, **-105.91 Fr.** (-46 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 13 von 68 (19 %)
- Mindestens 4x erreicht: 3 von 68 (4 %)
- Mindestens 10x erreicht: 2 von 68 (3 %)
- Auf -95 % oder Liquidität weg (tot): 20 von 68 (29 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -219.34 Fr. | -32 % |
| alles bei 3x | -248.33 Fr. | -37 % |
| alles bei 4x | -243.41 Fr. | -36 % |
| alles bei 5x | -215.76 Fr. | -32 % |
| alles bei 10x | -114.29 Fr. | -17 % |
| alles bei 20x | -75.57 Fr. | -11 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 36.86 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 35.34 Fr. | 9.9x |
| [0DAY](https://dexscreener.com/solana/6qlmg6pz7esjvz3i7mp4arqknlkdy4ncanzsu8nnnofa) | A: offen, B: offen | 27.88 Fr. | 23.86 Fr. | 3.4x |
| [WHITE](https://dexscreener.com/solana/gxx1ttdg4qw62pvvgicj1xgdztbay1yw6ah4rqagb8z4) | A: offen, B: offen | 22.66 Fr. | 21.83 Fr. | 3.0x |
| [AI](https://dexscreener.com/solana/j7zf2zipjlfctwtqxstq1ulaarxn3ljxhpiipkavexpp) | A: tot, B: tot | 0.03 Fr. | 0.03 Fr. | 1.0x |
| [AMD](https://dexscreener.com/solana/e9wpfxjqvwvdjkculu2xs742t6ehbn2cnzv2ps24fz14) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 49 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: zu jung | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: zu jung | 1'726 $ | 1'646 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/9tyhyxseygouvuj66vcjkr4bppi65h2muamuveuyy9wm) GTA VI | Markt-Filter: zu jung | 49'603 $ | 52'685 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/5afbwvsqpjf4cgejq4tajzyypyuvyktrrn3sahnrpnmv) GTA VI | Markt-Filter: zu alt | 114'063 $ | 12'738'260 $ | 2026-11-07 |
| [GTA6COP](https://dexscreener.com/solana/9sebidesbustw8xbbaczb6ab2ty72p6xp51mftpuwhp6) GTA6 Mendez | Markt-Filter: Liquidität 17077$ | 17'077 $ | 52'942 $ | 2026-11-07 |
| [CLAUDEPAID](https://dexscreener.com/solana/7tx6tl3e14nvhqgk4mfp3wdebmwp3rezsqgflxmrunuy) ClaudePaid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [$GTA6](https://dexscreener.com/solana/fytgbkzjhhcsymys7zbfu5ibxkrmwv8frvswvtdmoekz) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 242 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: Liquidität 0$ | 0 $ | 2'506 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/2hmk1t2s972sl7tmbugr8uh67txctefy5s74j6oaacv4) GTA6 | Markt-Filter: Liquidität 1651$ | 1'651 $ | 1'614 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/4l7yip761fgodtciqvdcbsbqy2jjts2uu6w8a6rhqbxw) Jason Duval  | Markt-Filter: Liquidität 0$ | 0 $ | 2'514 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/cecxwx7qqt6jp4qa956vzpqyuhuqkmbvgsptxenxrcc9) GTA6 | Markt-Filter: Liquidität 1737$ | 1'737 $ | 1'667 $ | 2026-11-07 |
| [GTA6FLAM](https://dexscreener.com/solana/9q8scnfw3zcph1v33emxent1jvaccnw2rvo9d5r4dk63) GTA6Flamingo | Markt-Filter: Liquidität 0$ | 0 $ | 2'492 $ | 2026-11-07 |
| [GTA6DOG](https://dexscreener.com/solana/6d18zgikseb8qkrjadtlltv3ssgxiwhb7njstmjm1kut) GTA6Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'520 $ | 2026-11-07 |
| [MTA6](https://dexscreener.com/solana/fgfdumvdcglkcq4zeq11sgqhklbv3ew8pwybx1mum4ys) Monke GTA6 | Markt-Filter: Liquidität 1913$ | 1'913 $ | 1'771 $ | 2026-11-07 |
| [solana](https://dexscreener.com/solana/h71ihsvdcdoab21yxedbb4xddhqrivp6xzpq9doycchb) LUCIA GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 2'524 $ | 2026-11-07 |
| [GTAmid](https://dexscreener.com/solana/ajzgg3thcspk857xvjerzmwn5saptqyhyh6vb6ijqfkt) GTAmid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [ATM](https://dexscreener.com/solana/1ukbur4jm7vbzfa6anncn9gr2hkactfbl9yae7543xz) GTA6ATM | Markt-Filter: Liquidität 2302$ | 2'302 $ | 2'108 $ | 2026-11-07 |
| [ROCCO](https://dexscreener.com/solana/eenwnbco7lyuysb8r8omaqutz85jc52eizxmfcfzwko7) GTA6 DOGE | Markt-Filter: Liquidität 1791$ | 1'791 $ | 1'688 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/bwfwgjeu3nitww44w2caeocvzqdybxhjhdnmkbgefg71) Grand Theft Airlines | Markt-Filter: Liquidität 2505$ | 2'505 $ | 2'456 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/66litxo66tc7g8kyg52c5kyqnulosrul6qod4dcxczvt) Grand Theft Airlines | Markt-Filter: Liquidität 1794$ | 1'794 $ | 1'678 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/ee7tn5dh18dwgpe9ste5g2dxeh6h63sb5yyckjfkyazb) Grand Theft Animal 6 | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA6K9](https://dexscreener.com/solana/bodz7ruysgf65hhz2aypprdtxik9onerskwhplhrb4xx) GTA6DOG | Sicherheits-Filter: Top-10 halten 56% | 27'742 $ | 129'074 $ | 2026-11-07 |
| [Claude](https://dexscreener.com/solana/9ug8i5hzyctcjugpbvjvegb1duuwdkipaumshuqexhhc) Be Nice To Claude | Markt-Filter: Liquidität 1684$ | 1'684 $ | 1'625 $ | 2026-11-07 |
| [CHOP](https://dexscreener.com/solana/d6mch8n2sxvdctlssrvoss46iwqvneiakbstkqusc2h) GTA Chop | Markt-Filter: zu alt | 37'429 $ | 205'430 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/4xbsv7yftzzeaxdjk77sgteas1mehwbb73ghuwhvj8sg) Giga Titty Ass | Markt-Filter: Liquidität 1763$ | 1'763 $ | 1'657 $ | 2026-11-07 |
| [RICO](https://dexscreener.com/solana/8mzdl9h38zzyalwfkprtapp9kyroxqw2x8etsd5981ya) GTA6DOG | Markt-Filter: Liquidität 0$ | 0 $ | 2'591 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/coburtyqxtw3j3fbu6lkz8pftw1pkuk2qjd1fgjju9ae) Giga Titty Ass | Markt-Filter: Liquidität 1725$ | 1'725 $ | 1'644 $ | 2026-11-07 |
| [GTM](https://dexscreener.com/solana/gro4fjwsbkcbzhqlekfhsofxrsxoawowqyqe5ncqaw8e) Grand Theft Mini Woke City | Markt-Filter: Liquidität 0$ | 0 $ | 2'507 $ | 2026-11-07 |
| [INVEST](https://dexscreener.com/solana/j1z33dbp71pkjwv7p5fmitoegpcdj8d6f8lfmr5nxwgm) Claude Invest | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/5r5rcy8jfrrgmnzguxihso45jgw2zkz2kpvms1kvkvsd) Grand Tits of America | Markt-Filter: Liquidität 1751$ | 1'751 $ | 1'675 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/7m44bf1ekzq1e4vgbdprlg7qgkz3q5ywts9ysgdehjs4) Grand Theft Auto VI | Markt-Filter: Liquidität 6653$ | 6'653 $ | 8'262 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/94yvmuoerf6m9c2kin81bnumnztzjlaamewvpc58cahf) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 3'081 $ | 2026-11-07 |
| [Flower](https://dexscreener.com/solana/4ywqpvfxexrafavkdttjpq2d4qgbhx3nw2upayggrmwq) Claude Flower | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-06 |
| [AGTA](https://dexscreener.com/solana/6zcsr1bkk1va2utmy2elxvuw2ef8xurwxuyscz9anbye) gta6 anime | Markt-Filter: Liquidität 0$ | 0 $ | 2'507 $ | 2026-11-06 |
| [GTA 6 Coin](https://dexscreener.com/solana/7dmjqdaiu9pcwcpcjxlrxnqbonjkpc92kzfyrx7tmk1e) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 3'058 $ | 2026-11-06 |
| [MAYHEM](https://dexscreener.com/solana/2tsgelokaeajvegvrrt5ezreya5pthy3x2wstcqc3nfk) GTA MONEY | Markt-Filter: Liquidität 0$ | 0 $ | 2'827 $ | 2026-11-06 |
| [GTA](https://dexscreener.com/solana/6qd5k4vkgpsgsm9x1dqxjtby5ng6zcdkisnvfpfgyps4) Grab That Ass | Markt-Filter: Liquidität 0$ | 0 $ | 482'299 $ | 2026-11-06 |
