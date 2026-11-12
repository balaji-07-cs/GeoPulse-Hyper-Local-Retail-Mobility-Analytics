import pandas as pd
import numpy as np

# 1. Set random seed for reproducible results
np.random.seed(42)

# 2. Define project parameters
num_devices = 1000
pings_per_device = 10

# 3. Define Chennai retail locations
locations = {
    "T_Nagar": (13.0418, 80.2341),
    "Anna_Nagar": (13.0850, 80.2101),
    "Velachery": (12.9750, 80.2200),
    "Adyar": (13.0012, 80.2565)
}

# 4. Generate GPS records
records = []

for device_num in range(1, num_devices + 1):

    device_id = f"DEV{device_num:04d}"

    for ping_num in range(pings_per_device):

        # Select a random retail area
        area = np.random.choice(list(locations.keys()))

        center_lat, center_long = locations[area]

        # Generate nearby coordinates
        latitude = center_lat + np.random.normal(0, 0.003)
        longitude = center_long + np.random.normal(0, 0.003)

        records.append({
            "DeviceID": device_id,
            "Lat": latitude,
            "Long": longitude,
            "Timestamp": pd.Timestamp("2026-11-12") +
                         pd.Timedelta(minutes=np.random.randint(0, 1440))
        })

# 5. Convert records into a DataFrame
gps_df = pd.DataFrame(records)

# 6. Sort records by timestamp
gps_df = gps_df.sort_values("Timestamp")

# 7. Save dataset as CSV
output_path = "data/raw/synthetic_gps_data.csv"

gps_df.to_csv(output_path, index=False)

# 8. Display dataset information
print("GeoPulse GPS dataset generated successfully!")
print("Total records:", len(gps_df))
print("Unique devices:", gps_df["DeviceID"].nunique())
print("\nDataset preview:")
print(gps_df.head())

print("\nDataset information:")
print(gps_df.info())