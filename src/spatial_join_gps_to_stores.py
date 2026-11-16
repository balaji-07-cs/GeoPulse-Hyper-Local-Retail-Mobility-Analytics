import os
from sedona.spark import SedonaContext

# Input files
gps_file = "data/raw/synthetic_gps_data.csv"
catchment_file = "data/processed/store_catchment_areas.csv"

# Output files
output_file = "data/processed/store_hourly_visitors.csv"
os.makedirs("data/processed", exist_ok=True)

# Configure Sedona
config = (
    SedonaContext.builder()
    .master("local[1]")
    .appName("GeoPulseSpatialJoin")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-3.5_2.12:1.9.1,"
        "org.datasyslab:geotools-wrapper:1.9.1-33.5"
    )
    .config(
        "spark.jars.repositories",
        "https://artifacts.unidata.ucar.edu/repository/unidata-all"
    )
    .getOrCreate()
)

sedona = SedonaContext.create(config)

try:
    # Read GPS pings and catchment polygons
    gps = (
        sedona.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(gps_file)
    )

    catchments = (
        sedona.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(catchment_file)
    )

    gps.createOrReplaceTempView("gps")
    catchments.createOrReplaceTempView("catchments")

    # Convert GPS coordinates to UTM and match them
    # with the 500-meter store catchment polygons
    joined = sedona.sql("""
        SELECT
            g.DeviceID,
            c.StoreID,
            c.StoreName,
            HOUR(TO_TIMESTAMP(g.Timestamp)) AS Hour
        FROM gps g
        INNER JOIN catchments c
        ON ST_Intersects(
            ST_Transform(
                ST_Point(g.Long, g.Lat),
                'EPSG:4326',
                'EPSG:32644'
            ),
            ST_GeomFromWKT(c.CatchmentWKT)
        )
    """)

    joined.createOrReplaceTempView("store_visits")

    # Calculate unique devices per store per hour
    hourly_visitors = sedona.sql("""
        SELECT
            StoreID,
            StoreName,
            Hour,
            COUNT(DISTINCT DeviceID) AS UniqueVisitors
        FROM store_visits
        GROUP BY StoreID, StoreName, Hour
        ORDER BY StoreID, Hour
    """)

    # Save detailed matched pings
    joined.toPandas().to_csv(
        "data/processed/gps_store_matches.csv",
        index=False
    )

    # Save hourly visitor summary
    hourly_visitors.toPandas().to_csv(
        output_file,
        index=False
    )

    print("\nSpatial join completed successfully!")
    print("Matched GPS pings:", joined.count())
    print("\nStore-wise hourly unique visitors:")
    hourly_visitors.show(30, truncate=False)
    print("Output saved to:", output_file)

finally:
    sedona.stop()