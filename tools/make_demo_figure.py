"""Draws the demo figure used by both slide templates.

The data are simulated. Colors are Okabe-Ito; markers and line styles differ
so the groups survive gray printing.

Usage: python make_demo_figure.py <out.png>
Output: opaque white PNG, 300 dpi, 90 x 62 mm, Noto Sans text of 10 pt.
"""

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # pylint: disable=wrong-import-position
import numpy as np  # pylint: disable=wrong-import-position
from matplotlib import font_manager  # pylint: disable=wrong-import-position

_FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                         "fonts")
_GRAY = "#4D5258"
# (label, color, marker, line style, saturation rate)
_SERIES = (
    ("Method A", "#0072B2", "o", "-", 0.30),
    ("Method B", "#D55E00", "^", "--", 0.55),
    ("Method C", "#009E73", "s", ":", 0.80),
)


def main(out: str) -> None:
    """Writes the figure to `out`.

    Args:
      out: Path of the PNG file to write.
    """
    for name in ("NotoSans-Regular", "NotoSans-Italic", "NotoSans-Bold"):
        font_manager.fontManager.addfont(
            os.path.join(_FONT_DIR, f"{name}.ttf"))
    plt.rcParams.update({"font.family": "Noto Sans", "font.size": 10})
    depth = np.array([5, 10, 15, 20, 30, 40, 60])
    fig, ax = plt.subplots(figsize=(90 / 25.4, 62 / 25.4))
    for label, color, marker, line, rate in _SERIES:
        # Simulated saturating curve; not real data.
        concordance = 99.9 - 18 * np.exp(-rate * depth / 5) * (1.4 - rate)
        ax.plot(depth, concordance, color=color, marker=marker,
                linestyle=line, lw=1.8, ms=5.5, label=label)
    ax.set_xlabel("Mean depth (×)", color=_GRAY)
    ax.set_ylabel("Genotype concordance (%)", color=_GRAY)
    ax.set_ylim(80, 100)
    ax.tick_params(colors=_GRAY)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(_GRAY)
    ax.legend(frameon=False, loc="lower right", handlelength=2.6)
    fig.text(0.99, 0.01, "Simulated data", ha="right", va="bottom",
             fontsize=8, style="italic", color=_GRAY)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(out, dpi=300, facecolor="white",
                pil_kwargs={"dpi": (300, 300)})


if __name__ == "__main__":
    main(sys.argv[1])
