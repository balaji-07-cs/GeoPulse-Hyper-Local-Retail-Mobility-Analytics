import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/processed/store_hourly_visitors.csv")
output_dir = Path("reports")
output_dir.mkdir(parents=True, exist_ok=True)

# Load hourly visitor data
df = pd.read_csv(input_file)

# Calculate store performance
summary = df.groupby(
    ["StoreID", "StoreName"]
).agg(
    TotalHourlyVisitors=("UniqueVisitors", "sum"),
    AverageHourlyVisitors=("UniqueVisitors", "mean"),
    PeakVisitors=("UniqueVisitors", "max")
).reset_index()

# Find peak activity hour
peak_hours = df.loc[
    df.groupby("StoreID")["UniqueVisitors"].idxmax(),
    ["StoreID", "Hour"]
].rename(columns={"Hour": "PeakHour"})

# Combine results
summary = summary.merge(peak_hours, on="StoreID")

# Rank stores
summary["PerformanceRank"] = (
    summary["TotalHourlyVisitors"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

summary = summary.sort_values("PerformanceRank")

# Save results
output_file = output_dir / "store_performance_summary.csv"
summary.to_csv(output_file, index=False)

print("\nSTORE PERFORMANCE SUMMARY")
print(summary.to_string(index=False))

print(f"\nReport saved to: {output_file}")