import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "reports" / "store_traffic_comparison.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "figures"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load comparison data
df = pd.read_csv(INPUT_FILE)

# Chart 1: Store-wise traffic comparison
plt.figure(figsize=(10, 6))
plt.bar(df["StoreName"], df["TotalHourlyVisitors"])
plt.title("Store-wise Traffic Comparison")
plt.xlabel("Store")
plt.ylabel("Total Hourly Visitor Counts")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "store_traffic_comparison.png", dpi=300)
plt.close()

# Chart 2: Store traffic share
plt.figure(figsize=(8, 8))
plt.pie(
    df["TrafficSharePercentage"],
    labels=df["StoreName"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Store Traffic Share Distribution")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "store_traffic_share.png", dpi=300)
plt.close()

# Chart 3: Peak vs lowest traffic
plt.figure(figsize=(10, 6))
x = range(len(df))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    df["PeakVisitors"],
    width,
    label="Peak"
)

plt.bar(
    [i + width / 2 for i in x],
    df["LowestVisitors"],
    width,
    label="Lowest"
)

plt.xticks(list(x), df["StoreName"], rotation=15)
plt.title("Peak vs Lowest Hourly Traffic")
plt.xlabel("Store")
plt.ylabel("Unique Device Counts")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "peak_vs_lowest_traffic.png", dpi=300)
plt.close()

print("All store comparison visualizations generated successfully!")

print(f"Charts saved in: {OUTPUT_DIR}")
