const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const [url, out] = process.argv.slice(2);
if (!url || !out) { console.error('Uso: node capturar.js <url> <salida/>'); process.exit(1); }
const code = (url.match(/instagram\.com\/(?:[^/]+\/)?(?:p|reel|tv)\/([A-Za-z0-9_-]+)/) || [])[1];
if (!code) { console.error('No reconozco el link de Instagram'); process.exit(1); }
fs.mkdirSync(out, { recursive: true });
const UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';
async function save(page, src, i) {
  const res = await page.request.get(src);
  if (!res.ok()) return false;
  fs.writeFileSync(path.join(out, `slide_${String(i).padStart(2, '0')}.jpg`), await res.body());
  return true;
}
function imageUrls(html) {
  let txt = html, prev;
  do { prev = txt; txt = txt.replace(/\\+u([0-9a-fA-F]{4})/g, (_, h) => String.fromCharCode(parseInt(h, 16))).replace(/\\+\//g, '/').replace(/\\+"/g, '"').replace(/&amp;/g, '&'); } while (txt !== prev);
  const sidecar = txt.match(/"edge_sidecar_to_children".*?"edges":\[(.*?)\]\}/s);
  const scope = sidecar ? sidecar[1] : txt;
  const urls = [];
  for (const m of scope.matchAll(/"display_url":"(https:[^"]+)"/g)) if (!urls.includes(m[1])) urls.push(m[1]);
  return urls;
}
(async () => {
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const browser = await chromium.launch(proxy ? { proxy: { server: proxy } } : {});
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 430, height: 932 }, deviceScaleFactor: 3, locale: 'es-CO' });
  const page = await ctx.newPage();
  let n = 0;
  try {
    await page.goto(`https://www.instagram.com/p/${code}/embed/captioned/`, { waitUntil: 'networkidle', timeout: 45000 });
    const urls = imageUrls(await page.content());
    for (const u of urls) if (await save(page, u, n + 1)) n++;
    const cap = await page.$eval('.Caption', el => el.innerText).catch(() => '');
    if (cap) fs.writeFileSync(path.join(out, 'caption_original.txt'), cap);
  } catch (e) { console.error('[embed] ' + e.message); }
  if (n < 2) {
    try {
      await page.goto(`https://www.instagram.com/p/${code}/`, { waitUntil: 'networkidle', timeout: 45000 });
      for (const sel of ['text=/Ahora no|Not now/i', '[aria-label="Cerrar"]', '[aria-label="Close"]', 'text=/Permitir todas|Allow all/i'])
        await page.locator(sel).first().click({ timeout: 2000 }).catch(() => {});
      const box = page.locator('main article ul').first();
      n = 0;
      for (let i = 1; i <= 20; i++) {
        await page.waitForTimeout(700);
        await box.screenshot({ path: path.join(out, `slide_${String(i).padStart(2, '0')}.png`) });
        n = i;
        const next = page.locator('button[aria-label="Siguiente"], button[aria-label="Next"]').first();
        if (!(await next.isVisible().catch(() => false))) break;
        await next.click();
      }
    } catch (e) { console.error('[navegador] ' + e.message); }
  }
  await browser.close();
  if (n) { console.log(`OK ${n} slides -> ${out}`); return; }
  console.error('NO_SE_PUDO_CAPTURAR'); process.exit(2);
})();
