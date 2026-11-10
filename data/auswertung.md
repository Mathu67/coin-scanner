# Coin-Scanner – Auswertung

_Stand: 2026-11-10 16:02 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **7.3 Tagen**, **93 Coins** gekauft (Einsatz 930.00 Fr.)
- Status Regel A: 6 bei 4x verkauft, 46 tot, 41 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 461.56 Fr. | **-468.44 Fr.** | -50 % |
| B: Hälfte bei 4x, Rest läuft | 497.90 Fr. | **-432.10 Fr.** | -46 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 516.22 Fr. | **-413.78 Fr.** | -44 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **43 Coins seit Start von Regel D** (Einsatz 430.00 Fr.):
  - A: **-181.52 Fr.** (-42 %)
  - B: **-207.04 Fr.** (-48 %)
  - C: **-209.72 Fr.** (-49 %)
  - D: **-127.73 Fr.** (-30 %)

D abgeschlossen: Stop-Loss 31x, Trailing-Stop 1x, tot 3x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 52 Coins, **-265.65 Fr.** (-51 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 22 von 93 (24 %)
- Mindestens 4x erreicht: 6 von 93 (6 %)
- Mindestens 10x erreicht: 3 von 93 (3 %)
- Auf -95 % oder Liquidität weg (tot): 46 von 93 (49 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -404.35 Fr. | -43 % |
| alles bei 3x | -463.49 Fr. | -50 % |
| alles bei 4x | -482.61 Fr. | -52 % |
| alles bei 5x | -510.91 Fr. | -55 % |
| alles bei 10x | -418.65 Fr. | -45 % |
| alles bei 20x | -437.78 Fr. | -47 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 19.46 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 37.17 Fr. | 10.1x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: verkauft | 29.83 Fr. | 12.60 Fr. | 4.8x |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) | A: offen, B: offen | 28.36 Fr. | 23.44 Fr. | 3.1x |
| [ORBIT](https://dexscreener.com/solana/ajt7zptztfeo9cqu8yuwddtmoah7bmyt7kmkmhombcne) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.0x |
| [BORLY](https://dexscreener.com/solana/7xwnpcwt4upj2hyuff4czvmmsvvws13k1w8ip6y4o5zq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 42 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [$GTA6](https://dexscreener.com/solana/5k1p5ykgqmu4nh67lvajwrkuwujenq76xgczzguwcicn) GTA6 | Markt-Filter: zu jung | 0 $ | 61 $ | 2026-11-10 |
| [WNTDDG GTA](https://dexscreener.com/solana/9anbun9pidak3rrtdflw9ce6cnrmswozzkybqgqktjxj) Wanted Dog | Markt-Filter: zu jung | 0 $ | 27 $ | 2026-11-10 |
| [GTCM](https://dexscreener.com/solana/5uirmf5wblsbxpx2za8p9ksfaay7aychsoqdzcyrptki) GTA CAT MAYHEM | Markt-Filter: zu jung | 0 $ | 1'155 $ | 2026-11-10 |
| [GTA 6](https://dexscreener.com/solana/an97u6gmthed1mymro2x9gyu62wktzfyu1ybahihyn5n) GTA 6 Updates | Markt-Filter: zu jung | 1'571 $ | 1'550 $ | 2026-11-10 |
| [ANT](https://dexscreener.com/solana/bivbn5dk1bjbk9sgasy4uziuh98pdsceqwnofxurywgf) Anthropic | Markt-Filter: zu jung | 0 $ | 2'337 $ | 2026-11-10 |
| [GTAVI](https://dexscreener.com/solana/adny4gknyqeruieyykqmxb3t1qceufogoao1pmceqeux) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 610 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/d4rug4cgsgqf2kugvbzcl9abbn743v2hqgbchvf2nkqy) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [CTA](https://dexscreener.com/solana/5cfxror3c1dc4grpqapudio4sh4wrkvnfca6sotbuhuc) CLAUDE THE ALLIGATOR | Markt-Filter: Liquidität 0$ | 0 $ | 2'401 $ | 2026-11-10 |
| [CLAUDE](https://dexscreener.com/solana/rzpgi3firhb7wkmtbznmvhuu2rc6c2wibjsjz5r1w7b) Claude The Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA4](https://dexscreener.com/solana/gflwdv18d7q8j1vbxuvpk4rayesrkf7fevzzlprj66ga) GTA IV | Markt-Filter: Liquidität 12619$ | 12'619 $ | 6'460 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/8npwyqgvv2z3pauiy8ydswqp3qim8amnm3hkuulsltnv) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA6](https://dexscreener.com/solana/fqqsjjtuhs3go7ponkgmrccwhkfot72knvneotgpvq9q) GTA VI | Markt-Filter: Liquidität 1566$ | 1'566 $ | 1'535 $ | 2026-11-10 |
| [GTAPE](https://dexscreener.com/solana/hmaehlol5khrbo1mdfdwndzq1degt5whpyyqn6phjqdo) GTAPE | Markt-Filter: Liquidität 0$ | 0 $ | 2'481 $ | 2026-11-09 |
| [GTFLOPPA](https://dexscreener.com/solana/lkre6pa2mxlvjixub7m5fowsivhpxgqkzt2d5y3p3ts) Grand Theft Floppa | Markt-Filter: Liquidität 0$ | 0 $ | 2'414 $ | 2026-11-09 |
| [$GTAINU](https://dexscreener.com/solana/7x7r2safcabbefphfucmjrvqxipanpa1rgs2mudy1pyr) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'421 $ | 2026-11-09 |
| [CLAUDEBOT](https://dexscreener.com/solana/acmjwv27qkaaxrrjfu6dfd1qsbcebn5u5s5acjatygof) CLAUDEBOT | Markt-Filter: Liquidität 0$ | 0 $ | 537 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/bkfysyujwx53rjumnbdue7madpe8uoscubfuz4hqtccg) Grand Theft Alice | Markt-Filter: Liquidität 1716$ | 1'716 $ | 1'603 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/9cp73nuksvjwhxvjqvw3v3xo6ymcs7akba6twcaeatjz) Grand Titty Army | Markt-Filter: Liquidität 1602$ | 1'602 $ | 1'519 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/8jpzwhv4kdzp6qqsztexm8pycxhrxaq5tkdg5qpr6zwi) GTA Trump | Markt-Filter: Liquidität 2028$ | 2'028 $ | 1'819 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/f66uvpj1bpqrknxe99bjtuqmg9smipnprqirue96ycfg) Grand Theft Apes | Sicherheits-Filter: Top-10 halten 27% | 27'524 $ | 128'493 $ | 2026-11-09 |
| [PETA](https://dexscreener.com/solana/9jwibvsonp2ab2zaf76ryycgiqucw2xf8jcb9dpcjkhh) Pepetide GTA | Markt-Filter: Liquidität 1845$ | 1'845 $ | 1'670 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fmyuqpjprnbycasqdz6hf2mulmjbuu6rjvt8mse8vky4) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 823 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fzzrktr3yv37dmkq9w862xykthzbcjddjjnbaoabau5n) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 352 $ | 2026-11-09 |
| [GTAVICAT](https://dexscreener.com/solana/g1gw9p4uzhu655rg54ccas4ukjv7af7nrf5cfikzkcud) GTAVICAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'405 $ | 2026-11-09 |
| [Gasgolem](https://dexscreener.com/solana/8tjxcyftfnzwx7e8rxtj51ypvqfgzlzqgsxylohekg3c) ANTHROPIC GAS GOLEM | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-09 |
| [GTA6](https://dexscreener.com/solana/5rjazs9pwatf2gc9hxj2seutww57q1aygdja9ufzb2h6) GTA VI | Markt-Filter: Liquidität 1578$ | 1'578 $ | 1'545 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/ggu7zxbz9nbens18erttk9p1yrrsyo2a5kwrvbbrzrix) Gta | Markt-Filter: Liquidität 0$ | 0 $ | 2'453 $ | 2026-11-09 |
| [ANT](https://dexscreener.com/solana/ce9qsaao9tiztoco4j8a84hc48o1r17anpufnzm1bqic) Anthropic | Sicherheits-Filter: Top-10 halten 26% | 67'912 $ | 116'543 $ | 2026-11-09 |
| [GTA6KODAK](https://dexscreener.com/solana/bkaagfumhqvgxa3bqzyabmibsmvietuiapu95prauhx7) GTA6 KODAK BLACK | Sicherheits-Filter: Top-10 halten 42% | 26'640 $ | 124'044 $ | 2026-11-09 |
| [AGTA6](https://dexscreener.com/solana/7tmyzu5blnzzapuvynrzaupjhmjd1draq6caan4mrzvf) after GTA 6 | Markt-Filter: zu alt | 0 $ | 11'888 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/cqfk47mb1xsdxo7mydcdyuw2cof8ad1ebxfwyeuql6yx) Grab That Ass | Markt-Filter: Liquidität 1621$ | 1'621 $ | 1'557 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/gskgzibftdnlhna8wtgc7bk7yz2mtenaqzyjgo9ycuj6) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'510 $ | 2026-11-08 |
| [MOD](https://dexscreener.com/solana/xop7dq4pqahq5f8cbcim3laqsnz5j9kd3xfdrfsgtgn) GTA5 | Markt-Filter: Liquidität 0$ | 0 $ | 354 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/3ncbw8vtqranx4nkfd2heke6w8xzftwel9nhwy978qtr) Grab That Ass | Markt-Filter: Liquidität 1121$ | 1'121 $ | 2'802 $ | 2026-11-08 |
| [MWOLF](https://dexscreener.com/solana/d59tjkurepmra66q48wrkmrqluq5xgh7fakqikpjbrqw) GTA MOONWOLF | Markt-Filter: Liquidität 0$ | 0 $ | 248 $ | 2026-11-08 |
| [GTA6](https://dexscreener.com/solana/girukqkcradhm5aq6gkxddmod8zmkvc6jlxjmudkomdm) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'526 $ | 2026-11-08 |
| [GATOGLITCH](https://dexscreener.com/solana/2ueabe4txr5mchey6ckzvncyczh4mbvyqgtwwubtkk1o) GTA6GLITCH | Markt-Filter: Liquidität 2800$ | 2'800 $ | 2'655 $ | 2026-11-08 |
| [GTAMOON](https://dexscreener.com/solana/2dmgss9oyfhccmi5dpbvpt5mpkhakkagzk2yf5cdjer5) GTA SOON MOON | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: Liquidität 1661$ | 1'661 $ | 1'583 $ | 2026-11-07 |
