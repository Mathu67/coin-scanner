# Coin-Scanner – Auswertung

_Stand: 2026-11-12 11:51 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **9.1 Tagen**, **115 Coins** gekauft (Einsatz 1'150.00 Fr.)
- Status Regel A: 9 bei 4x verkauft, 60 tot, 46 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 613.51 Fr. | **-536.49 Fr.** | -47 % |
| B: Hälfte bei 4x, Rest läuft | 608.04 Fr. | **-541.96 Fr.** | -47 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 605.56 Fr. | **-544.44 Fr.** | -47 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **65 Coins seit Start von Regel D** (Einsatz 650.00 Fr.):
  - A: **-248.92 Fr.** (-38 %)
  - B: **-316.25 Fr.** (-49 %)
  - C: **-324.53 Fr.** (-50 %)
  - D: **-216.88 Fr.** (-33 %)

D abgeschlossen: Stop-Loss 44x, Trailing-Stop 1x, tot 5x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 69 Coins, **-301.86 Fr.** (-44 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 27 von 115 (23 %)
- Mindestens 4x erreicht: 9 von 115 (8 %)
- Mindestens 10x erreicht: 3 von 115 (3 %)
- Auf -95 % oder Liquidität weg (tot): 60 von 115 (52 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -494.17 Fr. | -43 % |
| alles bei 3x | -588.36 Fr. | -51 % |
| alles bei 4x | -570.88 Fr. | -50 % |
| alles bei 5x | -644.01 Fr. | -56 % |
| alles bei 10x | -564.56 Fr. | -49 % |
| alles bei 20x | -617.87 Fr. | -54 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [NOBUSHIBA](https://dexscreener.com/solana/dagau7g32pmkjf8ng2372xo2hygfgenx5yn7mwmkhfgf) | A: verkauft, B: verkauft | 43.40 Fr. | 27.71 Fr. | 6.7x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 13.34 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 25.57 Fr. | 10.1x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: offen, B: offen | 31.20 Fr. | 24.46 Fr. | 3.7x |
| [BORLY](https://dexscreener.com/solana/7xwnpcwt4upj2hyuff4czvmmsvvws13k1w8ip6y4o5zq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 35 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Genug Coins für eine brauchbare Einschätzung (kein Beweis).
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTAmeme](https://dexscreener.com/solana/c9etl7uz66lmgqgxc9u4ieudnnjyzimmzxi2hgfm9bik) GTA | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/5675urx53hj1uatagbki6ecp1rvddksffzx5hjj6nmaf) Claudecoin | Markt-Filter: zu jung | 0 $ | 1'555 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/ayvp8hu6xbkx3km6qgyfkfvz8t5umesjwhwdsodawrgt) Claudecoin | Markt-Filter: zu jung | 1'648 $ | 1'543 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/av8nnjo59e9qxmrsj7rncdfnwbjolc3w2w2k6x5etxew) Claudecoin | Markt-Filter: zu jung | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/djb2hkkmionjb4vu6paejrsomqgrf3c884vhfwecnthy) Claude the Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/aptfoegpup16qstekfwzvrygipzhvbmdl56ewmbdbytz) Claudecoin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CODE](https://dexscreener.com/solana/e1dvqdszz1eiisnlxachrqurtmsyjja9blc9at1jxzcv) Claude Code Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/76dhpzci994kcacipvwsyhjrqjgy5ewwqvq48wgfyzwi) Grand Theft Auto: Vice City | Markt-Filter: Liquidität 0$ | 0 $ | 3'520 $ | 2026-11-12 |
| [GTAV](https://dexscreener.com/solana/dlwbtq6srzsebme95k5perlzddnzpp3169fsofdy9aj7) Grand Theft Auto V | Markt-Filter: Liquidität 0$ | 0 $ | 3'046 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/gncawlgbkstxtxejfj6j68ns3wbir1w9qfdf4mg2kq9f) Grand Theft Auto VI | Markt-Filter: Liquidität 6$ | 6 $ | 5'830 $ | 2026-11-12 |
| [GTA 6.0](https://dexscreener.com/solana/bea4eet5lqvp4gdeb3mbqioo98t1kxr3sakueqpthgte) Grand Theft Auto VI | Markt-Filter: Liquidität 0$ | 0 $ | 17'048 $ | 2026-11-12 |
| [GTA6](https://dexscreener.com/solana/4vj3nrvxvedyepybojbt5hjoikxj62teac5uvrusyykk) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'338 $ | 2026-11-11 |
| [GTA6Dog](https://dexscreener.com/solana/9zrngpz8jjstjnppsj3edv8drmjxkuadcrz2v6pfqusx) Gta6 dog | Markt-Filter: Liquidität 0$ | 0 $ | 856 $ | 2026-11-11 |
| [GTA6TRUMP](https://dexscreener.com/solana/emp4rvcuuarfsxyxcxecrjeoshjwnmgprycdgzx5mnd8) GTATRUMP | Sicherheits-Filter: Risiko: Creator history of rugged tokens | 25'159 $ | 115'805 $ | 2026-11-11 |
| [GTAFEVER](https://dexscreener.com/solana/e2d5cqnag7knvrvorzghdfjbufwycqv9d3xxzfqy89if) GTA VI FEVER | Markt-Filter: Liquidität 0$ | 0 $ | 3'692 $ | 2026-11-11 |
| [GTA$](https://dexscreener.com/solana/3fbyy8s1zbqarqpxfeeamxlnuebuxjnk4gsqrgbq3nky) Grand Theft Auto Dollars | Markt-Filter: Liquidität 16462$ | 16'462 $ | 36'377 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/fednfeglt8zfmgh4wkwzenb8bvbc8a2uik3kvngv3mxc) Grab That Ass | Markt-Filter: Liquidität 1608$ | 1'608 $ | 1'543 $ | 2026-11-11 |
| [TGATO](https://dexscreener.com/solana/byecx7tv5vpjjkruoypctc92twfbpre2ktqck9xrkhar) Trevor GTA6CAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [DTA](https://dexscreener.com/solana/hmxcypmqv7qol5vb8gzjnr6axgt4n4pdcmxurx6ca2on) GTA Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'350 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/ga3bqrkhfq4c5eldamitpfue1gchaphyeubqkeshihvu) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/fas2rmsutcfcvg3zbngb7bm9zxtopazxrkvhcynn7dyo) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 1'363 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/6praz8pjaatsaxxzy6hoeavnhpxek7ww2r6kanudxubn) Grand Theft Agent | Markt-Filter: Liquidität 2349$ | 2'349 $ | 2'227 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/g7aswxsctw7phzw2bq8w2kljjfl2chgk66jwzc9st26p) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 6 $ | 2026-11-11 |
| [GTABOY](https://dexscreener.com/solana/apy5xjtrfcgymcenh7nqujdjkwjtau4p7vfxrhbg9znp) GTA IN REAL LIFE | Markt-Filter: Liquidität 8434$ | 8'434 $ | 15'467 $ | 2026-11-11 |
| [GTA6MAS](https://dexscreener.com/solana/cmnkx12v3w9tybs36poqalq9486gcbfvggxxmxuwfqj5) GTA6MAS | Markt-Filter: Liquidität 13183$ | 13'183 $ | 26'976 $ | 2026-11-11 |
| [GTA 6 Coin](https://dexscreener.com/solana/3imvopi4a16w67aqup6uxqymolreo47aqgmzsg25dkmg) GTA6 | Markt-Filter: Liquidität 1521$ | 1'521 $ | 1'495 $ | 2026-11-11 |
| [GTA 6](https://dexscreener.com/solana/ejggrdtfiyrxs2nkvchsyxtlof9pwo41q9vznvjrkcgf) GTA 6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'318 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/c1mlhwpxczcxgav6nxxefwyuyy5g9rcenjbypglmcdnr) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 639 $ | 2026-11-10 |
| [ROCCO](https://dexscreener.com/solana/7af8rgiehaxc7adxqb9caqcgnvt88axzk8f3zg5fqfnv) GTA6 DOG | Markt-Filter: zu alt | 0 $ | 8'708 $ | 2026-11-10 |
| [GTASCII](https://dexscreener.com/solana/7ardrnamsxlqufjkhgydl4veqq4qrgmkxap35hfe9bhg) Grand Text ASCII | Markt-Filter: Liquidität 0$ | 0 $ | 3'243 $ | 2026-11-10 |
| [GTAX](https://dexscreener.com/solana/b9n7gy5vcystzxu3hpf2gozeggu2qigutwykef7txzvq) Grand Theft Auto X | Sicherheits-Filter: Risiko: Low Liquidity | 15'983'996 $ | 16'373'434 $ | 2026-11-10 |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) GTAVI AudaCity | GEKAUFT (simuliert) | 114'321 $ | 2'091'693 $ | 2026-11-10 |
| [DacityCoin](https://dexscreener.com/solana/5jgtzoj1fhv1ttkp8nqcbaexmwnztbhtzjajqtl585zd) ROCKSTAR TRAILER AUDACITY | Markt-Filter: Liquidität 0$ | 0 $ | 2'317 $ | 2026-11-10 |
| [Before](https://dexscreener.com/solana/7yqg7rlnvf4pc6scx4gckqpfrvmfms2bxjtwztqxyw64) Before GTA 6 | Markt-Filter: Liquidität 0$ | 0 $ | 3'647 $ | 2026-11-10 |
| [GTA](https://dexscreener.com/solana/vvlnpbvdrrdh5z3zh4bn4oyf5up3tbduthpjdow9zf1) Grand Theft America | Markt-Filter: Liquidität 0$ | 0 $ | 3'173 $ | 2026-11-10 |
| [gta6](https://dexscreener.com/solana/2kicm3f2sguw2gznpvrkj6wzwjkkkxddyv7q6gfi45ak) gta 6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'330 $ | 2026-11-10 |
| [$GTA6](https://dexscreener.com/solana/5k1p5ykgqmu4nh67lvajwrkuwujenq76xgczzguwcicn) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 60 $ | 2026-11-10 |
| [WNTDDG GTA](https://dexscreener.com/solana/9anbun9pidak3rrtdflw9ce6cnrmswozzkybqgqktjxj) Wanted Dog | Markt-Filter: Liquidität 0$ | 0 $ | 27 $ | 2026-11-10 |
| [GTCM](https://dexscreener.com/solana/5uirmf5wblsbxpx2za8p9ksfaay7aychsoqdzcyrptki) GTA CAT MAYHEM | Markt-Filter: Liquidität 0$ | 0 $ | 1'155 $ | 2026-11-10 |
| [GTA 6](https://dexscreener.com/solana/an97u6gmthed1mymro2x9gyu62wktzfyu1ybahihyn5n) GTA 6 Updates | Markt-Filter: Liquidität 1530$ | 1'530 $ | 1'496 $ | 2026-11-10 |
