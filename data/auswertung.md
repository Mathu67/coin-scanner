# Coin-Scanner – Auswertung

_Stand: 2026-11-09 05:36 UTC. Paper Trading, kein echtes Geld, Werte inkl. 4 % Kosten pro Kauf und Verkauf._

## Ergebnis

- Läuft seit **5.8 Tagen**, **82 Coins** gekauft (Einsatz 820.00 Fr.)
- Status Regel A: 6 bei 4x verkauft, 29 tot, 47 noch offen
- Noch offene Positionen sind mit dem letzten Kurs bewertet (nicht endgültig).

| Regel | Wert heute | Ergebnis | Rendite |
|---|---|---|---|
| A: alles bei 4x | 485.09 Fr. | **-334.91 Fr.** | -41 % |
| B: Hälfte bei 4x, Rest läuft | 535.55 Fr. | **-284.45 Fr.** | -35 % |
| C: Einsatz bei 2x raus, Rest ohne Stop | 532.25 Fr. | **-287.75 Fr.** | -35 % |

### Regel D: Verluste begrenzen, Gewinner laufen lassen

_Stop bei 0.6x, nach 48 h raus wenn unter Einstieg, bei 2x Einsatz zurück, Rest ohne Deckel, Trailing-Stop 50 % ab 5x. Nur für Coins ab Start von D, deshalb hier der Vergleich auf denselben Coins._

- Vergleich auf den **32 Coins seit Start von Regel D** (Einsatz 320.00 Fr.):
  - A: **-73.65 Fr.** (-23 %)
  - B: **-85.04 Fr.** (-27 %)
  - C: **-100.79 Fr.** (-31 %)
  - D: **-55.28 Fr.** (-17 %)

D abgeschlossen: Stop-Loss 23x

_Regel C gibt es seit 7.11.2026. Bei 50 älteren Coins ist C rückwirkend aus dem Höchststand geschätzt (Einsatz genau bei 2x raus, Rest bei 20x oder tot)._

_Korrigiert: Rocco: falscher Preis 43 $ (49'677x) am 7.11.2026. Position neu ab Einstieg bewertet._

Nur abgeschlossene Coins (Regel A, ohne offene): 35 Coins, **-107.74 Fr.** (-31 %)

## Wie oft steigt ein Coin?

- Mindestens 2x erreicht: 19 von 82 (23 %)
- Mindestens 4x erreicht: 6 von 82 (7 %)
- Mindestens 10x erreicht: 2 von 82 (2 %)
- Auf -95 % oder Liquidität weg (tot): 29 von 82 (35 %)

## Was wäre bei anderen Verkaufszielen gewesen?

_Näherung aus den Minutenpreisen: Wer das Ziel erreicht hat, gilt genau zum Ziel verkauft, alle anderen zu ihrem letzten Stand. Regel A oben kann leicht abweichen, weil sie zum tatsächlich beobachteten Kurs verkauft._

| Verkaufsziel | Ergebnis | Rendite |
|---|---|---|
| alles bei 2x | -320.65 Fr. | -39 % |
| alles bei 3x | -363.94 Fr. | -44 % |
| alles bei 4x | -349.09 Fr. | -43 % |
| alles bei 5x | -349.15 Fr. | -43 % |
| alles bei 10x | -278.41 Fr. | -34 % |
| alles bei 20x | -266.36 Fr. | -32 % |

## Beste und schlechteste Coins (Regel B)

| Coin | Status | Wert B | Wert C | Max. erreicht |
|---|---|---|---|---|
| [HIGH](https://dexscreener.com/solana/cqvmzmwdveufa5rzkubidyr4zmdqdpoljatsw6wgspmu) | A: verkauft, B: verkauft | 116.37 Fr. | 94.32 Fr. | 20.5x |
| [José](https://dexscreener.com/solana/cdpy6qhvhtn9dvjx1wjutdztzvmck5tfvnnxz51hdpry) | A: verkauft, B: verkauft | 40.63 Fr. | 18.36 Fr. | 10.6x |
| [0DAY](https://dexscreener.com/solana/6qlmg6pz7esjvz3i7mp4arqknlkdy4ncanzsu8nnnofa) | A: verkauft, B: offen | 37.67 Fr. | 26.93 Fr. | 5.3x |
| [WEALTH](https://dexscreener.com/solana/5n8v68fcantrqvaxzrmbryde5jflrgm65pffsmia6nro) | A: verkauft, B: verkauft | 33.55 Fr. | 26.79 Fr. | 9.9x |
| [PIRATE](https://dexscreener.com/solana/2ounpacqvbodqwj7ft6eghmcgsckpmrzaqn6a9vhkp6d) | A: verkauft, B: verkauft | 29.83 Fr. | 19.97 Fr. | 4.8x |
| [AMD](https://dexscreener.com/solana/e9wpfxjqvwvdjkculu2xs742t6ehbn2cnzv2ps24fz14) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.2x |
| [ORBIT](https://dexscreener.com/solana/ajt7zptztfeo9cqu8yuwddtmoah7bmyt7kmkmhombcne) | A: tot, B: tot | 0.02 Fr. | 0.02 Fr. | 1.0x |
| [AMD](https://dexscreener.com/solana/6zv8dyrdxh56au2ebhpzzbmkprp5ixbkprj7hb2pj3rr) | A: tot, B: tot | 0.01 Fr. | 0.01 Fr. | 1.1x |

Der beste Coin macht 40 % aller Gewinne aus (hoher Wert = Ergebnis hängt an einem einzigen Treffer).

## Aussagekraft

Erste Tendenz, aber noch nicht belastbar. Unter 100 Coins reicht ein einzelner Treffer, um alles zu drehen.
Grenzen der Simulation: Bei einem echten Rugpull zwischen zwei Kurs-Checks würde man schlechter aussteigen als hier. Echte Gebühren und Slippage bei Memecoins können auch über den angenommenen Kosten liegen. Der Kurs wird nur alle 60 Sekunden geprüft, Spitzen dazwischen fehlen.

## Coins mit Schlagwörtern (gta, grand theft, rockstar, claude, anthropic)

| Coin | Letzte Entscheidung | Liquidität | MCap | zuerst gesehen |
|---|---|---|---|---|
| [GTABABY](https://dexscreener.com/solana/fzzrktr3yv37dmkq9w862xykthzbcjddjjnbaoabau5n) GTA6 | Markt-Filter: zu jung | 0 $ | 352 $ | 2026-11-09 |
| [GTAVICAT](https://dexscreener.com/solana/g1gw9p4uzhu655rg54ccas4ukjv7af7nrf5cfikzkcud) GTAVICAT | Markt-Filter: zu jung | 0 $ | 2'486 $ | 2026-11-09 |
| [Gasgolem](https://dexscreener.com/solana/8tjxcyftfnzwx7e8rxtj51ypvqfgzlzqgsxylohekg3c) ANTHROPIC GAS GOLEM | Markt-Filter: zu jung | 0 $ | 18'029'680 $ | 2026-11-09 |
| [GTA6](https://dexscreener.com/solana/5rjazs9pwatf2gc9hxj2seutww57q1aygdja9ufzb2h6) GTA VI | Markt-Filter: zu jung | 1'597 $ | 1'564 $ | 2026-11-09 |
| [GTA](https://dexscreener.com/solana/ggu7zxbz9nbens18erttk9p1yrrsyo2a5kwrvbbrzrix) Gta | Markt-Filter: zu jung | 0 $ | 2'453 $ | 2026-11-09 |
| [ANT](https://dexscreener.com/solana/ce9qsaao9tiztoco4j8a84hc48o1r17anpufnzm1bqic) Anthropic | Markt-Filter: zu jung | 60'796 $ | 95'593 $ | 2026-11-09 |
| [GTA6KODAK](https://dexscreener.com/solana/bkaagfumhqvgxa3bqzyabmibsmvietuiapu95prauhx7) GTA6 KODAK BLACK | Markt-Filter: Liquidität 16965$ | 16'965 $ | 52'855 $ | 2026-11-09 |
| [AGTA6](https://dexscreener.com/solana/7tmyzu5blnzzapuvynrzaupjhmjd1draq6caan4mrzvf) after GTA 6 | Markt-Filter: zu alt | 0 $ | 11'888 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/cqfk47mb1xsdxo7mydcdyuw2cof8ad1ebxfwyeuql6yx) Grab That Ass | Markt-Filter: Liquidität 1675$ | 1'675 $ | 1'609 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/gskgzibftdnlhna8wtgc7bk7yz2mtenaqzyjgo9ycuj6) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'510 $ | 2026-11-08 |
| [MOD](https://dexscreener.com/solana/xop7dq4pqahq5f8cbcim3laqsnz5j9kd3xfdrfsgtgn) GTA5 | Markt-Filter: Liquidität 0$ | 0 $ | 367 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/3ncbw8vtqranx4nkfd2heke6w8xzftwel9nhwy978qtr) Grab That Ass | Markt-Filter: Liquidität 1731$ | 1'731 $ | 4'515 $ | 2026-11-08 |
| [MWOLF](https://dexscreener.com/solana/d59tjkurepmra66q48wrkmrqluq5xgh7fakqikpjbrqw) GTA MOONWOLF | Markt-Filter: Liquidität 0$ | 0 $ | 248 $ | 2026-11-08 |
| [GTA6](https://dexscreener.com/solana/girukqkcradhm5aq6gkxddmod8zmkvc6jlxjmudkomdm) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 2'526 $ | 2026-11-08 |
| [GATOGLITCH](https://dexscreener.com/solana/2ueabe4txr5mchey6ckzvncyczh4mbvyqgtwwubtkk1o) GTA6GLITCH | Markt-Filter: Liquidität 3411$ | 3'411 $ | 3'430 $ | 2026-11-08 |
| [GTAMOON](https://dexscreener.com/solana/2dmgss9oyfhccmi5dpbvpt5mpkhakkagzk2yf5cdjer5) GTA SOON MOON | Markt-Filter: Liquidität 0$ | 0 $ | 2 $ | 2026-11-08 |
| [$GTAINU](https://dexscreener.com/solana/cqwfzqzr1gid5maglg6wvlpiauxk3vmyyh4ywnaqy7zy) GTAINU | Markt-Filter: Liquidität 0$ | 0 $ | 2'486 $ | 2026-11-08 |
| [GTA](https://dexscreener.com/solana/hfbpprcrwajwktjuceukn6bad3yz7vdcnhyp6rb1rpzy) Giga Titty Ass | Markt-Filter: Liquidität 1715$ | 1'715 $ | 1'635 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/9tyhyxseygouvuj66vcjkr4bppi65h2muamuveuyy9wm) GTA VI | Markt-Filter: MCap 66353$ | 55'941 $ | 66'353 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/5afbwvsqpjf4cgejq4tajzyypyuvyktrrn3sahnrpnmv) GTA VI | Markt-Filter: zu alt | 129'570 $ | 14'249'272 $ | 2026-11-07 |
| [GTA6COP](https://dexscreener.com/solana/9sebidesbustw8xbbaczb6ab2ty72p6xp51mftpuwhp6) GTA6 Mendez | Markt-Filter: Liquidität 9833$ | 9'833 $ | 20'025 $ | 2026-11-07 |
| [CLAUDEPAID](https://dexscreener.com/solana/7tx6tl3e14nvhqgk4mfp3wdebmwp3rezsqgflxmrunuy) ClaudePaid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [$GTA6](https://dexscreener.com/solana/fytgbkzjhhcsymys7zbfu5ibxkrmwv8frvswvtdmoekz) GTA6 | Markt-Filter: Liquidität 0$ | 0 $ | 242 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/8qnemh37lbcbq2ljaw3tl6fffykbzsqm3ctblhb9krdq) Anthropic | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [HESOYAM](https://dexscreener.com/solana/dxbqzt6erznjp1stwmydan3fememejhn7e2bsbbsrash) GTA 6 CHEAT CODE | Markt-Filter: Liquidität 0$ | 0 $ | 2'503 $ | 2026-11-07 |
| [ANTS](https://dexscreener.com/solana/af5cn9mu1y8coh68xkbypsjxxdk1lbnxgo76dpprrolb) Anthropic | GEKAUFT (simuliert) | 67'356 $ | 697'993 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/f1wcmn8lgkqqwsclbttggzewrr92aphvogxf8ajyx3pt) GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 8'696 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/2hmk1t2s972sl7tmbugr8uh67txctefy5s74j6oaacv4) GTA6 | Markt-Filter: Liquidität 1575$ | 1'575 $ | 1'540 $ | 2026-11-07 |
| [GTA6](https://dexscreener.com/solana/4l7yip761fgodtciqvdcbsbqy2jjts2uu6w8a6rhqbxw) Jason Duval  | Markt-Filter: Liquidität 0$ | 0 $ | 2'514 $ | 2026-11-07 |
| [GTA 6 Coin](https://dexscreener.com/solana/cecxwx7qqt6jp4qa956vzpqyuhuqkmbvgsptxenxrcc9) GTA6 | Markt-Filter: Liquidität 1660$ | 1'660 $ | 1'592 $ | 2026-11-07 |
| [GTA6FLAM](https://dexscreener.com/solana/9q8scnfw3zcph1v33emxent1jvaccnw2rvo9d5r4dk63) GTA6Flamingo | Markt-Filter: Liquidität 0$ | 0 $ | 2'487 $ | 2026-11-07 |
| [GTA6DOG](https://dexscreener.com/solana/6d18zgikseb8qkrjadtlltv3ssgxiwhb7njstmjm1kut) GTA6Dog | Markt-Filter: Liquidität 0$ | 0 $ | 2'494 $ | 2026-11-07 |
| [MTA6](https://dexscreener.com/solana/fgfdumvdcglkcq4zeq11sgqhklbv3ew8pwybx1mum4ys) Monke GTA6 | Markt-Filter: Liquidität 1832$ | 1'832 $ | 1'695 $ | 2026-11-07 |
| [solana](https://dexscreener.com/solana/h71ihsvdcdoab21yxedbb4xddhqrivp6xzpq9doycchb) LUCIA GTA VI | Markt-Filter: Liquidität 0$ | 0 $ | 2'524 $ | 2026-11-07 |
| [GTAmid](https://dexscreener.com/solana/ajzgg3thcspk857xvjerzmwn5saptqyhyh6vb6ijqfkt) GTAmid | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
| [ATM](https://dexscreener.com/solana/1ukbur4jm7vbzfa6anncn9gr2hkactfbl9yae7543xz) GTA6ATM | Markt-Filter: Liquidität 2245$ | 2'245 $ | 2'055 $ | 2026-11-07 |
| [ROCCO](https://dexscreener.com/solana/eenwnbco7lyuysb8r8omaqutz85jc52eizxmfcfzwko7) GTA6 DOGE | Markt-Filter: Liquidität 1769$ | 1'769 $ | 1'667 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/bwfwgjeu3nitww44w2caeocvzqdybxhjhdnmkbgefg71) Grand Theft Airlines | Markt-Filter: Liquidität 2059$ | 2'059 $ | 1'950 $ | 2026-11-07 |
| [GTA](https://dexscreener.com/solana/66litxo66tc7g8kyg52c5kyqnulosrul6qod4dcxczvt) Grand Theft Airlines | Markt-Filter: Liquidität 1778$ | 1'778 $ | 1'662 $ | 2026-11-07 |
| [GTAVI](https://dexscreener.com/solana/ee7tn5dh18dwgpe9ste5g2dxeh6h63sb5yyckjfkyazb) Grand Theft Animal 6 | Markt-Filter: kein USD-Preis | 0 $ | 0 $ | 2026-11-07 |
