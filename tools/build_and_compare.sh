#!/usr/bin/env bash
# Builds the template PDF, renders it and the HTML deck at 1280 x 720, and
# prints how far the two formats differ per slide.
#
# Usage: build_and_compare.sh <scratch_dir> <playwright_dir> [python]
set -euo pipefail

main() {
  local root scratch playwright python
  root="$(cd "$(dirname "$0")/.." && pwd)"
  scratch="$1"
  playwright="$2"
  python="${3:-python3}"

  (cd "${root}/latex" && latexmk template.tex >/dev/null 2>&1) \
    || { echo "LaTeX build failed" >&2; exit 1; }
  rm -rf "${scratch:?}"/{pdf,html,cmp}
  mkdir -p "${scratch}/pdf"
  pdftoppm -png -scale-to-x 1280 -scale-to-y 720 \
    "${root}/latex/template.pdf" "${scratch}/pdf/p"
  node "${root}/tools/html_to_png.cjs" "${root}/html/index.html" \
    "${scratch}/html" "${playwright}"
  "${python}" "${root}/tools/compare_slides.py" \
    "${scratch}/pdf" "${scratch}/html" "${scratch}/cmp"
}

main "$@"
