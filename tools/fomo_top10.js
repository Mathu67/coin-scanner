// Fomo Top 10 -> data/copy/wallets.json
// ------------------------------------------------------------------
// Nur LESEN, mit deinem eigenen Login, in deinem eigenen Browser.
// So gehts (am Computer):
//   1. fomo.family öffnen und einloggen.
//   2. F12 (oder Ctrl+Shift+J) -> Tab "Console". Ganzes Skript einfügen, Enter.
//      (Fragt der Browser zuerst: "allow pasting" eintippen, Enter, nochmals einfügen.)
//   3. Nach ca. 10 Sekunden steht das Ergebnis in der Zwischenablage.
//      Auf GitHub data/copy/wallets.json damit ersetzen.
// Die Fomo-Schnittstelle ist nicht öffentlich und kann sich ändern.
(async () => {
  const API = 'https://prod-api.fomo.family';
  const SOLANA = 1399811149;
  const FENSTER = '30d';      // 30 Tage: weniger Glück als 24h/7d
  const MIN_TRADES = 20;      // Leute mit 1–2 Glückstreffern raus
  const MIN_SOL_SWAPS = 5;    // von den letzten 25 Trades müssen mind. 5 auf Solana sein
  const ANZAHL = 10;
  try {
    const token = JSON.parse(localStorage.getItem('privy:token') || 'null');
    if (!token) throw new Error('Nicht eingeloggt (kein privy:token). Zuerst bei Fomo einloggen.');
    const h = { headers: { authorization: 'Bearer ' + token, 'x-supported-chains': '1,56,143,4663,8453,1399811149' } };
    const get = async pfad => {
      const r = await fetch(API + pfad, h);
      if (!r.ok) throw new Error(pfad + ' -> ' + r.status);
      const j = await r.json();
      return j.responseObject ?? j;
    };
    console.log('Lade Rangliste ...');
    const lb = await get('/v2/leaderboard/' + FENSTER);
    const roh = Array.isArray(lb) ? lb : (lb.leaderboard || Object.values(lb).find(Array.isArray) || []);
    const liste = roh
      .filter(u => !u.isRestricted && (u.numTrades || u.swapCount || 0) >= MIN_TRADES)
      .sort((a, b) => (b.pnl30d || 0) - (a.pnl30d || 0));
    const trader = [];
    for (const u of liste) {
      if (trader.length >= ANZAHL) break;
      await new Promise(r => setTimeout(r, 300));
      const s = await get('/v2/users/' + u.id + '/swaps');
      const sol = (s.swaps || []).filter(x => x.inNetworkId === SOLANA && x.outNetworkId === SOLANA).length;
      console.log(u.userHandle, '| PnL 30d', Math.round(u.pnl30d || 0), '$ | Solana-Trades (von 25):', sol);
      if (sol < MIN_SOL_SWAPS) continue;
      trader.push({ name: u.userHandle || u.displayName, fomo_id: u.id,
                    pnl30d_usd: Math.round(u.pnl30d || 0), trades: u.numTrades || u.swapCount });
    }
    const out = JSON.stringify({
      hinweis: 'Top ' + ANZAHL + ' der Fomo-Rangliste ' + FENSTER + ' (mind. ' + MIN_TRADES + ' Trades). fomo_id = Fomo-Benutzer-ID; der Bot liest deren Trades über Fomo. \'aktiv\': false = nicht mehr kopieren.',
      stand: new Date().toISOString(), trader }, null, 1);
    try { copy(out); console.log('✅ In der Zwischenablage. Auf GitHub in data/copy/wallets.json einfügen.'); } catch (e) {}
    console.log(out);
  } catch (e) {
    console.error('Hat nicht geklappt:', e, '-> Claude die Fehlermeldung schicken.');
  }
})();
