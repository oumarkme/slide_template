// Screenshots every slide of html/index.html at 1280 x 720, one PNG per slide.
// Usage: node html_to_png.cjs <index.html> <out_dir> [playwright_module_dir]
// Needs playwright (npm install playwright) and Chromium
// (npx playwright install chromium).
const path = require('path');
const fs = require('fs');

const [indexHtml, outDir, pwDir] = process.argv.slice(2);
const {chromium} = require(pwDir || 'playwright');

(async () => {
  fs.mkdirSync(outDir, {recursive: true});
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: {width: 1280, height: 720},
    deviceScaleFactor: 1,
  });
  const url = 'file://' + path.resolve(indexHtml);
  await page.goto(url);
  await page.waitForFunction(
    () => window.Reveal && Reveal.isReady && Reveal.isReady(),
  );
  await page.evaluate(() => document.fonts.ready);
  const count = await page.evaluate(() => Reveal.getTotalSlides());
  for (let i = 0; i < count; i++) {
    await page.evaluate((k) => Reveal.slide(k), i);
    await page.waitForTimeout(250);
    const name = String(i + 1).padStart(2, '0');
    await page.screenshot({path: path.join(outDir, `h-${name}.png`)});
  }
  await browser.close();
  console.log(`wrote ${count} PNGs to ${outDir}`);
})();
