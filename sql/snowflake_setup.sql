-- GeoPulse: Snowflake database setup
-- Week 1: Data Loading

-- 1. Create database
CREATE DATABASE IF NOT EXISTS GEOPULSE_DB;

-- 2. Create RAW schema
CREATE SCHEMA IF NOT EXISTS GEOPULSE_DB.RAW;

-- 3. Create GPS pings table
CREATE TABLE IF NOT EXISTS GEOPULSE_DB.RAW.GPS_PINGS (
    DEVICEID VARCHAR(100),
    LAT FLOAT,
    LONG FLOAT,
    TIMESTAMP TIMESTAMP_NTZ,
    LOCATION GEOGRAPHY
);

-- 4. Load synthetic_gps_data.csv into GPS_PINGS
-- This step was performed using the Snowsight Upload Data interface.

-- 5. Populate GEOGRAPHY column
UPDATE GEOPULSE_DB.RAW.GPS_PINGS
SET LOCATION = ST_MAKEPOINT(LONG, LAT)
WHERE LOCATION IS NULL;

-- 6. Validate total records
SELECT COUNT(*) AS TOTAL_ROWS
FROM GEOPULSE_DB.RAW.GPS_PINGS;

-- 7. Validate geographic records
SELECT COUNT(LOCATION) AS GEO_RECORDS
FROM GEOPULSE_DB.RAW.GPS_PINGS;