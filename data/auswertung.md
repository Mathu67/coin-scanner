# Coin-Scanner – Auswertung

_Stand: 2026-11-14 15:02 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **11.2 Tagen**, **146 Coins** gekauft (Einsatz 1'460.00 Fr.)
- Status Regel A: 12 bei 4x verkauft, 81 tot, 53 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 782.94 Fr. | **-677.06 Fr.** | -46 % |
| B: Hälfte bei 4x, Rest läuft | 769.25 Fr. | **-690.75 Fr.** | -47 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 732.44 Fr. | **-727.56 Fr.** | -50 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **96 Coins seit Start von Regel D** (Einsatz 960.00 Fr.):
  - A: **-384.84 Fr.** (-40 %)
  - B: **-460.38 Fr.** (-48 %)
  - C: **-505.68 Fr.** (-53 %)
  - D: **-336.92 Fr.** (-35 %)

D abgeschlossen: Stop-Loss 71x, Trailing-Stop 2x, Zeit-Stop 2x, tot 6x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 93 Coins, **-423.64 Fr.** (-46 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 33 von 146 (23 %)
- Mindestens 4x erreicht: 12 von 146 (8 %)
- Mindestens 10x erreicht: 3 von 146 (2 %)
- Auf -95 % oder Liquidität weg (tot): 81 von 146 (55 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -658.42 Fr. | -45 % |
| alles bei 3x | -751.25 Fr. | -51 % |
| alles bei 4x | -714.43 Fr. | -49 % |
| alles bei 5x | -755.88 Fr. | -52 % |
| alles bei 10x | -759.89 Fr. | -52 % |
| alles bei 20x | -822.18 Fr. | -56 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [NOBUSHIBA](https://dexscreener.com/solana/dagau7g32pmkjf8ng2372xo2hygfgenx5yn7mwmkhfgf) | A: verkauft, B: verkauft | 43.40 Fr. | 10.08 Fr. | 6.7x |
| [BRUH](https://dexscreener.com/solana/ehpzesdxtymvwz1iy5nt3lrnjy1xbc1kgqspl1kqnyiv) | A: verkauft, B: offen | 41.53 Fr. | 30.99 Fr. | 5.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 12.08 Fr. | 10.6x |
| [HWAN](https://dexscreener.com/solana/54gedrrdayfg4zcavcrymcvvzzfmeak3luwhr7q8qwi1) | A: verkauft, B: offen | 34.12 Fr. | 23.93 Fr. | 4.2x |
| [DACITY](https://dexscreener.com/solana/89rsdzz3wncebojfruvi6omxbdytnrelfvqcvq1ophnq) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.2x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |
| [NATF](https://dexscreener.com/solana/gfdksknxksjeddbc1hzwbz2q5kqur6xdv5q9w5ltjdxm) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.6x |

Der beste Coin macht 27 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Genug Coins für eine brauchbare Einschätzung (kein Beweis).
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [Ballfin](https://dexscreener.com/solana/fgrbdrfdet7yupgrxi9gchuazu3nnzscjrfjtxnj4rtu) GTA 6 Lottery | Markt-Filter: zu jung | 1'465 $ | 1'391 $ | 2026-11-14 |
| [GTAVIME](https://dexscreener.com/solana/axm4amdhz5ndfsrhg2chfeo9ihxjrz5rvryn2aeju6x) Official GTA VI MEME | Markt-Filter: zu jung | 0 $ | 6'067 $ | 2026-11-14 |
| [GTV](https://dexscreener.com/solana/5amfpag6wqxj1cchjnddyv3pe27dcghlxhmzklrdhcob) Grand Theft Vi | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-14 |
| [AIRDROP](https://dexscreener.com/solana/89zgxm7rlst8aejqrxwsurfxu78q8m8pkjp5xtzbgjpa) GTA AIRDROP | Markt-Filter: zu jung | 0 $ | 5'095 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/9vowgbh1dbyhbhabkratwvpmg473pkz9dqrn75nlxbjy) GTA Dollars | Markt-Filter: zu jung | 0 $ | 17 $ | 2026-11-14 |
| [AIRDROP](https://dexscreener.com/solana/cqnpzpwr9u4ira6ufk1sffc7j3tjmcqm8hr8wr4s431b) GTA AIRDROP  | Markt-Filter: zu jung | 0 $ | 5'093 $ | 2026-11-14 |
| [GTA6](https://dexscreener.com/solana/3n61faw8aunetycbsyh8vboxfqlaqet1qcvibrhrlfam) GTA 6 | Markt-Filter: zu alt | 0 $ | 30'339 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/j6x41etxgh3v9cugedels5hfvdmrt5v7nzdgijngrgdp) GTA Dollars | Markt-Filter: zu jung | 0 $ | 0 $ | 2026-11-14 |
| [GTA6](https://dexscreener.com/solana/8zyfak1zokurd5quoyptmwzztx4osv9myssljao3jyaf) Grand Theft Auto VI | Markt-Filter: Liquidität 12665$ | 12'665 $ | 33'383 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/bivxozcepwrkukmngbd5qxnwxtgjjlphhb6jxgavbmsy) GTA Dollars | Markt-Filter: zu jung | 61'051 $ | 367'027 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/efhuwhfyqef9l3dhdepsb72wapqwndukcuqozpvjgv6n) GTA Dollar | Markt-Filter: zu jung | 10'254 $ | 15'100 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/azmnhupgr1teo7kxjennqusdeqmo8i9grazzy5nqrwq) GTA Dollar | Markt-Filter: zu jung | 0 $ | 3'066 $ | 2026-11-14 |
| [GTA 6 CHAIR](https://dexscreener.com/solana/4h7drc3kxwx2v1qhk7cnnms8vfr34ku5kovmtww3fokd) GTA6 GAMING CHAIR | Markt-Filter: Liquidität 0$ | 0 $ | 2'100 $ | 2026-11-14 |
| [GTA$](https://dexscreener.com/solana/dysgo2qeie4hm7geajycqq9dccmo9qkknywhequskgvj) GTA Dollars | Markt-Filter: zu alt | 7'467 $ | 10'111 $ | 2026-11-14 |
| [GTA6](https://dexscreener.com/solana/gdw7sl5n7ehjmqgbkkwtm3ygybhomlwhi4pzpsfgbqnr) Before GTA 6 | Markt-Filter: Liquidität 0$ | 0 $ | 16 $ | 2026-11-13 |
| [Ballfin](https://dexscreener.com/solana/eigncpkyjhevjzc5kbihkvtcexbhagbx4dpcy47tcp87) GTA 6  Ballfin | Markt-Filter: Liquidität 1611$ | 1'611 $ | 1'488 $ | 2026-11-13 |
| [GTAI](https://dexscreener.com/solana/7egl1xiruwptp3qhsv4lgf61rtyejejubdrm8bhqrf2n) Grand Theft Anarchy | Markt-Filter: Liquidität 0$ | 0 $ | 2'333 $ | 2026-11-13 |
| [GTA](https://dexscreener.com/solana/cwjz5zcytxjtvep1c5yabc2mpuzqwzy7borubks6c3bf) GrandTheftCrypto | Markt-Filter: Liquidität 2668$ | 2'668 $ | 2'834 $ | 2026-11-13 |
| [GTAMAS](https://dexscreener.com/solana/cldvsvn8qedpdm5rpyxn8ebzu5vntbtuqqciro9r59qi) GTAMAS | Markt-Filter: Liquidität 3467$ | 3'467 $ | 3'509 $ | 2026-11-13 |
| [ATHX](https://dexscreener.com/solana/c8xhp7vjdiwqn4xfsz9skazwsvcyz2quww76miqmrqva) Anthropic ETF | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-13 |
| [BEFORE](https://dexscreener.com/solana/j6mufxypbyaw9h835gjruzbznsclvxwv6bl2h2jvarjm) Before GTA 7 | Markt-Filter: Liquidität 0$ | 0 $ | 3'068 $ | 2026-11-13 |
| [GTAhouse](https://dexscreener.com/solana/cjppvtccatfxm2elmkugjs3jyt68oznlpw7yug3bjtbi) GTAhouse | Markt-Filter: zu jung | 8'938 $ | 14'781 $ | 2026-11-13 |
| [rockstar](https://dexscreener.com/solana/8rfudmcvffkk26kcm5ctshpjv53pmzga7p2ldxnjjgjq) rockstar | Markt-Filter: Liquidität 12698$ | 12'698 $ | 24'851 $ | 2026-11-13 |
| [GENNY](https://dexscreener.com/solana/cr7e76mcnt1kzemtyeah6fngqmecahc8uru8wnidj6m3) Generational Wealth Before GTA 6 | Markt-Filter: Liquidität 1613$ | 1'613 $ | 1'551 $ | 2026-11-13 |
| [WHEEL](https://dexscreener.com/solana/8zrewonvgwwk3srdzrd2h6d5ugujuhs21mubsvdy1epq) GTA Wheel | Markt-Filter: Liquidität 0$ | 0 $ | 2'165 $ | 2026-11-13 |
| [GTA](https://dexscreener.com/solana/12tbmwesau4zycdym7mlnzz3qtec4a67qesj9rf7xmw2) Grand Titty Affair | Markt-Filter: Liquidität 1698$ | 1'698 $ | 1'598 $ | 2026-11-13 |
| [GTA](https://dexscreener.com/solana/erar47r3czkgzmqkrjdebruaxwm84qrqmteuds7dzpdy) Grand Third Affair | Markt-Filter: Liquidität 0$ | 0 $ | 2'238 $ | 2026-11-13 |
| [gta6](https://dexscreener.com/solana/2x9cm6mnejwbzakggzumpsxzvkfr1782zcteta1ufdzt) Lucia | Markt-Filter: Liquidität 0$ | 0 $ | 434 $ | 2026-11-13 |
| [GTA](https://dexscreener.com/solana/hy5savp4t8i8skmwlnwwgmzqnmhyucxai57a5hjqvga) Grand Trench Auto | Markt-Filter: Liquidität 0$ | 0 $ | 2'247 $ | 2026-11-13 |
| [VI](https://dexscreener.com/solana/ebypqwwe1w8cmqcm2or9ixzvs9zhavc9cptklwpse31a) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 1'440 $ | 2026-11-13 |
| [BUX](https://dexscreener.com/solana/aodq34rjcjuszkdk2hnnj8sloadwfboe52fb1sc3xnpw) Grand Theft Agents | Markt-Filter: Liquidität 0$ | 0 $ | 3'938 $ | 2026-11-13 |
| [ROCCO](https://dexscreener.com/solana/2cv9fs87aiwrcgnxbeghxkbfajx8mi2mywsqxrsayvui) Rocco GTA VI Dog | Markt-Filter: Liquidität 0$ | 0 $ | 4'368 $ | 2026-11-13 |
| [GTAINU](https://dexscreener.com/solana/9cggxyegoygqf8rf7su6ktwtoqlsnxmnp6bd8u5ohvwf) GTA Inu | Markt-Filter: Liquidität 1562$ | 1'562 $ | 1'481 $ | 2026-11-13 |
| [GTATRENCH](https://dexscreener.com/solana/4trg9bpje6khpivk5jdf5eds3sckfptfqn4dfxrgdtus) GTA TRENCH | Markt-Filter: Liquidität 0$ | 0 $ | 2'281 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/bypyjk9gcsa5moeoagqbrfubqix8cqn44slp3rkic3ns) Girls Throwing Ass | Markt-Filter: Liquidität 0$ | 0 $ | 2'269 $ | 2026-11-12 |
| [GTAMAS](https://dexscreener.com/solana/atbnegfn2pzxm6vndmugwv4o51yzdm76rfjeofslibgg) GTAMAS | Markt-Filter: Liquidität 0$ | 0 $ | 4'108 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/2y1xtb5vjcrmabkfupnygkh68yzjhx3xkrd8es9z2e2z) VICE CITY | Markt-Filter: Liquidität 0$ | 0 $ | 59 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/8h16btmaedxzqyoxdwlt2znrj4gc8kw6nkjaigatgapr) Girls Throwing Ass | Markt-Filter: Liquidität 2$ | 2 $ | 30'193 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/d3thivp3fdwktx6x9tlp7ka11wfflt5pxdofhr1wfxwt) Giant Thick Ass | Markt-Filter: Liquidität 0$ | 0 $ | 2'279 $ | 2026-11-12 |
| [GTA](https://dexscreener.com/solana/3ktr4wufbveklrcezwg4vgvrqasagzqxodck3evkd792) Grand Theft Affair | Markt-Filter: Liquidität 1681$ | 1'681 $ | 1'545 $ | 2026-11-12 |
