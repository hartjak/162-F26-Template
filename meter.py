import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle


COLORS = {"red": "#d9534f", "yellow": "#f0ad4e", "green": "#5cb85c"}

def draw_meter(score, color):
    title="Password Strength"
    filename="meter.png"
    vmin=0
    vmax=50
    if not (vmin <= score <= vmax):
        raise ValueError(f"score must be between {vmin} and {vmax}")

    needle_color = COLORS[color]

    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw={"aspect": "equal"})

    span = vmax - vmin
    bands = [
            (vmin, 40, COLORS["red"]),
            (40, 45, COLORS["yellow"]),
            (45, vmax, COLORS["green"]),
            ]
    for lo, hi, band_color in bands:
        theta1 = 180 - (hi - vmin) / span * 180
        theta2 = 180 - (lo - vmin) / span * 180
        ax.add_patch(Wedge((0, 0), 1.0, theta1, theta2, width=0.3, facecolor=band_color, edgecolor="white"))

    frac = (score - vmin) / span
    angle = np.radians(180 - frac * 180)
    x, y = 0.85 * np.cos(angle), 0.85 * np.sin(angle)
    ax.plot([0, x], [0, y], color=needle_color, linewidth=4, solid_capstyle="round", zorder=5)
    ax.add_patch(Circle((0, 0), 0.05, facecolor=needle_color, edgecolor="black", zorder=6))

    for val in (vmin, 40, 45, vmax):
        a = np.radians(180 - (val - vmin) / span * 180)
        ax.text(1.15 * np.cos(a), 1.15 * np.sin(a), str(int(val)), ha="center", va="center", fontsize=9)

    ax.text(0, -0.25, f"{title}: {score} ({color})", ha="center", va="center",
            fontsize=13, fontweight="bold", color=needle_color)

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-0.4, 1.3)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close(fig)
    return color
