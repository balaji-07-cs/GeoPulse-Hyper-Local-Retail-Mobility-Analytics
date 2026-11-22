import pandas as pd
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "processed" / "store_hourly_visitors.csv"
OUTPUT_FILE = BASE_DIR / "reports" / "store_traffic_comparison.csv"

# Load hourly visitor data
df = pd.read_csv(INPUT_FILE)

# Calculate traffic metrics for each store
comparison = df.groupby(
    ["StoreID", "StoreName"]
).agg(
    TotalHourlyVisitors=("UniqueVisitors", "sum"),
    AverageHourlyVisitors=("UniqueVisitors", "mean"),
    PeakVisitors=("UniqueVisitors", "max"),
    LowestVisitors=("UniqueVisitors", "min")
).reset_index()

# Calculate traffic share
total_traffic = comparison["TotalHourlyVisitors"].sum()

comparison["TrafficSharePercentage"] = (
    comparison["TotalHourlyVisitors"] / total_traffic
) * 100

# Sort stores by total hourly visitor counts
comparison = comparison.sort_values(
    by="TotalHourlyVisitors",
    ascending=False
).reset_index(drop=True)

# Add ranking
comparison["TrafficRank"] = range(1, len(comparison) + 1)

# Save comparison report
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
comparison.to_csv(OUTPUT_FILE, index=False)

print("\nSTORE TRAFFIC COMPARISON")
print("=" * 60)
print(comparison.to_string(index=False))
print(f"\nReport saved to: {OUTPUT_FILE}")