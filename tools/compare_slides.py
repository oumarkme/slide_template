"""Compares PDF page images with HTML slide images.

Usage: python compare_slides.py <pdf_dir> <html_dir> <out_dir>

Inputs: `p-NN.png` (from pdftoppm) and `h-NN.png` (from html_to_png.cjs), both
1280 x 720. Writes `cmp-NN.png` (PDF | HTML | difference, dark = identical)
and prints the mean absolute pixel difference (0-255) per slide.
"""

import glob
import os
import sys

from PIL import Image, ImageChops


def main(pdf_dir: str, html_dir: str, out_dir: str) -> None:
    """Writes one comparison sheet per slide and prints the differences.

    Args:
      pdf_dir: Folder with the PDF page images.
      html_dir: Folder with the HTML slide images.
      out_dir: Folder for the comparison sheets (created if missing).
    """
    os.makedirs(out_dir, exist_ok=True)
    pdf_paths = sorted(glob.glob(os.path.join(pdf_dir, "p-*.png")))
    for i, pdf_path in enumerate(pdf_paths, start=1):
        html_path = os.path.join(html_dir, f"h-{i:02d}.png")
        pdf = Image.open(pdf_path).convert("RGB")
        html = Image.open(html_path).convert("RGB")
        gray = ImageChops.difference(pdf, html).convert("L")
        mean = sum(gray.tobytes()) / (gray.width * gray.height)
        shown = ImageChops.invert(gray.point(lambda v: min(255, v * 3)))
        sheet = Image.new("RGB", (pdf.width * 3 + 20, pdf.height), "#888888")
        for k, image in enumerate((pdf, html, shown.convert("RGB"))):
            sheet.paste(image, (k * (pdf.width + 10), 0))
        sheet.save(os.path.join(out_dir, f"cmp-{i:02d}.png"))
        print(f"slide {i:02d}: mean abs diff {mean:5.2f}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
