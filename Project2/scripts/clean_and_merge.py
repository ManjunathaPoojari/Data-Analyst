from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("CleanMerge").getOrCreate()

# GCS path where the raw CSV files are stored
input_path = "gs://mjk-bucket/fake_branch_data/*/*"  # Adjust path

# Load all CSV files from the GCS bucket
df = spark.read.option("header", "true").csv(input_path)

# Remove rows with null or blank values
cleaned_df = df.dropna(how="any")  # Drop rows that contain null values

# Save the cleaned and merged data back to GCS
output_path = "gs://mjk-bucket/cleaned_data/merged_data.csv"
cleaned_df.write.mode("overwrite").option("header", "true").csv(output_path)

print("Data cleaned and merged successfully!")
