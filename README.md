# GeoPulse – Hyper-Local Retail Mobility Analytics

## 1. Project Overview

GeoPulse is a geospatial retail analytics project designed to understand customer mobility patterns and evaluate retail store performance using anonymized, synthetic GPS location data.

The project aims to help retailers understand foot traffic, analyze store catchment areas, identify overlapping customer audiences, and detect potential cannibalization between nearby retail locations.

By combining geospatial processing, modern data engineering, and interactive visualization, GeoPulse aims to transform location data into actionable retail business insights.

## 2. Project Objectives

- Generate synthetic GPS mobility datasets.
- Analyze hourly foot traffic patterns.
- Identify store catchment areas using geospatial processing.
- Calculate unique visitors per store per hour.
- Identify potential cannibalization between retail locations.
- Visualize geographic foot traffic patterns.
- Develop an interactive retail mobility dashboard.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data generation and processing |
| Pandas | Data analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Snowflake | Geospatial data lakehouse |
| Apache Spark / PySpark | Large-scale data processing |
| Apache Sedona | Geospatial transformations and spatial joins |
| dbt | Data transformation and modeling |
| Kepler.gl | Geospatial visualization |
| React | Dashboard frontend |
| Apache Airflow | Workflow orchestration |
| Git & GitHub | Version control |

## 4. Official Project Timeline

### Week 1 – Data Synthesis and Snowflake Setup

- Generate synthetic anonymized GPS data containing DeviceID, Lat, Long, and Timestamp.
- Set up Snowflake.
- Create database tables using GEOGRAPHY columns.
- Load raw GPS ping data into Snowflake.

### Week 2 – Spatial Processing and ELT Modeling

- Configure Apache Sedona with PySpark.
- Create 500-meter catchment areas around target store locations.
- Perform spatial joins between GPS pings and store catchment polygons.
- Configure dbt to run inside Snowflake.
- Build models to calculate unique visitors per store per hour.

### Mid-Project Review

- Validate spatial intersections using millions of GPS points.
- Check PySpark processing and memory performance.
- Verify dbt compilation and data integrity.
- Validate morning and evening foot traffic patterns.

### Week 3 – Cannibalization Analysis and Map Interface

- Develop cannibalization analysis using unique DeviceIDs.
- Identify devices visiting multiple retail locations.
- Calculate the percentage of shared visitors between stores.
- Integrate Kepler.gl into a React frontend.
- Connect the dashboard to aggregated Snowflake data.

### Week 4 – Automation and Finalization

- Orchestrate PySpark and dbt workflows using Apache Airflow.
- Implement H3 hexagonal spatial indexing.
- Develop 3D foot traffic visualizations.
- Add an interactive 24-hour timeline slider.
- Refine and finalize the retail mobility dashboard.

### Final Project Review

Deliver a specialized geospatial analytics pipeline and interactive 3D mobility dashboard to support retail location and real-estate decisions.

## 5. Dataset Information

The synthetic GPS dataset contains the following fields:

| Column | Description |
|---|---|
| DeviceID | Anonymous synthetic device identifier |
| Lat | Latitude coordinate |
| Long | Longitude coordinate |
| Timestamp | Date and time of GPS observation |

### Current Dataset

- Records: 10,000 GPS pings
- Unique devices: 1,000
- Pings per device: 10
- Geographic area: Chennai, India
- Date: 12 November 2026

The dataset is synthetic and does not contain real individual tracking information.

**Data limitation:** Current GPS points are independently generated around selected retail-area coordinates. They do not yet represent continuous device movement trajectories.

## 6. Repository Structure

```text
GeoPulse-Hyper-Local-Retail-Mobility-Analytics/
│
├── data/
│   ├── raw/
│   │   └── synthetic_gps_data.csv
│   │
│   └── processed/
│       ├── hourly_unique_visitors.csv
│       └── hourly_unique_visitors.png
│
├── src/
│   ├── generate_gps_data.py
│   └── analyze_gps_data.py
│
├── sql/
│   └── snowflake_setup.sql
│
├── README.md
└── .gitignore
```

Additional directories and modules will be introduced as development progresses.

## 7. Current Project Status

**Current Phase:** Week 1 – Data Synthesis and Snowflake Setup

### Completed

- Created and configured the GitHub repository.
- Set up the project locally using VS Code.
- Created the project directory structure.
- Generated 10,000 synthetic GPS records using Python.
- Validated the generated dataset.
- Performed exploratory data analysis using Pandas.
- Extracted hourly visitor activity.
- Identified peak and lowest hourly activity.
- Generated an hourly activity visualization.
- Exported hourly analysis results to CSV.
- Created a Snowflake account and configured the project database.
- Created the `GEOPULSE_DB` database and `RAW` schema.
- Created the `GPS_PINGS` table with a GEOGRAPHY column.
- Loaded 10,000 GPS records into Snowflake.
- Populated geographic points using Snowflake's `ST_MAKEPOINT` function.
- Documented Snowflake setup and validation SQL in `sql/snowflake_setup.sql`.
- Committed and pushed previous development work to GitHub.

### Upcoming

- Prepare store location data.
- Configure Apache Sedona and PySpark.
- Create 500-meter store catchment areas.
- Perform spatial joins between GPS pings and store polygons.
- Build dbt transformation models.
- Calculate unique visitors per store per hour.

**Important:** The current hourly analysis measures unique devices across the entire dataset. It is not yet store-level unique visitor analysis. Store-level metrics will be developed after spatial processing.

## 8. Project Goal

The ultimate goal of GeoPulse is to build a hyper-local retail mobility analytics solution that helps businesses understand customer movement, evaluate store performance, identify potential store cannibalization, and make informed location-based business decisions.

---


### Week 2 – Spatial Analytics and dbt (Completed)

Implemented a geospatial analytics pipeline using Apache Sedona, PySpark, Snowflake, and dbt.

**Completed tasks:**
- Generated 500-metre store catchment areas using geospatial buffers.
- Processed 10,000 synthetic GPS pings using Apache Sedona.
- Performed spatial joins to identify GPS pings within store catchments.
- Calculated distinct device counts per store per hour.
- Connected dbt to Snowflake.
- Created a GPS staging view (`stg_gps_pings`).
- Created an hourly visitor analytics table (`store_hourly_visitors`).
- Added and successfully executed six dbt data quality tests.

**Results:**
- GPS records processed: 10,000
- Matched GPS pings: 6,860
- Synthetic stores analyzed: 4
- Hourly visitor summary records: 96
- dbt models executed successfully: 2
- dbt tests passed: 6/6


### Hourly Store Visitor Visualization
- Created a Python visualization script to plot hourly unique device counts across all four synthetic retail store locations.
- Generated a line chart comparing hourly activity patterns between stores.
- Saved the visualization to `reports/figures/store_hourly_visitors.png`.
- Script: `src/plot_store_hourly_visitors.py`

**Output:** Hourly Unique Device Counts by Store chart.

This visualization helps compare hourly activity patterns across store catchment areas and identify potential peak activity periods.

### Automated Store Performance Insights

- Developed `src/generate_store_insights.py` to automatically generate store performance reports.
- Analyzed hourly unique-device counts across all four synthetic retail stores.
- Identified the highest total hourly count and the highest single-hour activity.
- Generated store performance rankings.
- Included average hourly counts, peak activity counts, and peak activity hours.
- Saved the automated Markdown report to `reports/store_insights.md`.

**Generated Report:** `reports/store_insights.md`

**Key Highlights:**
- T_Nagar ranked first with 1,692 total hourly counts.
- Anna Nagar ranked second with 1,683.
- Velachery ranked third with 1,641.
- Adyar ranked fourth with 1,606.

*Note: Total hourly counts represent the sum of hourly unique-device counts, not distinct daily visitors. All results are based on synthetic GPS data.*

### Store Traffic Comparison Analysis

- Developed `src/compare_store_traffic.py` to compare traffic patterns across four retail stores.
- Calculated total hourly visitor counts and average hourly counts.
- Identified peak and lowest hourly visitor counts for each store.
- Calculated each store's percentage share of total hourly traffic.
- Ranked stores based on their total hourly visitor counts.
- Exported the comparison results to `reports/store_traffic_comparison.csv`.

**Traffic Ranking:**

| Rank | Store | Total Hourly Counts | Traffic Share |
|---|---|---:|---:|
| 1 | T_Nagar | 1,692 | 25.55% |
| 2 | Anna Nagar | 1,683 | 25.42% |
| 3 | Velachery | 1,641 | 24.78% |
| 4 | Adyar | 1,606 | 24.25% |

*Note: Traffic counts represent the sum of hourly unique-device counts, not daily distinct visitors. Results are based on synthetic GPS data.*


**Technology stack:** Python, PySpark, Apache Sedona, Snowflake, dbt, SQL, Pandas.

**Note:** GPS records and store coordinates are synthetic. Visitor counts represent distinct devices detected within 500-metre catchment areas, not verified physical visits.



**Project:** GeoPulse – Hyper-Local Retail Mobility Analytics  
**Domain:** Retail Strategy & Geospatial Analytics  
**Development Environment:** Python | VS Code | Snowflake | GitHub