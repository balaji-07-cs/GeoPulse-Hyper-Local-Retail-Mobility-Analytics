import pandas as pd
from pathlib import Path
from datetime import datetime

input_file = Path("reports/store_performance_summary.csv")
output_file = Path("reports/store_insights.md")

df = pd.read_csv(input_file)
df = df.sort_values("PerformanceRank")

top_store = df.iloc[0]
busiest_store = df.loc[df["PeakVisitors"].idxmax()]

lines = [
    "# GeoPulse - Store Performance Insights",
    "",
    f"Generated: {datetime.now():%Y-%m-%d %H:%M}",
    "",
    "## Overall Highlights",
    "",
    f"- Highest total hourly count: {top_store['StoreName']}",
    f"- Total hourly count: {top_store['TotalHourlyVisitors']}",
    f"- Highest single-hour count: {busiest_store['PeakVisitors']}",
    f"- Store with highest peak: {busiest_store['StoreName']}",
    f"- Peak activity hour: {int(busiest_store['PeakHour']):02d}:00",
    "",
    "## Store Rankings",
    "",
    "| Rank | Store | Total Hourly Count | Average | Peak Count | Peak Hour |",
    "|---:|---|---:|---:|---:|---:|",
]

for _, row in df.iterrows():
    lines.append(
        f"| {int(row['PerformanceRank'])} "
        f"| {row['StoreName']} "
        f"| {int(row['TotalHourlyVisitors'])} "
        f"| {row['AverageHourlyVisitors']:.2f} "
        f"| {int(row['PeakVisitors'])} "
        f"| {int(row['PeakHour']):02d}:00 |"
    )

lines.extend([
    "",
    "## Methodology Note",
    "",
    "Total hourly count is the sum of hourly unique-device counts. "
    "It does not represent distinct devices across the entire day.",
    "",
    "These results are based on synthetic GPS data and should be "
    "treated as analytical demonstrations, not actual retail footfall."
])

output_file.write_text("\n".join(lines), encoding="utf-8")

print(f"Insights report generated: {output_file}")