import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

# Configuration options
USE_LOG_SCALE_X = False  # Set to True for log scale on x-axis (Return Periods)
USE_LOG_SCALE_Y = False  # Set to True for log scale on y-axis (Loss)
DATA_PATH = "../test_java/runs/test_java/output/gul_S1_ept.csv"
PLOT_PATH_PNG = "../test_java/runs/test_java/output/gul_S1_ept.png"
PLOT_PATH_PDF = "../test_java/runs/test_java/output/gul_S1_ept.pdf"

# Set modern style
plt.style.use("default")  # Using default style for compatibility

# Load the CSV file
df = pd.read_csv(DATA_PATH)
df = df[df.iloc[:, 1] == 2]
df = df[df.iloc[:, 2] == 3]

# Create figure with custom layout
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
fig.patch.set_facecolor("#f8f9fa")

# Extract data
return_periods = df.iloc[:, -2]
losses = df.iloc[:, -1]

# Create gradient colors based on loss magnitude
# colors = plt.cm.plasma(np.linspace(0, 1, len(losses)))

# Main scatter plot with enhanced styling
scatter = ax.scatter(
    return_periods,
    losses,
    c=losses,
    cmap="plasma",
    s=120,
    alpha=0.8,
    edgecolors="white",
    linewidth=2,
    zorder=5,
)

# Add trend line
if len(return_periods) > 1:
    z = np.polyfit(return_periods, losses, 1)
    p = np.poly1d(z)
    ax.plot(
        return_periods,
        p(return_periods),
        color="red",
        linestyle="--",
        linewidth=3,
        alpha=0.7,
        label=f"Trend Line (slope: {z[0]:.2e})",
    )

# Enhanced title with custom styling
title_text = "Catastrophe Risk Analysis: Return Period vs Expected Loss"
ax.set_title(title_text, fontsize=18, fontweight="bold", pad=25, color="#2c3e50")

# Enhanced axis labels
xlabel_text = "Return Periods (Years)"
ylabel_text = "Expected Loss (IDR)"

if USE_LOG_SCALE_X:
    xlabel_text += " - Log Scale"
if USE_LOG_SCALE_Y:
    ylabel_text += " - Log Scale"

ax.set_xlabel(xlabel_text, fontsize=14, fontweight="semibold", color="#34495e")
ax.set_ylabel(ylabel_text, fontsize=14, fontweight="semibold", color="#34495e")


# Format y-axis to show IDR currency
def idr_currency_formatter(x: float, _) -> str:
    """Format float values as IDR currency."""

    if x >= 1e12:
        return f"Rp{x / 1e12:.1f}T"
    if x >= 1e9:
        return f"Rp{x / 1e9:.1f}B"
    if x >= 1e6:
        return f"Rp{x / 1e6:.1f}M"
    if x >= 1e3:
        return f"Rp{x / 1e3:.1f}K"
    return f"Rp{x:,.0f}"


ax.yaxis.set_major_formatter(FuncFormatter(idr_currency_formatter))

# Enhanced grid
ax.grid(True, alpha=0.3, linestyle="-", linewidth=0.8)
ax.set_axisbelow(True)

# Add colorbar with custom styling
cbar = plt.colorbar(scatter, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label(
    "Loss Magnitude", rotation=270, labelpad=20, fontsize=12, fontweight="semibold"
)
cbar.ax.yaxis.set_major_formatter(FuncFormatter(idr_currency_formatter))

# Add statistics box
stats_text = f"""Data Summary:
• Total Points: {len(losses)}
• Max Loss: Rp{max(losses):,.0f}
• Min Loss: Rp{min(losses):,.0f}
• Mean Loss: Rp{np.mean(losses):,.0f}
• Max Return Period: {max(return_periods):.0f} years"""

# Create fancy text box
props = {"boxstyle": "round,pad=0.5", "facecolor": "lightblue", "alpha": 0.8}

ax.text(
    0.02,
    0.98,
    stats_text,
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=props,
    fontfamily="monospace",
)

# Add legend if trend line exists
if len(return_periods) > 1:
    ax.legend(loc="lower right", frameon=True, fancybox=True, shadow=True, fontsize=11)

# Set log scales based on configuration
if USE_LOG_SCALE_X:
    ax.set_xscale("log")

if USE_LOG_SCALE_Y:
    ax.set_yscale("log")

# Enhance spines
for spine in ax.spines.values():
    spine.set_edgecolor("#7f8c8d")
    spine.set_linewidth(1.5)

# Add subtle background pattern
ax.set_facecolor("#fafbfc")

# Set log scales based on configuration
if USE_LOG_SCALE_X:
    ax.set_xscale("log")

if USE_LOG_SCALE_Y:
    ax.set_yscale("log")

# Tight layout with padding
plt.tight_layout(pad=2.0)

# Save with high quality
plt.savefig(
    PLOT_PATH_PNG,
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)

# Also save as PDF for vector graphics
plt.savefig(
    PLOT_PATH_PDF,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
