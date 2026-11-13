# Coin-Scanner – Auswertung

_Stand: 2026-11-13 00:00 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **9.6 Tagen**, **120 Coins** gekauft (Einsatz 1'200.00 Fr.)
- Status Regel A: 10 bei 4x verkauft, 68 tot, 42 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 625.13 Fr. | **-574.87 Fr.** | -48 % |
| B: Hälfte bei 4x, Rest läuft | 618.74 Fr. | **-581.26 Fr.** | -48 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 616.43 Fr. | **-583.57 Fr.** | -49 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **70 Coins seit Start von Regel D** (Einsatz 700.00 Fr.):
  - A: **-280.08 Fr.** (-40 %)
  - B: **-348.32 Fr.** (-50 %)
  - C: **-367.66 Fr.** (-53 %)
  - D: **-232.39 Fr.** (-33 %)

D abgeschlossen: Stop-Loss 50x, Trailing-Stop 1x, tot 6x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 78 Coins, **-352.66 Fr.** (-45 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 29 von 120 (24 %)
- Mindestens 4x erreicht: 10 von 120 (8 %)
- Mindestens 10x erreicht: 3 von 120 (2 %)
- Auf -95 % oder Liquidität weg (tot): 68 von 120 (57 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -519.72 Fr. | -43 % |
| alles bei 3x | -633.30 Fr. | -53 % |
| alles bei 4x | -610.17 Fr. | -51 % |
| alles bei 5x | -680.60 Fr. | -57 % |
| alles bei 10x | -625.46 Fr. | -52 % |
| alles bei 20x | -669.68 Fr. | -56 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [NOBUSHIBA](https://dexscreener.com/solana/dagau7g32pmkjf8ng2372xo2hygfgenx5yn7mwmkhfgf) | A: verkauft, B: verkauft | 43.40 Fr. | 14.77 Fr. | 6.7x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 13.04 Fr. | 10.6x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: verkauft, B: offen | 36.86 Fr. | 26.66 Fr. | 4.1x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 29.93 Fr. | 10.1x |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |
| [NATF](https://dexscreener.com/solana/gfdksknxksjeddbc1hzwbz2q5kqur6xdv5q9w5ltjdxm) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |

Der beste Coin macht 32 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Genug Coins für eine brauchbare Einschätzung (kein Beweis).
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTATRENCH](https://dexscreener.com/solana/4trg9bpje6khpivk5jdf5eds3sckfptfqn4dfxrgdtus) GTA TRENCH | Markt-Filter: zu jung | 0 $ | 2'281 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/bypyjk9gcsa5moeoagqbrfubqix8cqn44slp3rkic3ns) Girls Throwing Ass | Markt-Filter: zu jung | 0 $ | 2'283 $ | 2026-11-12 |
| [GTAMAS](https://dexscreener.com/solana/atbnegfn2pzxm6vndmugwv4o51yzdm76rfjeofslibgg) GTAMAS | Markt-Filter: zu jung | 0 $ | 4'034 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/2y1xtb5vjcrmabkfupnygkh68yzjhx3xkrd8es9z2e2z) VICE CITY | Markt-Filter: zu jung | 0 $ | 59 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/8h16btmaedxzqyoxdwlt2znrj4gc8kw6nkjaigatgapr) Girls Throwing Ass | Markt-Filter: zu jung | 1 $ | 1'939'940 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/d3thivp3fdwktx6x9tlp7ka11wfflt5pxdofhr1wfxwt) Giant Thick Ass | Markt-Filter: zu jung | 0 $ | 2'279 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/3ktr4wufbveklrcezwg4vgvrqasagzqxodck3evkd792) Grand Theft Affair | Markt-Filter: Liquidität 1701$ | 1'701 $ | 1'564 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/8hayj1ynkzqmfjwx74pwdku3m3wln8t5sxmt8895suv) Claude Cat | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTA Six](https://dexscreener.com/solana/av2bymmsfsfnvtgdmkzgtnsg9e8mzcowsmm6ihsnkklk) Grand Theft Auto VI | Markt-Filter: Liquidität 1641$ | 1'641 $ | 1'535 $ | 2026-11-12 |
| [ANTHROPE](https://dexscreener.com/solana/bnckk6axyhlyex6mwu8nvtigsdjchnlhlcf5itiqupvn) Anthropic Pepe | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTAmeme](https://dexscreener.com/solana/c9etl7uz66lmgqgxc9u4ieudnnjyzimmzxi2hgfm9bik) GTA | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/5675urx53hj1uatagbki6ecp1rvddksffzx5hjj6nmaf) Claudecoin | Markt-Filter: Liquidität 0$ | 0 $ | 1'555 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/ayvp8hu6xbkx3km6qgyfkfvz8t5umesjwhwdsodawrgt) Claudecoin | Markt-Filter: Liquidität 1628$ | 1'628 $ | 1'523 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/av8nnjo59e9qxmrsj7rncdfnwbjolc3w2w2k6x5etxew) Claudecoin | Markt-Filter: Liquidität 0$ | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/djb2hkkmionjb4vu6paejrsomqgrf3c884vhfwecnthy) Claude the Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CLAUDE](https://dexscreener.com/solana/aptfoegpup16qstekfwzvrygipzhvbmdl56ewmbdbytz) Claudecoin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [CODE](https://dexscreener.com/solana/e1dvqdszz1eiisnlxachrqurtmsyjja9blc9at1jxzcv) Claude Code Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/76dhpzci994kcacipvwsyhjrqjgy5ewwqvq48wgfyzwi) Grand Theft Auto: Vice City | Markt-Filter: Liquidität 0$ | 0 $ | 3'106 $ | 2026-11-12 |
| [GTAV](https://dexscreener.com/solana/dlwbtq6srzsebme95k5perlzddnzpp3169fsofdy9aj7) Grand Theft Auto V | Markt-Filter: Liquidität 0$ | 0 $ | 3'046 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/gncawlgbkstxtxejfj6j68ns3wbir1w9qfdf4mg2kq9f) Grand Theft Auto VI | Markt-Filter: Liquidität 6$ | 6 $ | 5'830 $ | 2026-11-12 |
| [GTA 6.0](https://dexscreener.com/solana/bea4eet5lqvp4gdeb3mbqioo98t1kxr3sakueqpthgte) Grand Theft Auto VI | Markt-Filter: Liquidität 10397$ | 10'397 $ | 23'215 $ | 2026-11-12 |
| [GTA6](https://dexscreener.com/solana/4vj3nrvxvedyepybojbt5hjoikxj62teac5uvrusyykk) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'338 $ | 2026-11-11 |
| [GTA6Dog](https://dexscreener.com/solana/9zrngpz8jjstjnppsj3edv8drmjxkuadcrz2v6pfqusx) Gta6 dog | Markt-Filter: Liquidität 0$ | 0 $ | 856 $ | 2026-11-11 |
| [GTA6TRUMP](https://dexscreener.com/solana/emp4rvcuuarfsxyxcxecrjeoshjwnmgprycdgzx5mnd8) GTATRUMP | Sicherheits-Filter: Risiko: Creator history of rugged tokens | 25'159 $ | 115'805 $ | 2026-11-11 |
| [GTAFEVER](https://dexscreener.com/solana/e2d5cqnag7knvrvorzghdfjbufwycqv9d3xxzfqy89if) GTA VI FEVER | Markt-Filter: Liquidität 0$ | 0 $ | 3'633 $ | 2026-11-11 |
| [GTA$](https://dexscreener.com/solana/3fbyy8s1zbqarqpxfeeamxlnuebuxjnk4gsqrgbq3nky) Grand Theft Auto Dollars | Markt-Filter: Liquidität 15069$ | 15'069 $ | 31'191 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/fednfeglt8zfmgh4wkwzenb8bvbc8a2uik3kvngv3mxc) Grab That Ass | Markt-Filter: Liquidität 1608$ | 1'608 $ | 1'543 $ | 2026-11-11 |
| [TGATO](https://dexscreener.com/solana/byecx7tv5vpjjkruoypctc92twfbpre2ktqck9xrkhar) Trevor GTA6CAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [DTA](https://dexscreener.com/solana/hmxcypmqv7qol5vb8gzjnr6axgt4n4pdcmxurx6ca2on) GTA Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'350 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/ga3bqrkhfq4c5eldamitpfue1gchaphyeubqkeshihvu) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/fas2rmsutcfcvg3zbngb7bm9zxtopazxrkvhcynn7dyo) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 1'363 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/6praz8pjaatsaxxzy6hoeavnhpxek7ww2r6kanudxubn) Grand Theft Agent | Markt-Filter: Liquidität 2305$ | 2'305 $ | 2'187 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/g7aswxsctw7phzw2bq8w2kljjfl2chgk66jwzc9st26p) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 6 $ | 2026-11-11 |
| [GTABOY](https://dexscreener.com/solana/apy5xjtrfcgymcenh7nqujdjkwjtau4p7vfxrhbg9znp) GTA IN REAL LIFE | Markt-Filter: Liquidität 7459$ | 7'459 $ | 12'639 $ | 2026-11-11 |
| [GTA6MAS](https://dexscreener.com/solana/cmnkx12v3w9tybs36poqalq9486gcbfvggxxmxuwfqj5) GTA6MAS | Markt-Filter: Liquidität 12454$ | 12'454 $ | 24'584 $ | 2026-11-11 |
| [GTA 6 Coin](https://dexscreener.com/solana/3imvopi4a16w67aqup6uxqymolreo47aqgmzsg25dkmg) GTA6 | Markt-Filter: Liquidität 1521$ | 1'521 $ | 1'495 $ | 2026-11-11 |
| [GTA 6](https://dexscreener.com/solana/ejggrdtfiyrxs2nkvchsyxtlof9pwo41q9vznvjrkcgf) GTA 6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'318 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/c1mlhwpxczcxgav6nxxefwyuyy5g9rcenjbypglmcdnr) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 639 $ | 2026-11-10 |
| [ROCCO](https://dexscreener.com/solana/7af8rgiehaxc7adxqb9caqcgnvt88axzk8f3zg5fqfnv) GTA6 DOG | Markt-Filter: zu alt | 0 $ | 8'708 $ | 2026-11-10 |
| [GTASCII](https://dexscreener.com/solana/7ardrnamsxlqufjkhgydl4veqq4qrgmkxap35hfe9bhg) Grand Text ASCII | Markt-Filter: Liquidität 0$ | 0 $ | 3'243 $ | 2026-11-10 |
