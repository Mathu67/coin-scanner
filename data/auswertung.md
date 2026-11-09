# Coin-Scanner – Auswertung

_Stand: 2026-11-09 19:03 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **6.4 Tagen**, **89 Coins** gekauft (Einsatz 890.00 Fr.)
- Status Regel A: 6 bei 4x verkauft, 38 tot, 45 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 483.75 Fr. | **-406.25 Fr.** | -46 % |
| B: Hälfte bei 4x, Rest läuft | 520.08 Fr. | **-369.92 Fr.** | -42 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 533.22 Fr. | **-356.78 Fr.** | -40 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **39 Coins seit Start von Regel D** (Einsatz 390.00 Fr.):
  - A: **-148.71 Fr.** (-38 %)
  - B: **-174.22 Fr.** (-45 %)
  - C: **-179.83 Fr.** (-46 %)
  - D: **-107.24 Fr.** (-27 %)

D abgeschlossen: Stop-Loss 26x, Trailing-Stop 1x, tot 1x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 44 Coins, **-194.95 Fr.** (-44 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 20 von 89 (22 %)
- Mindestens 4x erreicht: 6 von 89 (7 %)
- Mindestens 10x erreicht: 2 von 89 (2 %)
- Auf -95 % oder Liquidität weg (tot): 38 von 89 (43 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -358.95 Fr. | -40 % |
| alles bei 3x | -407.30 Fr. | -46 % |
| alles bei 4x | -420.43 Fr. | -47 % |
| alles bei 5x | -442.54 Fr. | -50 % |
| alles bei 10x | -377.86 Fr. | -42 % |
| alles bei 20x | -365.23 Fr. | -41 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 18.76 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 39.55 Fr. | 9.9x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: verkauft | 29.83 Fr. | 13.70 Fr. | 4.8x |
| [Elysion Pad](https://dexscreener.com/solana/7zh2xzczdslrdr7annmzwntgybx5ifvmawk3hwfouehe) | A: verkauft, B: verkauft | 27.78 Fr. | 13.97 Fr. | 4.0x |
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
| [CLAUDEBOT](https://dexscreener.com/solana/acmjwv27qkaaxrrjfu6dfd1qsbcebn5u5s5acjatygof) CLAUDEBOT | Markt-Filter: zu jung | 18'593 $ | 11'468 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/bkfysyujwx53rjumnbdue7madpe8uoscubfuz4hqtccg) Grand Theft Alice | Markt-Filter: zu jung | 35'047 $ | 207'286 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/9cp73nuksvjwhxvjqvw3v3xo6ymcs7akba6twcaeatjz) Grand Titty Army | Markt-Filter: zu jung | 1'697 $ | 1'609 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/8jpzwhv4kdzp6qqsztexm8pycxhrxaq5tkdg5qpr6zwi) GTA Trump | Markt-Filter: zu jung | 2'139 $ | 1'922 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/f66uvpj1bpqrknxe99bjtuqmg9smipnprqirue96ycfg) Grand Theft Apes | Markt-Filter: zu jung | 13'702 $ | 36'121 $ | 2026-11-09 |
| [PETA](https://dexscreener.com/solana/9jwibvsonp2ab2zaf76ryycgiqucw2xf8jcb9dpcjkhh) Pepetide GTA | Markt-Filter: Liquidität 2122$ | 2'122 $ | 1'946 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fmyuqpjprnbycasqdz6hf2mulmjbuu6rjvt8mse8vky4) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 823 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fzzrktr3yv37dmkq9w862xykthzbcjddjjnbaoabau5n) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 352 $ | 2026-11-09 |
| [GTAVICAT](https://dexscreener.com/solana/g1gw9p4uzhu655rg54ccas4ukjv7af7nrf5cfikzkcud) GTAVICAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'405 $ | 2026-11-09 |
| [Gasgolem](https://dexscreener.com/solana/8tjxcyftfnzwx7e8rxtj51ypvqfgzlzqgsxylohekg3c) ANTHROPIC GAS GOLEM | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-09 |
| [GTA6](https://dexscreener.com/solana/5rjazs9pwatf2gc9hxj2seutww57q1aygdja9ufzb2h6) GTA VI | Markt-Filter: Liquidität 1573$ | 1'573 $ | 1'541 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/ggu7zxbz9nbens18erttk9p1yrrsyo2a5kwrvbbrzrix) Gta | Markt-Filter: Liquidität 0$ | 0 $ | 2'453 $ | 2026-11-09 |
| [ANT](https://dexscreener.com/solana/ce9qsaao9tiztoco4j8a84hc48o1r17anpufnzm1bqic) Anthropic | Markt-Filter: Volumen 47132$ | 64'248 $ | 104'610 $ | 2026-11-09 |
| [GTA6KODAK](https://dexscreener.com/solana/bkaagfumhqvgxa3bqzyabmibsmvietuiapu95prauhx7) GTA6 KODAK BLACK | Markt-Filter: Liquidität 23339$ | 23'339 $ | 95'369 $ | 2026-11-09 |
| [AGTA6](https://dexscreener.com/solana/7tmyzu5blnzzapuvynrzaupjhmjd1draq6caan4mrzvf) after GTA 6 | Markt-Filter: zu alt | 0 $ | 11'888 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/cqfk47mb1xsdxo7mydcdyuw2cof8ad1ebxfwyeuql6yx) Grab That Ass | Markt-Filter: Liquidität 1650$ | 1'650 $ | 1'585 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/gskgzibftdnlhna8wtgc7bk7yz2mtenaqzyjgo9ycuj6) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'510 $ | 2026-11-08 |
| [MOD](https://dexscreener.com/solana/xop7dq4pqahq5f8cbcim3laqsnz5j9kd3xfdrfsgtgn) GTA5 | Markt-Filter: Liquidität 0$ | 0 $ | 354 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/3ncbw8vtqranx4nkfd2heke6w8xzftwel9nhwy978qtr) Grab That Ass | Markt-Filter: Liquidität 1961$ | 1'961 $ | 5'056 $ | 2026-11-08 |
| [MWOLF](https://dexscreener.com/solana/d59tjkurepmra66q48wrkmrqluq5xgh7fakqikpjbrqw) GTA MOONWOLF | Markt-Filter: Liquidität 0$ | 0 $ | 248 $ | 2026-11-08 |
| [GTA6](https://dexscreener.com/solana/girukqkcradhm5aq6gkxddmod8zmkvc6jlxjmudkomdm) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'526 $ | 2026-11-08 |
| [GATOGLITCH](https://dexscreener.com/solana/2ueabe4txr5mchey6ckzvncyczh4mbvyqgtwwubtkk1o) GTA6GLITCH | Markt-Filter: Liquidität 3131$ | 3'131 $ | 3'056 $ | 2026-11-08 |
| [GTAMOON](https://dexscreener.com/solana/2dmgss9oyfhccmi5dpbvpt5mpkhakkagzk2yf5cdjer5) GTA SOON MOON | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: Liquidität 1662$ | 1'662 $ | 1'585 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/9tyhyxseygouvuj66vcjkr4bppi65h2muamuveuyy9wm) GTA VI | Markt-Filter: MCap 55467$ | 50'213 $ | 55'467 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/5afbwvsqpjf4cgejq4tajzyypyuvyktrrn3sahnrpnmv) GTA VI | Markt-Filter: zu alt | 129'570 $ | 14'249'272 $ | 2026-11-07 |
| [GTA6COP](https://dexscreener.com/solana/9sebidesbustw8xbbaczb6ab2ty72p6xp51mftpuwhp6) GTA6 Mendez | Markt-Filter: Liquidität 10018$ | 10'018 $ | 20'778 $ | 2026-11-07 |
| [CLAUDEPAID](https://dexscreener.com/solana/7tx6tl3e14nvhqgk4mfp3wdebmwp3rezsqgflxmrunuy) ClaudePaid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [$GTA6](https://dexscreener.com/solana/fytgbkzjhhcsymys7zbfu5ibxkrmwv8frvswvtdmoekz) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 242 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: Liquidität 0$ | 0 $ | 2'503 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/2hmk1t2s972sl7tmbugr8uh67txctefy5s74j6oaacv4) GTA6 | Markt-Filter: Liquidität 1585$ | 1'585 $ | 1'549 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/4l7yip761fgodtciqvdcbsbqy2jjts2uu6w8a6rhqbxw) Jason Duval  | Markt-Filter: Liquidität 0$ | 0 $ | 2'514 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/cecxwx7qqt6jp4qa956vzpqyuhuqkmbvgsptxenxrcc9) GTA6 | Markt-Filter: Liquidität 1660$ | 1'660 $ | 1'592 $ | 2026-11-07 |
| [GTA6FLAM](https://dexscreener.com/solana/9q8scnfw3zcph1v33emxent1jvaccnw2rvo9d5r4dk63) GTA6Flamingo | Markt-Filter: Liquidität 0$ | 0 $ | 2'487 $ | 2026-11-07 |
| [GTA6DOG](https://dexscreener.com/solana/6d18zgikseb8qkrjadtlltv3ssgxiwhb7njstmjm1kut) GTA6Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'494 $ | 2026-11-07 |
| [MTA6](https://dexscreener.com/solana/fgfdumvdcglkcq4zeq11sgqhklbv3ew8pwybx1mum4ys) Monke GTA6 | Markt-Filter: zu alt | 1'834 $ | 1'697 $ | 2026-11-07 |
