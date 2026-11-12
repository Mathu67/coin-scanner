# Coin-Scanner – Auswertung

_Stand: 2026-11-12 06:03 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **8.9 Tagen**, **111 Coins** gekauft (Einsatz 1'110.00 Fr.)
- Status Regel A: 9 bei 4x verkauft, 57 tot, 45 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 611.73 Fr. | **-498.27 Fr.** | -45 % |
| B: Hälfte bei 4x, Rest läuft | 617.12 Fr. | **-492.88 Fr.** | -44 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 612.12 Fr. | **-497.88 Fr.** | -45 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **61 Coins seit Start von Regel D** (Einsatz 610.00 Fr.):
  - A: **-212.03 Fr.** (-35 %)
  - B: **-268.50 Fr.** (-44 %)
  - C: **-282.90 Fr.** (-46 %)
  - D: **-187.41 Fr.** (-31 %)

D abgeschlossen: Stop-Loss 42x, Trailing-Stop 1x, tot 5x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 66 Coins, **-272.38 Fr.** (-41 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 27 von 111 (24 %)
- Mindestens 4x erreicht: 9 von 111 (8 %)
- Mindestens 10x erreicht: 3 von 111 (3 %)
- Auf -95 % oder Liquidität weg (tot): 57 von 111 (51 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -460.37 Fr. | -41 % |
| alles bei 3x | -553.49 Fr. | -50 % |
| alles bei 4x | -532.66 Fr. | -48 % |
| alles bei 5x | -614.51 Fr. | -55 % |
| alles bei 10x | -515.91 Fr. | -46 % |
| alles bei 20x | -559.60 Fr. | -50 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [NOBUSHIBA](https://dexscreener.com/solana/dagau7g32pmkjf8ng2372xo2hygfgenx5yn7mwmkhfgf) | A: verkauft, B: offen | 54.25 Fr. | 37.91 Fr. | 6.2x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 13.47 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 29.89 Fr. | 10.1x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: offen, B: offen | 32.47 Fr. | 25.05 Fr. | 3.7x |
| [BORLY](https://dexscreener.com/solana/7xwnpcwt4upj2hyuff4czvmmsvvws13k1w8ip6y4o5zq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 33 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Genug Coins für eine brauchbare Einschätzung (kein Beweis).
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTAVI](https://dexscreener.com/solana/76dhpzci994kcacipvwsyhjrqjgy5ewwqvq48wgfyzwi) Grand Theft Auto: Vice City | Markt-Filter: zu jung | 0 $ | 5'406 $ | 2026-11-12 |
| [GTAV](https://dexscreener.com/solana/dlwbtq6srzsebme95k5perlzddnzpp3169fsofdy9aj7) Grand Theft Auto V | Markt-Filter: zu jung | 0 $ | 3'046 $ | 2026-11-12 |
| [GTAVI](https://dexscreener.com/solana/gncawlgbkstxtxejfj6j68ns3wbir1w9qfdf4mg2kq9f) Grand Theft Auto VI | Markt-Filter: zu jung | 12 $ | 11'780 $ | 2026-11-12 |
| [GTA 6.0](https://dexscreener.com/solana/bea4eet5lqvp4gdeb3mbqioo98t1kxr3sakueqpthgte) Grand Theft Auto VI | Markt-Filter: Liquidität 0$ | 0 $ | 17'209 $ | 2026-11-12 |
| [GTA6](https://dexscreener.com/solana/4vj3nrvxvedyepybojbt5hjoikxj62teac5uvrusyykk) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'338 $ | 2026-11-11 |
| [GTA6Dog](https://dexscreener.com/solana/9zrngpz8jjstjnppsj3edv8drmjxkuadcrz2v6pfqusx) Gta6 dog | Markt-Filter: Liquidität 0$ | 0 $ | 856 $ | 2026-11-11 |
| [GTA6TRUMP](https://dexscreener.com/solana/emp4rvcuuarfsxyxcxecrjeoshjwnmgprycdgzx5mnd8) GTATRUMP | Sicherheits-Filter: Risiko: Creator history of rugged tokens | 25'159 $ | 115'805 $ | 2026-11-11 |
| [GTAFEVER](https://dexscreener.com/solana/e2d5cqnag7knvrvorzghdfjbufwycqv9d3xxzfqy89if) GTA VI FEVER | Markt-Filter: Liquidität 0$ | 0 $ | 3'692 $ | 2026-11-11 |
| [GTA$](https://dexscreener.com/solana/3fbyy8s1zbqarqpxfeeamxlnuebuxjnk4gsqrgbq3nky) Grand Theft Auto Dollars | Markt-Filter: Liquidität 17132$ | 17'132 $ | 38'849 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/fednfeglt8zfmgh4wkwzenb8bvbc8a2uik3kvngv3mxc) Grab That Ass | Markt-Filter: Liquidität 1608$ | 1'608 $ | 1'543 $ | 2026-11-11 |
| [TGATO](https://dexscreener.com/solana/byecx7tv5vpjjkruoypctc92twfbpre2ktqck9xrkhar) Trevor GTA6CAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [DTA](https://dexscreener.com/solana/hmxcypmqv7qol5vb8gzjnr6axgt4n4pdcmxurx6ca2on) GTA Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'350 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/ga3bqrkhfq4c5eldamitpfue1gchaphyeubqkeshihvu) GTA 6 Coin | Markt-Filter: Liquidität 0$ | 0 $ | 2'343 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/fas2rmsutcfcvg3zbngb7bm9zxtopazxrkvhcynn7dyo) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 1'363 $ | 2026-11-11 |
| [GTA](https://dexscreener.com/solana/6praz8pjaatsaxxzy6hoeavnhpxek7ww2r6kanudxubn) Grand Theft Agent | Markt-Filter: Liquidität 2368$ | 2'368 $ | 2'247 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/g7aswxsctw7phzw2bq8w2kljjfl2chgk66jwzc9st26p) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 6 $ | 2026-11-11 |
| [GTABOY](https://dexscreener.com/solana/apy5xjtrfcgymcenh7nqujdjkwjtau4p7vfxrhbg9znp) GTA IN REAL LIFE | Markt-Filter: Liquidität 11992$ | 11'992 $ | 28'529 $ | 2026-11-11 |
| [GTA6MAS](https://dexscreener.com/solana/cmnkx12v3w9tybs36poqalq9486gcbfvggxxmxuwfqj5) GTA6MAS | Markt-Filter: Liquidität 12432$ | 12'432 $ | 24'218 $ | 2026-11-11 |
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
| [ANT](https://dexscreener.com/solana/bivbn5dk1bjbk9sgasy4uziuh98pdsceqwnofxurywgf) Anthropic | Markt-Filter: Liquidität 0$ | 0 $ | 2'337 $ | 2026-11-10 |
| [GTAVI](https://dexscreener.com/solana/adny4gknyqeruieyykqmxb3t1qceufogoao1pmceqeux) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 610 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/d4rug4cgsgqf2kugvbzcl9abbn743v2hqgbchvf2nkqy) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [CTA](https://dexscreener.com/solana/5cfxror3c1dc4grpqapudio4sh4wrkvnfca6sotbuhuc) CLAUDE THE ALLIGATOR | Markt-Filter: Liquidität 0$ | 0 $ | 2'401 $ | 2026-11-10 |
| [CLAUDE](https://dexscreener.com/solana/rzpgi3firhb7wkmtbznmvhuu2rc6c2wibjsjz5r1w7b) Claude The Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA4](https://dexscreener.com/solana/gflwdv18d7q8j1vbxuvpk4rayesrkf7fevzzlprj66ga) GTA IV | Markt-Filter: Liquidität 12349$ | 12'349 $ | 6'310 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/8npwyqgvv2z3pauiy8ydswqp3qim8amnm3hkuulsltnv) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
