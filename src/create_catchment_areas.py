import os
import pandas as pd

from sedona.spark import SedonaContext

# Input and output paths
input_file = "data/raw/store_locations.csv"
output_file = "data/processed/store_catchment_areas.csv"

# Ensure output directory exists
os.makedirs("data/processed", exist_ok=True)

# Configure Sedona and Spark
config = (
    SedonaContext.builder()
    .master("local[1]")
    .appName("GeoPulseCatchmentAreas")
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
    # Read store locations
    stores = (
        sedona.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_file)
    )

    stores.createOrReplaceTempView("stores")

    # Generate 500-meter catchment polygons
    catchments = sedona.sql("""
        SELECT
            StoreID,
            StoreName,
            ST_Buffer(
                ST_Transform(
                    ST_Point(Long, Lat),
                    'EPSG:4326',
                    'EPSG:32644'
                ),
                500
            ) AS CatchmentArea
        FROM stores
    """)

    # Prepare output with polygon geometry as WKT
    result = catchments.selectExpr(
        "StoreID",
        "StoreName",
        "ST_AsText(CatchmentArea) AS CatchmentWKT",
        "'EPSG:32644' AS CRS"
    )

    # Save results
    result_df = result.toPandas()
    result_df.to_csv(output_file, index=False)

    print("\nCatchment areas generated successfully!")
    print("\nStore catchment summary:")

    for _, row in result_df.iterrows():
        print(f"{row['StoreID']} - {row['StoreName']}")

    print(f"\nTotal catchment areas: {len(result_df)}")
    print(f"Output saved to: {output_file}")

finally:
    sedona.stop()