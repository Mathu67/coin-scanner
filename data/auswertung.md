# Coin-Scanner – Auswertung

_Stand: 2026-11-11 01:02 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **7.6 Tagen**, **96 Coins** gekauft (Einsatz 960.00 Fr.)
- Status Regel A: 6 bei 4x verkauft, 48 tot, 42 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 476.63 Fr. | **-483.37 Fr.** | -50 % |
| B: Hälfte bei 4x, Rest läuft | 512.96 Fr. | **-447.04 Fr.** | -47 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 530.16 Fr. | **-429.84 Fr.** | -45 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **46 Coins seit Start von Regel D** (Einsatz 460.00 Fr.):
  - A: **-197.41 Fr.** (-43 %)
  - B: **-222.92 Fr.** (-48 %)
  - C: **-230.80 Fr.** (-50 %)
  - D: **-135.34 Fr.** (-29 %)

D abgeschlossen: Stop-Loss 32x, Trailing-Stop 1x, tot 3x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 54 Coins, **-284.80 Fr.** (-53 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 22 von 96 (23 %)
- Mindestens 4x erreicht: 6 von 96 (6 %)
- Mindestens 10x erreicht: 3 von 96 (3 %)
- Auf -95 % oder Liquidität weg (tot): 48 von 96 (50 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -419.46 Fr. | -44 % |
| alles bei 3x | -479.37 Fr. | -50 % |
| alles bei 4x | -497.55 Fr. | -52 % |
| alles bei 5x | -527.77 Fr. | -55 % |
| alles bei 10x | -435.52 Fr. | -45 % |
| alles bei 20x | -451.50 Fr. | -47 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 15.60 Fr. | 10.6x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 41.16 Fr. | 10.1x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: verkauft | 29.83 Fr. | 12.58 Fr. | 4.8x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: offen, B: offen | 29.41 Fr. | 23.63 Fr. | 3.3x |
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
| [GTA 6](https://dexscreener.com/solana/ejggrdtfiyrxs2nkvchsyxtlof9pwo41q9vznvjrkcgf) GTA 6 | Markt-Filter: zu jung | 0 $ | 2'345 $ | 2026-11-11 |
| [$GTA6](https://dexscreener.com/solana/c1mlhwpxczcxgav6nxxefwyuyy5g9rcenjbypglmcdnr) GTA6 | Markt-Filter: zu jung | 0 $ | 639 $ | 2026-11-10 |
| [ROCCO](https://dexscreener.com/solana/7af8rgiehaxc7adxqb9caqcgnvt88axzk8f3zg5fqfnv) GTA6 DOG | Markt-Filter: zu alt | 0 $ | 8'708 $ | 2026-11-10 |
| [GTASCII](https://dexscreener.com/solana/7ardrnamsxlqufjkhgydl4veqq4qrgmkxap35hfe9bhg) Grand Text ASCII | Markt-Filter: zu jung | 0 $ | 3'336 $ | 2026-11-10 |
| [GTAX](https://dexscreener.com/solana/b9n7gy5vcystzxu3hpf2gozeggu2qigutwykef7txzvq) Grand Theft Auto X | Markt-Filter: zu jung | 1'568'385 $ | 1'637'737 $ | 2026-11-10 |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) GTAVI AudaCity | Markt-Filter: zu jung | 107'189 $ | 1'851'730 $ | 2026-11-10 |
| [DacityCoin](https://dexscreener.com/solana/5jgtzoj1fhv1ttkp8nqcbaexmwnztbhtzjajqtl585zd) ROCKSTAR TRAILER AUDACITY | Markt-Filter: Liquidität 0$ | 0 $ | 2'317 $ | 2026-11-10 |
| [Before](https://dexscreener.com/solana/7yqg7rlnvf4pc6scx4gckqpfrvmfms2bxjtwztqxyw64) Before GTA 6 | Markt-Filter: Liquidität 0$ | 0 $ | 4'757 $ | 2026-11-10 |
| [GTA](https://dexscreener.com/solana/vvlnpbvdrrdh5z3zh4bn4oyf5up3tbduthpjdow9zf1) Grand Theft America | Markt-Filter: Liquidität 0$ | 0 $ | 3'278 $ | 2026-11-10 |
| [gta6](https://dexscreener.com/solana/2kicm3f2sguw2gznpvrkj6wzwjkkkxddyv7q6gfi45ak) gta 6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'330 $ | 2026-11-10 |
| [$GTA6](https://dexscreener.com/solana/5k1p5ykgqmu4nh67lvajwrkuwujenq76xgczzguwcicn) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 60 $ | 2026-11-10 |
| [WNTDDG GTA](https://dexscreener.com/solana/9anbun9pidak3rrtdflw9ce6cnrmswozzkybqgqktjxj) Wanted Dog | Markt-Filter: Liquidität 0$ | 0 $ | 27 $ | 2026-11-10 |
| [GTCM](https://dexscreener.com/solana/5uirmf5wblsbxpx2za8p9ksfaay7aychsoqdzcyrptki) GTA CAT MAYHEM | Markt-Filter: Liquidität 0$ | 0 $ | 1'155 $ | 2026-11-10 |
| [GTA 6](https://dexscreener.com/solana/an97u6gmthed1mymro2x9gyu62wktzfyu1ybahihyn5n) GTA 6 Updates | Markt-Filter: Liquidität 1525$ | 1'525 $ | 1'491 $ | 2026-11-10 |
| [ANT](https://dexscreener.com/solana/bivbn5dk1bjbk9sgasy4uziuh98pdsceqwnofxurywgf) Anthropic | Markt-Filter: Liquidität 0$ | 0 $ | 2'337 $ | 2026-11-10 |
| [GTAVI](https://dexscreener.com/solana/adny4gknyqeruieyykqmxb3t1qceufogoao1pmceqeux) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 610 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/d4rug4cgsgqf2kugvbzcl9abbn743v2hqgbchvf2nkqy) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [CTA](https://dexscreener.com/solana/5cfxror3c1dc4grpqapudio4sh4wrkvnfca6sotbuhuc) CLAUDE THE ALLIGATOR | Markt-Filter: Liquidität 0$ | 0 $ | 2'401 $ | 2026-11-10 |
| [CLAUDE](https://dexscreener.com/solana/rzpgi3firhb7wkmtbznmvhuu2rc6c2wibjsjz5r1w7b) Claude The Alligator | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA4](https://dexscreener.com/solana/gflwdv18d7q8j1vbxuvpk4rayesrkf7fevzzlprj66ga) GTA IV | Markt-Filter: Liquidität 12450$ | 12'450 $ | 6'408 $ | 2026-11-10 |
| [Anthropic](https://dexscreener.com/solana/8npwyqgvv2z3pauiy8ydswqp3qim8amnm3hkuulsltnv) Anthropic Coin | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-10 |
| [GTA6](https://dexscreener.com/solana/fqqsjjtuhs3go7ponkgmrccwhkfot72knvneotgpvq9q) GTA VI | Markt-Filter: Liquidität 1566$ | 1'566 $ | 1'535 $ | 2026-11-10 |
| [GTAPE](https://dexscreener.com/solana/hmaehlol5khrbo1mdfdwndzq1degt5whpyyqn6phjqdo) GTAPE | Markt-Filter: Liquidität 0$ | 0 $ | 2'497 $ | 2026-11-09 |
| [GTFLOPPA](https://dexscreener.com/solana/lkre6pa2mxlvjixub7m5fowsivhpxgqkzt2d5y3p3ts) Grand Theft Floppa | Markt-Filter: Liquidität 0$ | 0 $ | 2'312 $ | 2026-11-09 |
| [$GTAINU](https://dexscreener.com/solana/7x7r2safcabbefphfucmjrvqxipanpa1rgs2mudy1pyr) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'421 $ | 2026-11-09 |
| [CLAUDEBOT](https://dexscreener.com/solana/acmjwv27qkaaxrrjfu6dfd1qsbcebn5u5s5acjatygof) CLAUDEBOT | Markt-Filter: Liquidität 0$ | 0 $ | 537 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/bkfysyujwx53rjumnbdue7madpe8uoscubfuz4hqtccg) Grand Theft Alice | Markt-Filter: Liquidität 1712$ | 1'712 $ | 1'597 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/9cp73nuksvjwhxvjqvw3v3xo6ymcs7akba6twcaeatjz) Grand Titty Army | Markt-Filter: Liquidität 1602$ | 1'602 $ | 1'519 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/8jpzwhv4kdzp6qqsztexm8pycxhrxaq5tkdg5qpr6zwi) GTA Trump | Markt-Filter: Liquidität 2030$ | 2'030 $ | 1'820 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/f66uvpj1bpqrknxe99bjtuqmg9smipnprqirue96ycfg) Grand Theft Apes | Sicherheits-Filter: Top-10 halten 27% | 27'524 $ | 128'493 $ | 2026-11-09 |
| [PETA](https://dexscreener.com/solana/9jwibvsonp2ab2zaf76ryycgiqucw2xf8jcb9dpcjkhh) Pepetide GTA | Markt-Filter: Liquidität 1867$ | 1'867 $ | 1'690 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fmyuqpjprnbycasqdz6hf2mulmjbuu6rjvt8mse8vky4) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 823 $ | 2026-11-09 |
| [GTABABY](https://dexscreener.com/solana/fzzrktr3yv37dmkq9w862xykthzbcjddjjnbaoabau5n) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 352 $ | 2026-11-09 |
| [GTAVICAT](https://dexscreener.com/solana/g1gw9p4uzhu655rg54ccas4ukjv7af7nrf5cfikzkcud) GTAVICAT | Markt-Filter: Liquidität 0$ | 0 $ | 2'405 $ | 2026-11-09 |
| [Gasgolem](https://dexscreener.com/solana/8tjxcyftfnzwx7e8rxtj51ypvqfgzlzqgsxylohekg3c) ANTHROPIC GAS GOLEM | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-09 |
| [GTA6](https://dexscreener.com/solana/5rjazs9pwatf2gc9hxj2seutww57q1aygdja9ufzb2h6) GTA VI | Markt-Filter: Liquidität 1578$ | 1'578 $ | 1'545 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/ggu7zxbz9nbens18erttk9p1yrrsyo2a5kwrvbbrzrix) Gta | Markt-Filter: Liquidität 0$ | 0 $ | 2'453 $ | 2026-11-09 |
| [ANT](https://dexscreener.com/solana/ce9qsaao9tiztoco4j8a84hc48o1r17anpufnzm1bqic) Anthropic | Sicherheits-Filter: Top-10 halten 26% | 67'912 $ | 116'543 $ | 2026-11-09 |
| [GTA6KODAK](https://dexscreener.com/solana/bkaagfumhqvgxa3bqzyabmibsmvietuiapu95prauhx7) GTA6 KODAK BLACK | Sicherheits-Filter: Top-10 halten 42% | 26'640 $ | 124'044 $ | 2026-11-09 |
| [AGTA6](https://dexscreener.com/solana/7tmyzu5blnzzapuvynrzaupjhmjd1draq6caan4mrzvf) after GTA 6 | Markt-Filter: zu alt | 0 $ | 11'888 $ | 2026-11-08 |
