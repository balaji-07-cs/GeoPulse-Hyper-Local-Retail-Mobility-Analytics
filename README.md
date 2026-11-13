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
├── README.md
└── .gitignore
```

Additional directories and modules will be introduced as development progresses.

## 7. Current Project Status

**Current Phase:** Week 1 – Data Synthesis and Initial Analysis

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
- Committed and pushed the work to GitHub.

### Pending

- Snowflake environment setup.
- Create Snowflake tables with GEOGRAPHY columns.
- Load raw GPS data into Snowflake.
- Prepare store location data.
- Configure Apache Sedona and PySpark.
- Perform spatial joins.
- Build dbt transformation models.

**Important:** The current hourly analysis measures unique devices across the entire dataset. It is not yet store-level unique visitor analysis. Store-level metrics will be developed after spatial processing.

## 8. Project Goal

The ultimate goal of GeoPulse is to build a hyper-local retail mobility analytics solution that helps businesses understand customer movement, evaluate store performance, identify potential store cannibalization, and make informed location-based business decisions.

---

**Project:** GeoPulse – Hyper-Local Retail Mobility Analytics  
**Domain:** Retail Strategy & Geospatial Analytics  
**Development Environment:** Python | VS Code | 