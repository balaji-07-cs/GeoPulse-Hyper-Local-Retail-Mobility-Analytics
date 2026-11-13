import pandas as pd
import matplotlib.pyplot as plt
# 1. Load the GPS dataset
file_path = "data/raw/synthetic_gps_data.csv"
gps_df = pd.read_csv(file_path)

# Convert Timestamp column into datetime format
gps_df["Timestamp"] = pd.to_datetime(gps_df["Timestamp"])

print("\n--- UPDATED DATA TYPES ---")
print(gps_df.dtypes)

# 2. Display the first five records
print("\n--- GPS DATA PREVIEW ---")
print(gps_df.head())

# 3. Display dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Rows and Columns:", gps_df.shape)

# 4. Display column information
print("\n--- DATASET INFORMATION ---")
print(gps_df.info())

# 5. Display statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(gps_df.describe())

# 6. Check missing values
print("\n--- MISSING VALUES ---")
print(gps_df.isnull().sum())

# 7. Analyze hourly GPS activity
gps_df["Hour"] = gps_df["Timestamp"].dt.hour

hourly_footfall = gps_df.groupby("Hour").size()

print("\n--- HOURLY FOOTFALL ANALYSIS ---")
print(hourly_footfall)

# 8. Count unique devices per hour
hourly_unique_visitors = gps_df.groupby("Hour")["DeviceID"].nunique()

# Save hourly visitor analysis
hourly_summary = hourly_unique_visitors.rename(
    "UniqueVisitors"
).reset_index()

hourly_summary.to_csv(
    "data/processed/hourly_unique_visitors.csv",
    index=False
)

print("\nHourly visitor data saved successfully!")

print("\n--- HOURLY UNIQUE VISITORS ---")
print(hourly_unique_visitors)

# 9. Identify peak and lowest visitor hours
peak_hour = hourly_unique_visitors.idxmax()
lowest_hour = hourly_unique_visitors.idxmin()

print("\n--- PEAK HOUR ANALYSIS ---")
print(f"Busiest Hour: {peak_hour}:00")
print(f"Unique Visitors: {hourly_unique_visitors.max()}")

print(f"Quietest Hour: {lowest_hour}:00")
print(f"Unique Visitors: {hourly_unique_visitors.min()}")

# 10. Visualize hourly unique visitors
plt.figure(figsize=(12, 6))

plt.plot(
    hourly_unique_visitors.index,
    hourly_unique_visitors.values,
    marker="o",
    linestyle="-"
)

plt.title("Hourly Unique Visitor Activity")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Unique Visitors")

plt.xticks(range(24))
plt.grid(True)
plt.ylim(bottom=0)

plt.tight_layout()

# Save the chart
plt.savefig("data/processed/hourly_unique_visitors.png")

plt.show()

print("\nChart saved successfully!")