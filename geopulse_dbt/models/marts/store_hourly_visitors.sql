{{ config(materialized='table') }}

WITH stores AS (
    SELECT 'TNG01' AS STORE_ID, 'T_Nagar_Store' AS STORE_NAME, 13.0418 AS LATITUDE, 80.2341 AS LONGITUDE
    UNION ALL
    SELECT 'ANN01', 'Anna_Nagar_Store', 13.0850, 80.2101
    UNION ALL
    SELECT 'VEL01', 'Velachery_Store', 12.9750, 80.2200
    UNION ALL
    SELECT 'ADY01', 'Adyar_Store', 13.0012, 80.2565
),

matched_pings AS (
    SELECT
        s.STORE_ID,
        s.STORE_NAME,
        g.DEVICE_ID,
        DATE_TRUNC('HOUR', g.PING_TIMESTAMP) AS HOUR_START
    FROM {{ ref('stg_gps_pings') }} g
    CROSS JOIN stores s
    WHERE ST_DISTANCE(
        g.GEO_LOCATION,
        ST_MAKEPOINT(s.LONGITUDE, s.LATITUDE)
    ) <= 500
)

SELECT
    STORE_ID,
    STORE_NAME,
    HOUR_START,
    COUNT(DISTINCT DEVICE_ID) AS UNIQUE_VISITORS
FROM matched_pings
GROUP BY STORE_ID, STORE_NAME, HOUR_START
ORDER BY STORE_ID, HOUR_START