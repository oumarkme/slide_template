# mark-academic-slide

A 16:9 slide template for academic talks, in two matching formats: one LaTeX file (Beamer, XeLaTeX) and one HTML file (reveal.js).

Version 1.0. MIT license.

Both formats share one design: white pages, Noto fonts for English and Traditional Chinese, the Okabe-Ito color palette, and the same geometry, so a PDF and an HTML talk look alike. The demo deck shows lists, blocks, a figure with a credit line, a table, equations, code, and a palette slide. The Beamer theme is written from scratch; its page layout follows Metropolis.

## Install

You need TeX Live with XeLaTeX, Beamer, xeCJK, unicode-math, listings, and `latexmk` for the PDF. The HTML deck needs only a browser and a network connection. Clone the repository and download the Noto fonts for LaTeX once (about 36 MB, needs `curl`):

```bash
git clone https://github.com/oumarkme/slide_template.git
cd slide_template
bash fonts/download.sh
```

## Quick start

```bash
cd latex && latexmk template.tex     # writes template.pdf, 13 pages
```

Then open `html/index.html` in a browser. The PDF and the HTML deck contain the same 13 slides, and the browser tab shows the author name from the title page.

## Contents

| Path | Content |
|---|---|
| `latex/template.tex` | One self-contained file: the Beamer theme (part 1) and the demo deck (part 2). `template.pdf` is the build. |
| `latex/latexmkrc` | Selects XeLaTeX and points it at `fonts/`. |
| `html/index.html` | One self-contained file: theme CSS in `<style>`, a small script, and the demo deck. |
| `fonts/` | `download.sh` fetches the fonts; `OFL.txt` is their license. The font files are not in the repository. |
| `figures/` | The simulated demo figure. |
| `tools/` | Scripts that build both formats and measure how far they differ. |

## Usage

### LaTeX deck

1. Copy `latex/template.tex` to a new file, for example `latex/my-talk.tex`. Keep it in `latex/` so `latexmkrc` finds the fonts. For another folder, copy `latex/latexmkrc` there and adjust the relative paths.
2. Keep part 1 (the theme) unchanged. Edit part 2: the title block and the slides.

   ```latex
   % ======== Part 2: your talk ========
   \title{Talk title}
   \author{Your Name}
   % \footertext{Your Name \textbullet{} Talk title}   % optional left footer; empty by default
   ```

3. Build with `cd latex && latexmk my-talk.tex`. Without latexmk, run `OPENTYPEFONTS=../fonts//: TTFONTS=../fonts//: xelatex my-talk.tex` twice; the trailing colons keep the default search paths.

| Need | Write |
|---|---|
| Section page and outline | `\section{Name}`, `\tableofcontents` |
| Slide | `\begin{frame}{Title} ... \end{frame}` |
| Standout slide (large centered text, no footer or number) | `\begin{frame}[standout] Thank you \end{frame}` |
| Blocks | `block`, `alertblock`, `exampleblock` environments |
| Emphasis | `\alert{text}` (vermillion), `\emph{text}` |
| Figure credit | `\credit{Adapted from ...}` |
| Code | `\begin{frame}[fragile]` with `\begin{codebox}\begin{lstlisting}[language=Python] ... \end{lstlisting}\end{codebox}` |
| Table | `tabular` with `booktabs` rules |
| Math | standard LaTeX math; write bold italic with `\boldsymbol{}` and do not load `amssymb` |
| Chinese | type it directly; technical terms can stay in English |

For colors, use `oiBlue`, `oiVermillion`, `oiGreen`, and the grays `oiInk`, `oiMuted`, and `oiRule`.

### HTML deck

1. Copy `html/index.html` and rename it, for example `my-talk.html`. It holds the theme, so nothing else is needed.
2. Put your images next to it and fix the `src` paths. The demo figure path (`../figures/demo-concordance.png`) works only inside this repository.
3. Edit the slides between the `<div class="slides">` tags. Each slide is one `<section>`. Start from the demo slide closest to what you need and delete the others. Leave the `<style>` and `<script>` blocks alone unless you want to change the design.
4. Open the file in a browser. No server or build step is needed.

The left footer is empty by default. To add text, set it on the container: `<div class="slides" data-footer="Your Name • Talk title">`.

| Need | Write |
|---|---|
| Title page | `<section class="titlepage" data-nonumber>` with `h1`, `.subtitle`, `hr`, `.author`, `.date`, `.institute` |
| Section page | `<section class="sectionpage" data-nonumber><div class="inner"><h2>Name</h2><div class="bar"></div></div></section>` |
| Normal slide | `<section><h2 class="frametitle">Title</h2><div class="frame-body"> ... </div></section>` |
| Standout slide | `<section class="standout" data-nonumber>` |
| Blocks | `<div class="block">`, `class="block alert-block"`, `class="block example-block"`, each with `.block-title` and `.block-body` |
| Two columns | `<div class="columns">` with `<div class="col-46">` and `<div class="col-52">` |
| Table | `<table>`; add `class="num"` to numeric cells and a `<p class="caption muted">` below |
| Figure credit | `<p class="credit">Adapted from ...</p>` |
| Code | `<div class="codebox"><pre><code class="language-python" data-trim data-noescape> ... </code></pre></div>` |
| Math | `$x^2$` inline, `$$ ... $$` displayed (KaTeX) |
| Emphasis | `<span class="alert">text</span>`, `<em>text</em>` |
| Speaker notes | `<aside class="notes">text</aside>` inside a `<section>` |
| Chinese | type it directly |

Slides marked `data-nonumber` are not counted in the frame counter, as in Beamer. The browser tab shows the text of the `.author` line on the title page.

While presenting: arrow keys or Space change slides, `F` goes fullscreen, `Esc` shows the overview, `S` opens the speaker view, and `?` lists all shortcuts. To save a PDF, add `?print-pdf` to the address and print from Chrome with margins set to none.

## Design

* Every page is pure white (`#FFFFFF`), including the last slide. Text is `#1F2328`. Frame titles have no fill; a thin blue line under the title shows progress. For a dark title bar, set `\setbeamercolor{frametitle}{fg=oiPaper, bg=oiInk}` in part 1 of `template.tex` and `background: var(--ink); color: var(--paper)` on `.frametitle` in the CSS.
* One accent, Okabe-Ito blue (`#0072B2`), marks progress lines, block rules, and links. Vermillion (`#D55E00`) marks `\alert` text and warnings; bluish green (`#009E73`) marks examples. The other palette colors appear only on the palette slide. Use color only where it makes a slide easier to read.
* The base size is 10 pt on a 160 x 90 mm page. In HTML, 1 TeX pt equals 2.81 px on a 1280 x 720 grid, which reveal.js scales to the window.

## Fonts and versions

* PDF: Noto Sans (text), Noto Sans Mono (code), Noto Sans CJK TC (Traditional Chinese), Latin Modern Math (math). Files come from `fonts/`, which `latexmkrc` adds to the search path; no system install is needed.
* HTML: Noto Sans, Noto Sans TC, and Noto Sans Mono from Google Fonts through `@import` in the `<style>` block. KaTeX draws math in Computer Modern, so equations look the same in both formats. Offline, the browser's default sans-serif and monospace fonts are used and line breaks may shift slightly.
* HTML libraries load from jsDelivr at pinned versions: reveal.js 6.0.2 (with its highlight, math, and notes plugins) and KaTeX 0.19.1. To update, change the version in the `<link>` and `<script>` tags and in the `katex` setting of the script.
* To fetch the LaTeX fonts by hand, save `NotoSans-{Regular,Bold,Italic,BoldItalic}.ttf` and `NotoSansMono-{Regular,Bold}.ttf` (from `github.com/notofonts/notofonts.github.io`, folders `fonts/NotoSans/unhinted/ttf/` and `fonts/NotoSansMono/unhinted/ttf/`) and `NotoSansCJKtc-{Regular,Bold}.otf` (from `github.com/notofonts/noto-cjk`, folder `Sans/OTF/TraditionalChinese/`) into `fonts/`.
* The Noto fonts are licensed under the SIL Open Font License 1.1 (`fonts/OFL.txt`).

## How the two formats stay alike

1. Both formats use the same grid: 160 x 90 mm in LaTeX, 1280 x 720 px in HTML.
2. The CSS copies the Beamer lengths: type sizes (10, 9, 8, 7, 12, and 14.4 pt), margins (7 mm), the title bar, line spacing (1.15), block spacing, and the 1.2 pt accent lines.
3. A short script (`markAcademicSlide()`) numbers the slides, skipping `data-nonumber` slides as Beamer does, and fills the progress line and the footer.
4. Hyphenation is off in LaTeX so line breaks match the browser.

Limits: line breaks can differ by a word when a line is almost full, and code tokens can split differently because LaTeX `listings` and highlight.js use different tokenizers. pdfLaTeX is not supported; use XeLaTeX.

## Test

`tools/build_and_compare.sh <scratch_dir> <playwright_dir> [python]` builds the PDF, screenshots the HTML deck at 1280 x 720 with headless Chromium, and prints the mean absolute pixel difference (0 to 255) per slide. It needs Playwright with Chromium, Node 20 or later, `pdftoppm`, and Python with Pillow. On the demo deck the values range from 0.7 to 9.4. A value near 0 means the two formats are identical; a jump above 10 after an edit means a layout drift worth inspecting in `<scratch_dir>/cmp/`.

`tools/make_demo_figure.py` redraws the demo figure from simulated data.

## Credits

The page layout follows the Metropolis Beamer theme by Matthias Vogelgesang and contributors (CC BY-SA 4.0). The theme code here is an independent implementation. The color palette is from Okabe and Ito (2008), *Color Universal Design*, https://jfly.uni-koeln.de/color/. reveal.js and KaTeX are MIT licensed.

Author: Jen-Hsiang Ou, Ph.D. Released under the MIT license (`LICENSE`); the Noto fonts keep their own license (`fonts/OFL.txt`).
