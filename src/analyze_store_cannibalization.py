
import os
from itertools import combinations

import pandas as pd


INPUT_FILE = "data/processed/gps_store_matches.csv"
OUTPUT_DIR = "reports"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load GPS-to-store matching records
df = pd.read_csv(INPUT_FILE)

required_columns = {"DeviceID", "StoreID", "StoreName", "Hour"}

if not required_columns.issubset(df.columns):
    raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

# Create one device set for each store
store_devices = {
    store_id: set(group["DeviceID"].unique())
    for store_id, group in df.groupby("StoreID")
}

# Store-level device summary
store_summary = []

for store_id, devices in store_devices.items():
    store_name = df.loc[df["StoreID"] == store_id, "StoreName"].iloc[0]

    store_summary.append({
        "StoreID": store_id,
        "StoreName": store_name,
        "UniqueMatchedDevices": len(devices)
    })

store_summary_df = pd.DataFrame(store_summary)

# Store-pair overlap analysis
pair_results = []

for store_a, store_b in combinations(sorted(store_devices), 2):
    devices_a = store_devices[store_a]
    devices_b = store_devices[store_b]

    shared_devices = devices_a & devices_b
    union_devices = devices_a | devices_b

    jaccard = (
        len(shared_devices) / len(union_devices)
        if union_devices else 0
    )

    pair_results.append({
        "StoreA": store_a,
        "StoreB": store_b,
        "DevicesInStoreA": len(devices_a),
        "DevicesInStoreB": len(devices_b),
        "SharedDevices": len(shared_devices),
        "JaccardSimilarity": round(jaccard, 4),
        "OverlapPercentage": round(jaccard * 100, 2)
    })

pair_df = pd.DataFrame(pair_results)

# Identify devices detected around multiple stores
device_store_counts = (
    df.groupby("DeviceID")["StoreID"]
    .nunique()
    .reset_index(name="NumberOfStores")
)

multi_store_devices = device_store_counts[
    device_store_counts["NumberOfStores"] > 1
]

# Save analytical outputs
store_summary_df.to_csv(
    f"{OUTPUT_DIR}/store_device_summary.csv",
    index=False
)

pair_df.to_csv(
    f"{OUTPUT_DIR}/store_pair_overlap.csv",
    index=False
)

device_store_counts.to_csv(
    f"{OUTPUT_DIR}/device_store_overlap.csv",
    index=False
)

# Generate Markdown report
highest_overlap = pair_df.loc[pair_df["JaccardSimilarity"].idxmax()]
lowest_overlap = pair_df.loc[pair_df["JaccardSimilarity"].idxmin()]

report = f"""# Store Cannibalization and Cross-Store Overlap Analysis

## Overview

This report analyzes synthetic GPS-to-store matching records
to identify devices detected within multiple store catchment areas.

The results are potential cross-store overlap indicators.
They do not establish actual customer movement, store switching,
or confirmed retail cannibalization.

## Dataset Summary

- GPS-to-store matching records: {len(df):,}
- Matched devices: {df['DeviceID'].nunique():,}
- Stores analyzed: {len(store_devices)}
- Store pairs analyzed: {len(pair_df)}
- Devices detected near multiple stores: {len(multi_store_devices):,}

## Store-Level Device Summary

{store_summary_df.to_markdown(index=False)}

## Store-Pair Overlap

{pair_df.to_markdown(index=False)}

## Key Findings

- Highest pairwise overlap: {highest_overlap['StoreA']} and
  {highest_overlap['StoreB']}, with
  {highest_overlap['SharedDevices']} shared devices and
  {highest_overlap['OverlapPercentage']:.2f}% Jaccard similarity.

- Lowest pairwise overlap: {lowest_overlap['StoreA']} and
  {lowest_overlap['StoreB']}, with
  {lowest_overlap['SharedDevices']} shared devices and
  {lowest_overlap['OverlapPercentage']:.2f}% Jaccard similarity.

## Methodology

For each store pair, shared devices are calculated using set
intersection.

Jaccard similarity is calculated as:

J(A, B) = |A intersection B| / |A union B|

## Limitations

- The GPS dataset is synthetic.
- GPS pings are independently generated rather than continuous trajectories.
- Devices detected near multiple stores are not necessarily customers
  visiting or switching between those stores.
- High overlap does not prove geographic competition or cannibalization.
- Further analysis with real, consented mobility data and verified
  store locations would be required for business conclusions.
"""

with open(f"{OUTPUT_DIR}/store_cannibalization_report.md", "w", encoding="utf-8") as file:
    file.write(report)

print("Store overlap analysis completed successfully!")
print(f"Matched devices: {df['DeviceID'].nunique():,}")
print(f"Devices detected near multiple stores: {len(multi_store_devices):,}")
print(f"Store pairs analyzed: {len(pair_df)}")
print("\nHighest overlap:")
print(highest_overlap.to_string())
print(f"\nReports saved in: {OUTPUT_DIR}")
