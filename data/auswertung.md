# Coin-Scanner – Auswertung

_Stand: 2026-11-10 02:35 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **6.7 Tagen**, **89 Coins** gekauft (Einsatz 890.00 Fr.)
- Status Regel A: 6 bei 4x verkauft, 42 tot, 41 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 456.99 Fr. | **-433.01 Fr.** | -49 % |
| B: Hälfte bei 4x, Rest läuft | 493.33 Fr. | **-396.67 Fr.** | -45 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 523.72 Fr. | **-366.28 Fr.** | -41 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **39 Coins seit Start von Regel D** (Einsatz 390.00 Fr.):
  - A: **-165.60 Fr.** (-42 %)
  - B: **-191.11 Fr.** (-49 %)
  - C: **-184.95 Fr.** (-47 %)
  - D: **-109.73 Fr.** (-28 %)

D abgeschlossen: Stop-Loss 28x, Trailing-Stop 1x, tot 2x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 48 Coins, **-233.89 Fr.** (-49 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 20 von 89 (22 %)
- Mindestens 4x erreicht: 6 von 89 (7 %)
- Mindestens 10x erreicht: 2 von 89 (2 %)
- Auf -95 % oder Liquidität weg (tot): 42 von 89 (47 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -376.64 Fr. | -42 % |
| alles bei 3x | -433.08 Fr. | -49 % |
| alles bei 4x | -447.18 Fr. | -50 % |
| alles bei 5x | -463.56 Fr. | -52 % |
| alles bei 10x | -386.32 Fr. | -43 % |
| alles bei 20x | -368.48 Fr. | -41 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 22.37 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 45.30 Fr. | 9.9x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: verkauft | 29.83 Fr. | 14.05 Fr. | 4.8x |
| [Elysion Pad](https://dexscreener.com/solana/7zh2xzczdslrdr7annmzwntgybx5ifvmawk3hwfouehe) | A: verkauft, B: verkauft | 27.78 Fr. | 16.93 Fr. | 4.0x |
| [AMD](https://dexscreener.com/solana/e9wpfxjqvwvdjkculu2xs742t6ehbn2cnzv2ps24fz14) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.2x |
| [ORBIT](https://dexscreener.com/solana/ajt7zptztfeo9cqu8yuwddtmoah7bmyt7kmkmhombcne) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.0x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 43 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTA4](https://dexscreener.com/solana/gflwdv18d7q8j1vbxuvpk4rayesrkf7fevzzlprj66ga) GTA IV | Markt-Filter: zu jung | 70'449 $ | 194'853 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/8npwyqgvv2z3pauiy8ydswqp3qim8amnm3hkuulsltnv) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA6](https://dexscreener.com/solana/fqqsjjtuhs3go7ponkgmrccwhkfot72knvneotgpvq9q) GTA VI | Markt-Filter: zu jung | 1'558 $ | 1'549 $ | 2026-11-10 |
| [GTAPE](https://dexscreener.com/solana/hmaehlol5khrbo1mdfdwndzq1degt5whpyyqn6phjqdo) GTAPE | Markt-Filter: zu jung | 0 $ | 2'716 $ | 2026-11-09 |
| [GTFLOPPA](https://dexscreener.com/solana/lkre6pa2mxlvjixub7m5fowsivhpxgqkzt2d5y3p3ts) Grand Theft Floppa | Markt-Filter: zu jung | 0 $ | 2'414 $ | 2026-11-09 |
| [$GTAINU](https://dexscreener.com/solana/7x7r2safcabbefphfucmjrvqxipanpa1rgs2mudy1pyr) GTAINU | Markt-Filter: zu jung | 0 $ | 2'421 $ | 2026-11-09 |
| [CLAUDEBOT](https://dexscreener.com/solana/acmjwv27qkaaxrrjfu6dfd1qsbcebn5u5s5acjatygof) CLAUDEBOT | Markt-Filter: Liquidität 0$ | 0 $ | 537 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/bkfysyujwx53rjumnbdue7madpe8uoscubfuz4hqtccg) Grand Theft Alice | Markt-Filter: Liquidität 1771$ | 1'771 $ | 1'652 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/9cp73nuksvjwhxvjqvw3v3xo6ymcs7akba6twcaeatjz) Grand Titty Army | Markt-Filter: Liquidität 1735$ | 1'735 $ | 1'647 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/8jpzwhv4kdzp6qqsztexm8pycxhrxaq5tkdg5qpr6zwi) GTA Trump | Markt-Filter: Liquidität 2127$ | 2'127 $ | 1'909 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/f66uvpj1bpqrknxe99bjtuqmg9smipnprqirue96ycfg) Grand Theft Apes | Markt-Filter: Liquidität 15711$ | 15'711 $ | 45'423 $ | 2026-11-09 |
| [PETA](https://dexscreener.com/solana/9jwibvsonp2ab2zaf76ryycgiqucw2xf8jcb9dpcjkhh) Pepetide GTA | Markt-Filter: Liquidität 1961$ | 1'961 $ | 1'777 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fmyuqpjprnbycasqdz6hf2mulmjbuu6rjvt8mse8vky4) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 823 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fzzrktr3yv37dmkq9w862xykthzbcjddjjnbaoabau5n) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 352 $ | 2026-11-09 |
| [GTAVICAT](https://dexscreener.com/solana/g1gw9p4uzhu655rg54ccas4ukjv7af7nrf5cfikzkcud) GTAVICAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'405 $ | 2026-11-09 |
| [Gasgolem](https://dexscreener.com/solana/8tjxcyftfnzwx7e8rxtj51ypvqfgzlzqgsxylohekg3c) ANTHROPIC GAS GOLEM | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-09 |
| [GTA6](https://dexscreener.com/solana/5rjazs9pwatf2gc9hxj2seutww57q1aygdja9ufzb2h6) GTA VI | Markt-Filter: Liquidität 1578$ | 1'578 $ | 1'545 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/ggu7zxbz9nbens18erttk9p1yrrsyo2a5kwrvbbrzrix) Gta | Markt-Filter: Liquidität 0$ | 0 $ | 2'453 $ | 2026-11-09 |
| [ANT](https://dexscreener.com/solana/ce9qsaao9tiztoco4j8a84hc48o1r17anpufnzm1bqic) Anthropic | Sicherheits-Filter: Top-10 halten 26% | 67'912 $ | 116'543 $ | 2026-11-09 |
| [GTA6KODAK](https://dexscreener.com/solana/bkaagfumhqvgxa3bqzyabmibsmvietuiapu95prauhx7) GTA6 KODAK BLACK | Markt-Filter: Liquidität 22246$ | 22'246 $ | 87'044 $ | 2026-11-09 |
| [AGTA6](https://dexscreener.com/solana/7tmyzu5blnzzapuvynrzaupjhmjd1draq6caan4mrzvf) after GTA 6 | Markt-Filter: zu alt | 0 $ | 11'888 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/cqfk47mb1xsdxo7mydcdyuw2cof8ad1ebxfwyeuql6yx) Grab That Ass | Markt-Filter: Liquidität 1650$ | 1'650 $ | 1'585 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/gskgzibftdnlhna8wtgc7bk7yz2mtenaqzyjgo9ycuj6) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'510 $ | 2026-11-08 |
| [MOD](https://dexscreener.com/solana/xop7dq4pqahq5f8cbcim3laqsnz5j9kd3xfdrfsgtgn) GTA5 | Markt-Filter: Liquidität 0$ | 0 $ | 354 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/3ncbw8vtqranx4nkfd2heke6w8xzftwel9nhwy978qtr) Grab That Ass | Markt-Filter: Liquidität 1725$ | 1'725 $ | 4'992 $ | 2026-11-08 |
| [MWOLF](https://dexscreener.com/solana/d59tjkurepmra66q48wrkmrqluq5xgh7fakqikpjbrqw) GTA MOONWOLF | Markt-Filter: Liquidität 0$ | 0 $ | 248 $ | 2026-11-08 |
| [GTA6](https://dexscreener.com/solana/girukqkcradhm5aq6gkxddmod8zmkvc6jlxjmudkomdm) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'526 $ | 2026-11-08 |
| [GATOGLITCH](https://dexscreener.com/solana/2ueabe4txr5mchey6ckzvncyczh4mbvyqgtwwubtkk1o) GTA6GLITCH | Markt-Filter: Liquidität 3071$ | 3'071 $ | 2'982 $ | 2026-11-08 |
| [GTAMOON](https://dexscreener.com/solana/2dmgss9oyfhccmi5dpbvpt5mpkhakkagzk2yf5cdjer5) GTA SOON MOON | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: Liquidität 1661$ | 1'661 $ | 1'583 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/9tyhyxseygouvuj66vcjkr4bppi65h2muamuveuyy9wm) GTA VI | Markt-Filter: MCap 44526$ | 45'637 $ | 44'526 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/5afbwvsqpjf4cgejq4tajzyypyuvyktrrn3sahnrpnmv) GTA VI | Markt-Filter: zu alt | 129'570 $ | 14'249'272 $ | 2026-11-07 |
| [GTA6COP](https://dexscreener.com/solana/9sebidesbustw8xbbaczb6ab2ty72p6xp51mftpuwhp6) GTA6 Mendez | Markt-Filter: Liquidität 7394$ | 7'394 $ | 12'437 $ | 2026-11-07 |
| [CLAUDEPAID](https://dexscreener.com/solana/7tx6tl3e14nvhqgk4mfp3wdebmwp3rezsqgflxmrunuy) ClaudePaid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [$GTA6](https://dexscreener.com/solana/fytgbkzjhhcsymys7zbfu5ibxkrmwv8frvswvtdmoekz) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 242 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: Liquidität 0$ | 0 $ | 2'503 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
