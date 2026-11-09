// Fomo Top 10 -> wallets.json
// ------------------------------------------------------------------
// Nur LESEN, mit deinem eigenen Login, in deinem eigenen Browser.
// So gehts (am Computer, Chrome):
//   1. fomo.family öffnen und einloggen.
//   2. F12 -> Tab "Console". Ganzes Skript einfügen, Enter.
//      (Chrome fragt evtl. zuerst: "allow pasting" eintippen, Enter.)
//   3. Auf der Seite einmal irgendwo hinklicken (z. B. Rangliste), damit die App
//      eine Anfrage macht. Das Skript liest daraus nur deinen Login für diese Anfragen.
//   4. Nach ca. 10 Sekunden steht das Ergebnis in der Zwischenablage.
//      In data/copy/wallets.json einfügen (oder Claude schicken).
// Die Fomo-Schnittstelle ist nicht öffentlich und kann sich ändern.
(() => {
  const API = 'https://prod-api.fomo.family';
  const SOLANA = 1399811149;
  const FENSTER = '30d';        // 30 Tage: weniger Glück als 24h/7d
  const MIN_TRADES = 20;        // Leute mit 1–2 Glückstreffern raus
  const MIN_SOL_SWAPS = 5;      // muss wirklich auf Solana handeln
  const ANZAHL = 10;
  let auth = null, chains = '1,56,143,4663,8453,1399811149', gestartet = false;
  const pause = ms => new Promise(r => setTimeout(r, ms));

  const merke = (url, headers) => {
    if (!String(url).includes('prod-api.fomo.family') || !headers) return;
    const h = headers instanceof Headers ? Object.fromEntries(headers.entries()) : headers;
    for (const [k, v] of Object.entries(h)) {
      if (k.toLowerCase() === 'authorization') auth = v;
      if (k.toLowerCase() === 'x-supported-chains') chains = v;
    }
    if (auth && !gestartet) { gestartet = true; los(); }
  };
  const origFetch = window.fetch;
  window.fetch = function (input, init) {
    try { merke(input.url || input, (init && init.headers) || input.headers); } catch (e) {}
    return origFetch.apply(this, arguments);
  };
  const origSet = XMLHttpRequest.prototype.setRequestHeader, origOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (m, url) { this._u = url; return origOpen.apply(this, arguments); };
  XMLHttpRequest.prototype.setRequestHeader = function (k, v) {
    try { merke(this._u, { [k]: v }); } catch (e) {}
    return origSet.apply(this, arguments);
  };

  const get = async pfad => {
    const r = await origFetch(API + pfad, { headers: { authorization: auth, 'x-supported-chains': chains } });
    if (!r.ok) throw new Error(pfad + ' -> ' + r.status);
    const j = await r.json();
    return j.responseObject ?? j;
  };

  async function los() {
    console.log('Login gefunden, lade Rangliste ...');
    try {
      const lb = await get('/v2/leaderboard/' + FENSTER);
      const liste = (lb.leaderboard || lb)
        .filter(u => !u.isRestricted && (u.numTrades || u.swapCount || 0) >= MIN_TRADES)
        .sort((a, b) => (b.pnl30d || 0) - (a.pnl30d || 0));
      const trader = [];
      for (const u of liste) {
        if (trader.length >= ANZAHL) break;
        await pause(400);
        const s = await get('/v2/users/' + u.id + '/swaps');
        const zaehler = {};
        for (const sw of s.swaps || []) {
          if (sw.inNetworkId === SOLANA && sw.address) zaehler[sw.address] = (zaehler[sw.address] || 0) + 1;
          if (sw.outNetworkId === SOLANA && sw.recipient) zaehler[sw.recipient] = (zaehler[sw.recipient] || 0) + 1;
        }
        const [wallet, n] = Object.entries(zaehler).sort((a, b) => b[1] - a[1])[0] || [null, 0];
        console.log(u.userHandle, 'PnL 30d', Math.round(u.pnl30d), '$ | Solana-Swaps', n, wallet || '-');
        if (!wallet || n < MIN_SOL_SWAPS) continue;
        trader.push({ name: u.userHandle || u.displayName, wallet, pnl30d_usd: Math.round(u.pnl30d || 0),
                      trades: u.numTrades || u.swapCount, fomo_id: u.id });
      }
      const out = JSON.stringify({ hinweis: 'Top ' + ANZAHL + ' Fomo ' + FENSTER + ', nur Solana', stand: new Date().toISOString(), trader }, null, 1);
      try { copy(out); console.log('✅ In der Zwischenablage. In data/copy/wallets.json einfügen.'); } catch (e) {}
      console.log(out);
    } catch (e) {
      console.error('Hat nicht geklappt:', e, '-> Claude die Fehlermeldung schicken.');
    }
  }
  console.log('Bereit. Jetzt einmal auf der Seite klicken (z. B. Rangliste).');
})();
