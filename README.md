# GeoPulse – Hyper-Local Retail Mobility Analytics

A geospatial retail analytics project that uses synthetic GPS mobility data to analyze store-level traffic patterns, evaluate retail catchment areas, and identify potential audience overlap between retail locations.

---

## 1. Project Overview

**GeoPulse – Hyper-Local Retail Mobility Analytics** is a data engineering and geospatial analytics project designed to help retailers understand location-based mobility patterns and evaluate store performance.

The project processes synthetic GPS observations to identify devices within retail store catchment areas, calculate hourly device counts, compare store traffic patterns, and analyze potential overlap between retail locations.

By combining geospatial processing, cloud data warehousing, data transformation, and visualization, GeoPulse demonstrates how location intelligence can support retail strategy and site-selection decisions.

### Key Capabilities

- Synthetic GPS data generation and analysis.
- Geospatial store catchment area creation.
- GPS-to-store spatial joins.
- Hourly store-level device-count analysis.
- Snowflake data warehousing.
- dbt-based data transformation and testing.
- Store performance comparison.
- Cross-store device overlap analysis.
- Automated reports and visualizations.

---

## 2. Project Objectives

- Generate synthetic anonymized GPS mobility datasets.
- Analyze hourly location-based activity.
- Create 500-metre catchment areas around retail stores.
- Identify GPS observations within store catchment areas.
- Calculate distinct device counts per store per hour.
- Compare traffic patterns across retail locations.
- Identify devices detected within multiple store catchments.
- Calculate shared-device counts and Jaccard similarity.
- Generate analytical reports and visualizations.

---

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Data generation and processing |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| PySpark | Distributed data processing |
| Apache Sedona | Geospatial processing and spatial joins |
| Shapely | Geospatial geometry operations |
| Snowflake | Cloud data warehousing and geospatial storage |
| SQL | Database queries and transformations |
| dbt | Data transformation and data quality testing |
| Git | Version control |
| GitHub | Source code management |

### Planned Technologies

The following technologies are potential future enhancements and are not part of the currently completed implementation:

- React – Interactive dashboard frontend.
- Kepler.gl – Advanced geospatial visualization.
- Apache Airflow – Workflow orchestration.
- H3 – Hexagonal spatial indexing and aggregation.

---

## 4. Dataset Information

GeoPulse uses a synthetic GPS dataset generated using Python.

### Dataset Attributes

| Attribute | Description |
|---|---|
| DeviceID | Synthetic anonymous device identifier |
| Lat | Latitude coordinate |
| Long | Longitude coordinate |
| Timestamp | GPS observation timestamp |

### Dataset Summary

| Metric | Value |
|---|---:|
| Total GPS records | 10,000 |
| Unique devices | 1,000 |
| GPS records per device | 10 |
| Geographic area | Chennai, India |
| Observation date | 12 November 2026 |
| Synthetic retail locations | 4 |

**Important data limitation:** GPS observations are independently generated around selected retail-area coordinates. They do not represent continuous device movement trajectories or verified customer journeys.

The dataset contains no real individual tracking information.

---

## 5. Store Locations

The project analyzes four representative synthetic retail locations in Chennai.

| Store ID | Store Name | Latitude | Longitude |
|---|---|---:|---:|
| TNG01 | T_Nagar_Store | 13.0418 | 80.2341 |
| ANN01 | Anna_Nagar_Store | 13.0850 | 80.2101 |
| VEL01 | Velachery_Store | 12.9750 | 80.2200 |
| ADY01 | Adyar_Store | 13.0012 | 80.2565 |

A 500-metre catchment area is generated around each store location.

---

## 6. Project Architecture

The GeoPulse implementation follows a geospatial analytics and ELT workflow.

```text
                 SYNTHETIC GPS DATA
                         |
                         v
              Python Data Generation
                         |
                         v
                GPS Dataset (CSV)
                         |
             +-----------+-----------+
             |                       |
             v                       v
       Snowflake Upload       Local Processing
             |                       |
             v                       v
        GPS_PINGS Table       PySpark + Sedona
             |                       |
             |                       v
             |               Store Catchment Areas
             |                       |
             |                       v
             |                 Spatial Joins
             |                       |
             |                       v
             |             GPS-to-Store Matches
             |                       |
             +-----------+-----------+
                         |
                         v
                   dbt Models
                         |
                         v
              Store Hourly Analytics
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Store Performance       Cross-Store Overlap
          Analysis                 Analysis
             |                       |
             v                       v
       CSV / Reports            CSV / Reports
             |                       |
             +-----------+-----------+
                         |
                         v
                   Visualizations
```

---

## 7. Implementation Details

### 7.1 Synthetic GPS Data Generation

**Script:** `src/generate_gps_data.py`

- Generated 10,000 synthetic GPS observations.
- Created 1,000 synthetic device identifiers.
- Generated 10 observations per device.
- Stored latitude, longitude, device ID, and timestamp information.
- Exported the dataset to CSV.

**Output:**

`data/raw/synthetic_gps_data.csv`

### 7.2 Exploratory Data Analysis

**Script:** `src/analyze_gps_data.py`

Performed initial dataset analysis using Pandas.

Activities included:

- Dataset inspection.
- Coordinate validation.
- Missing-value checks.
- GPS observation analysis.
- Hourly activity exploration.

### 7.3 Store Catchment Area Generation

**Script:** `src/create_catchment_areas.py`

Generated 500-metre catchment areas around the four synthetic retail locations.

Implementation details:

- Used Shapely for geometry operations.
- Projected geographic coordinates into UTM EPSG:32644.
- Generated buffer polygons around store locations.
- Exported store catchment geometry information.

**Output:**

`data/processed/store_catchment_areas.csv`

### 7.4 Geospatial Processing and Spatial Joins

**Script:** `src/spatial_join_gps_to_stores.py`

Used PySpark and Apache Sedona to process GPS observations and identify points intersecting store catchment polygons.

Processing steps:

1. Loaded GPS observations.
2. Converted GPS coordinates into spatial points.
3. Transformed coordinates into UTM EPSG:32644.
4. Loaded store catchment geometries.
5. Performed spatial intersection operations.
6. Extracted hourly information.
7. Calculated distinct device counts per store per hour.

**Generated outputs:**

- `data/processed/gps_store_matches.csv`
- `data/processed/store_hourly_visitors.csv`

### 7.5 Snowflake Data Warehousing

Snowflake was used to store raw GPS observations and support geospatial data transformations.

Database configuration:

| Component | Name |
|---|---|
| Database | GEOPULSE_DB |
| Schema | RAW |
| Raw table | GPS_PINGS |
| Geometry type | GEOGRAPHY |

The raw GPS table includes:

- DEVICEID
- LAT
- LONG
- TIMESTAMP
- LOCATION

Geographic points were populated using Snowflake's `ST_MAKEPOINT` function.

### 7.6 dbt Data Transformation

The dbt project is maintained inside:

`geopulse_dbt/`

Implemented models:

| Model | Description |
|---|---|
| `stg_gps_pings` | Staging view for raw GPS observations |
| `store_hourly_visitors` | Store-level hourly device-count analytics table |

The mart model calculates distinct devices within the 500-metre store catchments using Snowflake geospatial functions.

**Data quality validation:**

Six dbt tests were configured and successfully executed.

Test coverage includes:

- Non-null device identifiers.
- Non-null GPS timestamps.
- Non-null store identifiers.
- Non-null hourly timestamps.
- Non-null visitor counts.
- Accepted store ID values.

---

## 8. Store Performance Analysis

**Script:** `src/analyze_store_performance.py`

Developed store-level performance summaries using hourly distinct-device counts.

### Store Performance Results

| Store | Total Hourly Counts | Average Hourly Count | Peak Count | Peak Hour | Rank |
|---|---:|---:|---:|---:|---:|
| T_Nagar | 1,692 | 70.50 | 81 | 15:00 | 1 |
| Anna Nagar | 1,683 | 70.13 | 90 | 13:00 | 2 |
| Velachery | 1,641 | 68.38 | 83 | 10:00 | 3 |
| Adyar | 1,606 | 66.92 | 84 | 21:00 | 4 |

**Output:**

`reports/store_performance_summary.csv`

**Important:** Total hourly counts represent the sum of distinct-device counts across individual hours. They are not daily distinct visitor counts.

---

## 9. Automated Store Insights

**Script:** `src/generate_store_insights.py`

Created an automated Markdown report summarizing store performance.

The report includes:

- Store performance rankings.
- Average hourly device counts.
- Peak hourly activity.
- Store-level comparisons.
- Analytical observations.

**Output:**

`reports/store_insights.md`

---

## 10. Store Traffic Comparison

**Script:** `src/compare_store_traffic.py`

Developed a comparison module to evaluate hourly traffic patterns across all four synthetic stores.

### Features

- Total hourly device-count comparison.
- Average hourly counts.
- Peak and lowest hourly activity.
- Percentage share of total hourly counts.
- Store performance ranking.

**Output:**

`reports/store_traffic_comparison.csv`

### Traffic Share Results

| Rank | Store | Total Hourly Counts | Traffic Share |
|---|---|---:|---:|
| 1 | T_Nagar | 1,692 | 25.55% |
| 2 | Anna Nagar | 1,683 | 25.42% |
| 3 | Velachery | 1,641 | 24.78% |
| 4 | Adyar | 1,606 | 24.25% |

---

## 11. Store Traffic Visualizations

**Script:** `src/visualize_store_comparison.py`

Generated three visualizations to compare store-level traffic performance.

### Generated Charts

**1. Store Traffic Comparison**

Compares total hourly device counts across the four retail locations.

`reports/figures/store_traffic_comparison.png`

**2. Store Traffic Share**

Displays each store's percentage contribution to total hourly counts.

`reports/figures/store_traffic_share.png`

**3. Peak vs Lowest Traffic**

Compares peak and lowest hourly device counts across stores.

`reports/figures/peak_vs_lowest_traffic.png`

### Hourly Store Visitor Visualization

**Script:** `src/plot_store_hourly_visitors.py`

Generated a line chart showing hourly distinct-device counts across the four stores.

`reports/figures/store_hourly_visitors.png`

---

## 12. Cross-Store Device Overlap Analysis

**Script:** `src/analyze_store_cannibalization.py`

GeoPulse includes a cross-store device overlap analysis to identify synthetic device IDs detected within multiple retail store catchment areas.

### Features

- Identifies devices associated with multiple stores.
- Calculates shared device counts for every store pair.
- Computes Jaccard similarity.
- Calculates pairwise overlap percentages.
- Generates analytical CSV and Markdown reports.

### Jaccard Similarity

The Jaccard similarity coefficient measures the overlap between two device sets.

Formula:

```text
Jaccard Similarity =

Number of Shared Devices
-----------------------
Number of Unique Devices Across Both Stores
```

### Pairwise Overlap Results

| Store Pair | Shared Devices | Jaccard Similarity |
|---|---:|---:|
| ADY01 – ANN01 | 708 | 71.95% |
| ADY01 – TNG01 | 696 | 70.37% |
| ADY01 – VEL01 | 704 | 71.26% |
| ANN01 – TNG01 | 705 | 71.36% |
| ANN01 – VEL01 | 718 | 73.12% |
| TNG01 – VEL01 | 707 | 71.70% |

### Key Finding

The highest observed device overlap was between:

**Anna Nagar (ANN01) and Velachery (VEL01)**

- Shared devices: 718
- Jaccard similarity: 73.12%

The lowest observed overlap was between Adyar and T_Nagar, with 696 shared devices and a Jaccard similarity of 70.37%.

### Generated Outputs

- `reports/device_store_overlap.csv`
- `reports/store_device_summary.csv`
- `reports/store_pair_overlap.csv`
- `reports/store_cannibalization_report.md`

### Store Overlap Heatmap

**Script:** `src/visualize_store_overlap.py`

Generated a heatmap showing pairwise device overlap between the four retail locations.

**Output:**

`reports/figures/store_overlap_heatmap.png`

**Methodology limitation:** GPS observations are independently generated rather than continuous device trajectories. Therefore, shared-device overlap is an analytical indicator based on synthetic observations, not proof of actual customer journeys, store switching, or retail cannibalization.

---

## 13. Project Results and Validation

The current implementation successfully demonstrates a complete geospatial analytics workflow using synthetic GPS observations.

### Processing Results

| Metric | Result |
|---|---:|
| Input GPS records | 10,000 |
| Synthetic devices | 1,000 |
| Matched GPS pings | 6,860 |
| GPS match percentage | 68.6% |
| Synthetic stores | 4 |
| Hourly summary records | 96 |
| Store pairs analyzed | 6 |

### Final dbt Validation

| Validation | Result |
|---|---|
| Snowflake connection | Successful |
| dbt debug | Passed |
| dbt staging model | Successful |
| dbt mart model | Successful |
| Total dbt models | 2 |
| dbt data quality tests | 6/6 passed |

The project successfully executed both dbt models and all six configured data quality tests against Snowflake during final validation.

---

## 14. Repository Structure

```text
GeoPulse-Hyper-Local-Retail-Mobility-Analytics/
│
├── data/
│   ├── raw/
│   │   └── synthetic_gps_data.csv
│   │
│   └── processed/
│       ├── store_catchment_areas.csv
│       ├── gps_store_matches.csv
│       └── store_hourly_visitors.csv
│
├── geopulse_dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_gps_pings.sql
│   │   │   └── sources.yml
│   │   │
│   │   ├── marts/
│   │   │   └── store_hourly_visitors.sql
│   │   │
│   │   └── schema.yml
│   │
│   └── dbt_project.yml
│
├── reports/
│   ├── figures/
│   │   ├── peak_vs_lowest_traffic.png
│   │   ├── store_hourly_visitors.png
│   │   ├── store_overlap_heatmap.png
│   │   ├── store_traffic_comparison.png
│   │   └── store_traffic_share.png
│   │
│   ├── device_store_overlap.csv
│   ├── store_device_summary.csv
│   ├── store_pair_overlap.csv
│   ├── store_cannibalization_report.md
│   ├── store_insights.md
│   ├── store_performance_summary.csv
│   └── store_traffic_comparison.csv
│
├── src/
│   ├── generate_gps_data.py
│   ├── analyze_gps_data.py
│   ├── create_catchment_areas.py
│   ├── spatial_join_gps_to_stores.py
│   ├── plot_store_hourly_visitors.py
│   ├── analyze_store_performance.py
│   ├── generate_store_insights.py
│   ├── compare_store_traffic.py
│   ├── visualize_store_comparison.py
│   ├── analyze_store_cannibalization.py
│   └── visualize_store_overlap.py
│
├── sql/
│   └── snowflake_setup.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 15. Running the Project

### Step 1 – Clone the Repository

```bash
git clone https://github.com/balaji-07-cs/GeoPulse-Hyper-Local-Retail-Mobility-Analytics.git
```

```bash
cd GeoPulse-Hyper-Local-Retail-Mobility-Analytics
```

### Step 2 – Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 – Run the Python Analytics Scripts

Run the required scripts from the project root:

```bash
python src/generate_gps_data.py
```

```bash
python src/create_catchment_areas.py
```

```bash
python src/spatial_join_gps_to_stores.py
```

```bash
python src/analyze_store_performance.py
```

```bash
python src/compare_store_traffic.py
```

```bash
python src/analyze_store_cannibalization.py
```

Generate visualizations:

```bash
python src/plot_store_hourly_visitors.py
```

```bash
python src/visualize_store_comparison.py
```

```bash
python src/visualize_store_overlap.py
```

### Step 5 – Configure Snowflake and dbt

Configure your Snowflake connection through your local dbt profile.

Do not commit credentials or passwords to the repository.

Navigate to the dbt project:

```bash
cd geopulse_dbt
```

Check the connection:

```bash
dbt debug
```

Execute models:

```bash
dbt run
```

Run data quality tests:

```bash
dbt test
```

**Note:** Snowflake account access, database configuration, and the required source data must be available to execute the dbt models successfully.

---

## 16. Limitations

The current implementation has the following limitations:

1. The GPS dataset is synthetic and does not represent real customer location information.
2. GPS observations are independently generated and do not form continuous movement trajectories.
3. Device counts are analytical proxies, not verified physical customer visits.
4. Hourly distinct-device counts cannot be interpreted as daily unique visitors.
5. Cross-store overlap does not prove customer switching or actual retail cannibalization.
6. The project currently focuses on batch processing and analytical reporting.
7. Large-scale performance benchmarking using millions of GPS records has not been completed.
8. An interactive React and Kepler.gl dashboard has not yet been implemented.

These limitations should be considered when interpreting the analytical results.

---

## 17. Future Enhancements

Potential future development includes:

- Integrating Kepler.gl for interactive geospatial visualization.
- Developing a React-based retail analytics dashboard.
- Implementing Apache Airflow for workflow orchestration.
- Introducing H3 hexagonal spatial indexing.
- Building 3D spatial traffic visualizations.
- Adding an interactive 24-hour timeline.
- Generating continuous synthetic mobility trajectories.
- Evaluating scalability with larger GPS datasets.
- Improving retail catchment and cannibalization analysis.

---

## 18. Conclusion

GeoPulse demonstrates how synthetic location data can be transformed into useful retail analytics through geospatial processing and data engineering.

The completed implementation combines Python, PySpark, Apache Sedona, Snowflake, and dbt to generate store-level hourly analytics, compare retail traffic patterns, and identify potential overlap between store catchment areas.

The project provides a foundation for future development of advanced retail mobility analytics and location-intelligence solutions.

---

## Project Information

**Project Name:** GeoPulse – Hyper-Local Retail Mobility Analytics

**Domain:** Retail Strategy & Geospatial Analytics

**Data:** Synthetic GPS Mobility Dataset

**Primary Technologies:** Python, PySpark, Apache Sedona, Snowflake, dbt, SQL, Pandas, Matplotlib

**Development Environment:** Windows 11, VS Code, Python 3.11

**Repository:**  
https://github.com/balaji-07-cs/GeoPulse-Hyper-Local-Retail-Mobility-Analytics