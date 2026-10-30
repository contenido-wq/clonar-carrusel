// node render.js carrusel.html salida/  -> un PNG 1080x1350 por cada <section class="slide">
const path = require('path'); const fs = require('fs'); const { chromium } = require('playwright');
const [html, out] = process.argv.slice(2);
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy; // para cargar Google Fonts detrás de un proxy
  const browser = await chromium.launch(proxy ? { proxy: { server: proxy } } : {});
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400); // deja correr scripts de ajuste de texto
  const slides = await page.$$('section.slide');
  for (let i = 0; i < slides.length; i++) {
    const overflow = await slides[i].evaluate(el => [...el.querySelectorAll('*')].some(c => { const r = c.getBoundingClientRect(), s = el.getBoundingClientRect(); return r.right > s.right + 1 || r.bottom > s.bottom + 1; }));
    const file = path.join(out, `slide_${String(i + 1).padStart(2, '0')}.png`);
    await slides[i].screenshot({ path: file });
    console.log(file + (overflow ? '  ⚠ texto desbordado' : ''));
  }
  await browser.close();
})();
