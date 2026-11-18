import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
input_file = Path("data/processed/store_hourly_visitors.csv")
output_dir = Path("reports/figures")
output_dir.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(input_file)

# Normalize column names
df.columns = df.columns.str.strip()

# Plot hourly visitors for each store
plt.figure(figsize=(12, 6))

for store_name, group in df.groupby("StoreName"):
    group = group.sort_values("Hour")
    plt.plot(
        group["Hour"],
        group["UniqueVisitors"],
        marker="o",
        label=store_name
    )

plt.title("Hourly Unique Device Counts by Store")
plt.xlabel("Hour of Day")
plt.ylabel("Unique Devices")
plt.xticks(range(24))
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Save chart
output_file = output_dir / "store_hourly_visitors.png"
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Chart saved to: {output_file}")