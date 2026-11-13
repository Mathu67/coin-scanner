# Coin-Scanner – Auswertung

_Stand: 2026-11-13 13:37 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **10.2 Tagen**, **128 Coins** gekauft (Einsatz 1'280.00 Fr.)
- Status Regel A: 11 bei 4x verkauft, 72 tot, 45 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 687.87 Fr. | **-592.13 Fr.** | -46 % |
| B: Hälfte bei 4x, Rest läuft | 687.15 Fr. | **-592.85 Fr.** | -46 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 673.70 Fr. | **-606.30 Fr.** | -47 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **78 Coins seit Start von Regel D** (Einsatz 780.00 Fr.):
  - A: **-310.87 Fr.** (-40 %)
  - B: **-373.44 Fr.** (-48 %)
  - C: **-400.92 Fr.** (-51 %)
  - D: **-250.34 Fr.** (-32 %)

D abgeschlossen: Stop-Loss 56x, Trailing-Stop 1x, Zeit-Stop 1x, tot 6x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 83 Coins, **-364.60 Fr.** (-44 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 30 von 128 (23 %)
- Mindestens 4x erreicht: 11 von 128 (9 %)
- Mindestens 10x erreicht: 3 von 128 (2 %)
- Auf -95 % oder Liquidität weg (tot): 72 von 128 (56 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -572.33 Fr. | -45 % |
| alles bei 3x | -668.38 Fr. | -52 % |
| alles bei 4x | -627.76 Fr. | -49 % |
| alles bei 5x | -679.01 Fr. | -53 % |
| alles bei 10x | -627.77 Fr. | -49 % |
| alles bei 20x | -664.91 Fr. | -52 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [inuhao](https://dexscreener.com/solana/aqfc3qfatjggpqeuqgs65ruaqq5u2pin6myjz1eu4s31) | A: verkauft, B: offen | 44.09 Fr. | 36.08 Fr. | 6.1x |
| [NOBUSHIBA](https://dexscreener.com/solana/dagau7g32pmkjf8ng2372xo2hygfgenx5yn7mwmkhfgf) | A: verkauft, B: verkauft | 43.40 Fr. | 10.08 Fr. | 6.7x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 12.80 Fr. | 10.6x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: verkauft, B: offen | 35.63 Fr. | 25.51 Fr. | 4.3x |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |
| [NATF](https://dexscreener.com/solana/gfdksknxksjeddbc1hzwbz2q5kqur6xdv5q9w5ltjdxm) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |

Der beste Coin macht 28 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Genug Coins für eine brauchbare Einschätzung (kein Beweis).
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTA](https://dexscreener.com/solana/hy5savp4t8i8skmwlnwwgmzqnmhyucxai57a5hjqvga) Grand Trench Auto | Markt-Filter: zu jung | 0 $ | 2'247 $ | 2026-11-13 |
| [VI](https://dexscreener.com/solana/ebypqwwe1w8cmqcm2or9ixzvs9zhavc9cptklwpse31a) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 1'440 $ | 2026-11-13 |
| [BUX](https://dexscreener.com/solana/aodq34rjcjuszkdk2hnnj8sloadwfboe52fb1sc3xnpw) Grand Theft Agents | Markt-Filter: Liquidität 0$ | 0 $ | 38'547 $ | 2026-11-13 |
| [ROCCO](https://dexscreener.com/solana/2cv9fs87aiwrcgnxbeghxkbfajx8mi2mywsqxrsayvui) Rocco GTA VI Dog | Markt-Filter: Liquidität 0$ | 0 $ | 8'312 $ | 2026-11-13 |
| [GTAINU](https://dexscreener.com/solana/9cggxyegoygqf8rf7su6ktwtoqlsnxmnp6bd8u5ohvwf) GTA Inu | Markt-Filter: Liquidität 1542$ | 1'542 $ | 1'460 $ | 2026-11-13 |
| [GTATRENCH](https://dexscreener.com/solana/4trg9bpje6khpivk5jdf5eds3sckfptfqn4dfxrgdtus) GTA TRENCH | Markt-Filter: Liquidität 0$ | 0 $ | 2'281 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/bypyjk9gcsa5moeoagqbrfubqix8cqn44slp3rkic3ns) Girls Throwing Ass | Markt-Filter: Liquidität 0$ | 0 $ | 2'269 $ | 2026-11-12 |
| [GTAMAS](https://dexscreener.com/solana/atbnegfn2pzxm6vndmugwv4o51yzdm76rfjeofslibgg) GTAMAS | Markt-Filter: Liquidität 0$ | 0 $ | 3'420 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/2y1xtb5vjcrmabkfupnygkh68yzjhx3xkrd8es9z2e2z) VICE CITY | Markt-Filter: Liquidität 0$ | 0 $ | 59 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/8h16btmaedxzqyoxdwlt2znrj4gc8kw6nkjaigatgapr) Girls Throwing Ass | Markt-Filter: Liquidität 1$ | 1 $ | 2'010'881 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/d3thivp3fdwktx6x9tlp7ka11wfflt5pxdofhr1wfxwt) Giant Thick Ass | Markt-Filter: Liquidität 0$ | 0 $ | 2'279 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/3ktr4wufbveklrcezwg4vgvrqasagzqxodck3evkd792) Grand Theft Affair | Markt-Filter: Liquidität 1701$ | 1'701 $ | 1'564 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/8hayj1ynkzqmfjwx74pwdku3m3wln8t5sxmt8895suv) Claude Cat | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTA Six](https://dexscreener.com/solana/av2bymmsfsfnvtgdmkzgtnsg9e8mzcowsmm6ihsnkklk) Grand Theft Auto VI | Markt-Filter: Liquidität 1610$ | 1'610 $ | 1'506 $ | 2026-11-12 |
| [ANTHROPE](https://dexscreener.com/solana/bnckk6axyhlyex6mwu8nvtigsdjchnlhlcf5itiqupvn) Anthropic Pepe | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTAmeme](https://dexscreener.com/solana/c9etl7uz66lmgqgxc9u4ieudnnjyzimmzxi2hgfm9bik) GTA | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/5675urx53hj1uatagbki6ecp1rvddksffzx5hjj6nmaf) Claudecoin | Markt-Filter: Liquidität 0$ | 0 $ | 1'555 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/ayvp8hu6xbkx3km6qgyfkfvz8t5umesjwhwdsodawrgt) Claudecoin | Markt-Filter: Liquidität 1625$ | 1'625 $ | 1'521 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/av8nnjo59e9qxmrsj7rncdfnwbjolc3w2w2k6x5etxew) Claudecoin | Markt-Filter: Liquidität 0$ | 0 $ | 219 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/djb2hkkmionjb4vu6paejrsomqgrf3c884vhfwecnthy) Claude the Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/aptfoegpup16qstekfwzvrygipzhvbmdl56ewmbdbytz) Claudecoin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CODE](https://dexscreener.com/solana/e1dvqdszz1eiisnlxachrqurtmsyjja9blc9at1jxzcv) Claude Code Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/76dhpzci994kcacipvwsyhjrqjgy5ewwqvq48wgfyzwi) Grand Theft Auto: Vice City | Markt-Filter: Liquidität 0$ | 0 $ | 3'095 $ | 2026-11-12 |
| [GTAV](https://dexscreener.com/solana/dlwbtq6srzsebme95k5perlzddnzpp3169fsofdy9aj7) Grand Theft Auto V | Markt-Filter: Liquidität 0$ | 0 $ | 3'046 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/gncawlgbkstxtxejfj6j68ns3wbir1w9qfdf4mg2kq9f) Grand Theft Auto VI | Markt-Filter: Liquidität 6$ | 6 $ | 5'830 $ | 2026-11-12 |
| [GTA 6.0](https://dexscreener.com/solana/bea4eet5lqvp4gdeb3mbqioo98t1kxr3sakueqpthgte) Grand Theft Auto VI | Markt-Filter: Liquidität 12857$ | 12'857 $ | 34'057 $ | 2026-11-12 |
| [GTA6](https://dexscreener.com/solana/4vj3nrvxvedyepybojbt5hjoikxj62teac5uvrusyykk) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'338 $ | 2026-11-11 |
| [GTA6Dog](https://dexscreener.com/solana/9zrngpz8jjstjnppsj3edv8drmjxkuadcrz2v6pfqusx) Gta6 dog | Markt-Filter: Liquidität 0$ | 0 $ | 856 $ | 2026-11-11 |
| [GTA6TRUMP](https://dexscreener.com/solana/emp4rvcuuarfsxyxcxecrjeoshjwnmgprycdgzx5mnd8) GTATRUMP | Sicherheits-Filter: Risiko: Creator history of rugged tokens | 25'159 $ | 115'805 $ | 2026-11-11 |
| [GTAFEVER](https://dexscreener.com/solana/e2d5cqnag7knvrvorzghdfjbufwycqv9d3xxzfqy89if) GTA VI FEVER | Markt-Filter: Liquidität 0$ | 0 $ | 3'633 $ | 2026-11-11 |
| [GTA$](https://dexscreener.com/solana/3fbyy8s1zbqarqpxfeeamxlnuebuxjnk4gsqrgbq3nky) Grand Theft Auto Dollars | Markt-Filter: Liquidität 20740$ | 20'740 $ | 54'054 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/fednfeglt8zfmgh4wkwzenb8bvbc8a2uik3kvngv3mxc) Grab That Ass | Markt-Filter: Liquidität 1608$ | 1'608 $ | 1'543 $ | 2026-11-11 |
| [TGATO](https://dexscreener.com/solana/byecx7tv5vpjjkruoypctc92twfbpre2ktqck9xrkhar) Trevor GTA6CAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [DTA](https://dexscreener.com/solana/hmxcypmqv7qol5vb8gzjnr6axgt4n4pdcmxurx6ca2on) GTA Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'350 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/ga3bqrkhfq4c5eldamitpfue1gchaphyeubqkeshihvu) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'269 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/fas2rmsutcfcvg3zbngb7bm9zxtopazxrkvhcynn7dyo) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 1'363 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/6praz8pjaatsaxxzy6hoeavnhpxek7ww2r6kanudxubn) Grand Theft Agent | Markt-Filter: Liquidität 2428$ | 2'428 $ | 2'312 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/g7aswxsctw7phzw2bq8w2kljjfl2chgk66jwzc9st26p) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 6 $ | 2026-11-11 |
| [GTABOY](https://dexscreener.com/solana/apy5xjtrfcgymcenh7nqujdjkwjtau4p7vfxrhbg9znp) GTA IN REAL LIFE | Markt-Filter: Liquidität 6403$ | 6'403 $ | 9'879 $ | 2026-11-11 |
| [GTA6MAS](https://dexscreener.com/solana/cmnkx12v3w9tybs36poqalq9486gcbfvggxxmxuwfqj5) GTA6MAS | Markt-Filter: Liquidität 14006$ | 14'006 $ | 29'780 $ | 2026-11-11 |
