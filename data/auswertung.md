# Coin-Scanner – Auswertung

_Stand: 2026-11-08 18:59 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **5.4 Tagen**, **80 Coins** gekauft (Einsatz 800.00 Fr.)
- Status Regel A: 5 bei 4x verkauft, 27 tot, 48 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 541.64 Fr. | **-258.36 Fr.** | -32 % |
| B: Hälfte bei 4x, Rest läuft | 598.23 Fr. | **-201.77 Fr.** | -25 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 586.64 Fr. | **-213.36 Fr.** | -27 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **30 Coins seit Start von Regel D** (Einsatz 300.00 Fr.):
  - A: **-32.40 Fr.** (-11 %)
  - B: **-40.18 Fr.** (-13 %)
  - C: **-60.49 Fr.** (-20 %)
  - D: **-43.47 Fr.** (-14 %)

D abgeschlossen: Stop-Loss 19x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 32 Coins, **-119.90 Fr.** (-37 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 16 von 80 (20 %)
- Mindestens 4x erreicht: 5 von 80 (6 %)
- Mindestens 10x erreicht: 2 von 80 (2 %)
- Auf -95 % oder Liquidität weg (tot): 27 von 80 (34 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -267.05 Fr. | -33 % |
| alles bei 3x | -284.44 Fr. | -36 % |
| alles bei 4x | -268.12 Fr. | -34 % |
| alles bei 5x | -269.44 Fr. | -34 % |
| alles bei 10x | -190.33 Fr. | -24 % |
| alles bei 20x | -171.43 Fr. | -21 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 23.10 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 25.11 Fr. | 9.9x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: offen | 32.34 Fr. | 22.37 Fr. | 4.8x |
| [Elysion Pad](https://dexscreener.com/solana/7zh2xzczdslrdr7annmzwntgybx5ifvmawk3hwfouehe) | A: verkauft, B: verkauft | 27.78 Fr. | 20.56 Fr. | 4.0x |
| [AMD](https://dexscreener.com/solana/e9wpfxjqvwvdjkculu2xs742t6ehbn2cnzv2ps24fz14) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.2x |
| [ORBIT](https://dexscreener.com/solana/ajt7zptztfeo9cqu8yuwddtmoah7bmyt7kmkmhombcne) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.0x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 39 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [$GTAINU](https://dexscreener.com/solana/gskgzibftdnlhna8wtgc7bk7yz2mtenaqzyjgo9ycuj6) GTAINU | Markt-Filter: zu jung | 0 $ | 2'510 $ | 2026-11-08 |
| [MOD](https://dexscreener.com/solana/xop7dq4pqahq5f8cbcim3laqsnz5j9kd3xfdrfsgtgn) GTA5 | Markt-Filter: zu jung | 0 $ | 367 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/3ncbw8vtqranx4nkfd2heke6w8xzftwel9nhwy978qtr) Grab That Ass | Markt-Filter: zu jung | 722 $ | 1'721 $ | 2026-11-08 |
| [MWOLF](https://dexscreener.com/solana/d59tjkurepmra66q48wrkmrqluq5xgh7fakqikpjbrqw) GTA MOONWOLF | Markt-Filter: zu jung | 0 $ | 248 $ | 2026-11-08 |
| [GTA6](https://dexscreener.com/solana/girukqkcradhm5aq6gkxddmod8zmkvc6jlxjmudkomdm) GTA6 | Markt-Filter: zu jung | 0 $ | 2'526 $ | 2026-11-08 |
| [GATOGLITCH](https://dexscreener.com/solana/2ueabe4txr5mchey6ckzvncyczh4mbvyqgtwwubtkk1o) GTA6GLITCH | Markt-Filter: Liquidität 3278$ | 3'278 $ | 3'214 $ | 2026-11-08 |
| [GTAMOON](https://dexscreener.com/solana/2dmgss9oyfhccmi5dpbvpt5mpkhakkagzk2yf5cdjer5) GTA SOON MOON | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: Liquidität 1764$ | 1'764 $ | 1'683 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/9tyhyxseygouvuj66vcjkr4bppi65h2muamuveuyy9wm) GTA VI | Markt-Filter: MCap 66849$ | 55'931 $ | 66'849 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/5afbwvsqpjf4cgejq4tajzyypyuvyktrrn3sahnrpnmv) GTA VI | Markt-Filter: zu alt | 129'570 $ | 14'249'272 $ | 2026-11-07 |
| [GTA6COP](https://dexscreener.com/solana/9sebidesbustw8xbbaczb6ab2ty72p6xp51mftpuwhp6) GTA6 Mendez | Markt-Filter: Liquidität 15050$ | 15'050 $ | 41'688 $ | 2026-11-07 |
| [CLAUDEPAID](https://dexscreener.com/solana/7tx6tl3e14nvhqgk4mfp3wdebmwp3rezsqgflxmrunuy) ClaudePaid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [$GTA6](https://dexscreener.com/solana/fytgbkzjhhcsymys7zbfu5ibxkrmwv8frvswvtdmoekz) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 242 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: Liquidität 0$ | 0 $ | 2'500 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/2hmk1t2s972sl7tmbugr8uh67txctefy5s74j6oaacv4) GTA6 | Markt-Filter: Liquidität 1651$ | 1'651 $ | 1'614 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/4l7yip761fgodtciqvdcbsbqy2jjts2uu6w8a6rhqbxw) Jason Duval  | Markt-Filter: Liquidität 0$ | 0 $ | 2'514 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/cecxwx7qqt6jp4qa956vzpqyuhuqkmbvgsptxenxrcc9) GTA6 | Markt-Filter: Liquidität 1737$ | 1'737 $ | 1'667 $ | 2026-11-07 |
| [GTA6FLAM](https://dexscreener.com/solana/9q8scnfw3zcph1v33emxent1jvaccnw2rvo9d5r4dk63) GTA6Flamingo | Markt-Filter: Liquidität 0$ | 0 $ | 2'487 $ | 2026-11-07 |
| [GTA6DOG](https://dexscreener.com/solana/6d18zgikseb8qkrjadtlltv3ssgxiwhb7njstmjm1kut) GTA6Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'494 $ | 2026-11-07 |
| [MTA6](https://dexscreener.com/solana/fgfdumvdcglkcq4zeq11sgqhklbv3ew8pwybx1mum4ys) Monke GTA6 | Markt-Filter: Liquidität 1896$ | 1'896 $ | 1'755 $ | 2026-11-07 |
| [solana](https://dexscreener.com/solana/h71ihsvdcdoab21yxedbb4xddhqrivp6xzpq9doycchb) LUCIA GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 2'524 $ | 2026-11-07 |
| [GTAmid](https://dexscreener.com/solana/ajzgg3thcspk857xvjerzmwn5saptqyhyh6vb6ijqfkt) GTAmid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [ATM](https://dexscreener.com/solana/1ukbur4jm7vbzfa6anncn9gr2hkactfbl9yae7543xz) GTA6ATM | Markt-Filter: Liquidität 2296$ | 2'296 $ | 2'102 $ | 2026-11-07 |
| [ROCCO](https://dexscreener.com/solana/eenwnbco7lyuysb8r8omaqutz85jc52eizxmfcfzwko7) GTA6 DOGE | Markt-Filter: Liquidität 1769$ | 1'769 $ | 1'667 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/bwfwgjeu3nitww44w2caeocvzqdybxhjhdnmkbgefg71) Grand Theft Airlines | Markt-Filter: Liquidität 2087$ | 2'087 $ | 1'978 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/66litxo66tc7g8kyg52c5kyqnulosrul6qod4dcxczvt) Grand Theft Airlines | Markt-Filter: Liquidität 1778$ | 1'778 $ | 1'662 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/ee7tn5dh18dwgpe9ste5g2dxeh6h63sb5yyckjfkyazb) Grand Theft Animal 6 | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA6K9](https://dexscreener.com/solana/bodz7ruysgf65hhz2aypprdtxik9onerskwhplhrb4xx) GTA6DOG | Sicherheits-Filter: Top-10 halten 56% | 27'742 $ | 129'074 $ | 2026-11-07 |
| [Claude](https://dexscreener.com/solana/9ug8i5hzyctcjugpbvjvegb1duuwdkipaumshuqexhhc) Be Nice To Claude | Markt-Filter: Liquidität 1671$ | 1'671 $ | 1'612 $ | 2026-11-07 |
| [CHOP](https://dexscreener.com/solana/d6mch8n2sxvdctlssrvoss46iwqvneiakbstkqusc2h) GTA Chop | Markt-Filter: zu alt | 37'429 $ | 205'430 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/4xbsv7yftzzeaxdjk77sgteas1mehwbb73ghuwhvj8sg) Giga Titty Ass | Markt-Filter: Liquidität 1763$ | 1'763 $ | 1'657 $ | 2026-11-07 |
| [RICO](https://dexscreener.com/solana/8mzdl9h38zzyalwfkprtapp9kyroxqw2x8etsd5981ya) GTA6DOG | Markt-Filter: Liquidität 0$ | 0 $ | 2'552 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/coburtyqxtw3j3fbu6lkz8pftw1pkuk2qjd1fgjju9ae) Giga Titty Ass | Markt-Filter: zu alt | 1'725 $ | 1'644 $ | 2026-11-07 |
| [GTM](https://dexscreener.com/solana/gro4fjwsbkcbzhqlekfhsofxrsxoawowqyqe5ncqaw8e) Grand Theft Mini Woke City | Markt-Filter: Liquidität 0$ | 0 $ | 2'507 $ | 2026-11-07 |
| [INVEST](https://dexscreener.com/solana/j1z33dbp71pkjwv7p5fmitoegpcdj8d6f8lfmr5nxwgm) Claude Invest | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/5r5rcy8jfrrgmnzguxihso45jgw2zkz2kpvms1kvkvsd) Grand Tits of America | Markt-Filter: zu alt | 1'740 $ | 1'664 $ | 2026-11-07 |
