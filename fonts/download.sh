#!/usr/bin/env bash
# Downloads the Noto fonts used by the XeLaTeX templates into this folder (about 36 MB).
# Usage: bash fonts/download.sh [target_dir]   (default: the folder of this script)
# Sources: github.com/notofonts/notofonts.github.io and github.com/notofonts/noto-cjk (SIL OFL 1.1).
set -euo pipefail
dir="${1:-$(cd "$(dirname "$0")" && pwd)}"
mkdir -p "$dir"
latin=https://github.com/notofonts/notofonts.github.io/raw/main/fonts
cjk=https://github.com/notofonts/noto-cjk/raw/main/Sans/OTF/TraditionalChinese
for f in NotoSans-{Regular,Bold,Italic,BoldItalic}.ttf; do
  curl -fsSL --retry 3 -o "$dir/$f" "$latin/NotoSans/unhinted/ttf/$f"
done
for f in NotoSansMono-{Regular,Bold}.ttf; do
  curl -fsSL --retry 3 -o "$dir/$f" "$latin/NotoSansMono/unhinted/ttf/$f"
done
for f in NotoSansCJKtc-{Regular,Bold}.otf; do
  curl -fsSL --retry 3 -o "$dir/$f" "$cjk/$f"
done
echo "Fonts saved in $dir"
