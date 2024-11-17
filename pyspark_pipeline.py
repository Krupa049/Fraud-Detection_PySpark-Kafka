
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime
from pyspark.sql.window import Window
from pyspark.sql.functions import avg, count
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

def main(input_file='transactions.csv', output_file='suspicious_transactions.csv'):
    # Initialize Spark Session
    spark = SparkSession.builder.appName("FraudDetectionPipeline").getOrCreate()

    # Load Data
    schema = (
        "transaction_id INT, customer_id INT, merchant_id INT, amount FLOAT, "
        "latitude FLOAT, longitude FLOAT, timestamp FLOAT"
    )
    transactions = spark.read.csv(input_file, schema=schema, header=True)

    # Preprocess Data
    transactions = transactions.withColumn("timestamp", from_unixtime(col("timestamp")))
    transactions = transactions.withColumn("transaction_velocity", col("amount") / 100)

    # Feature Engineering
    window_spec = Window.partitionBy("customer_id").orderBy("timestamp").rowsBetween(-10, 0)
    transactions = transactions.withColumn("avg_amount", avg("amount").over(window_spec))
    transactions = transactions.withColumn("transaction_count", count("transaction_id").over(window_spec))

    # Assemble Features
    feature_cols = ["amount", "transaction_velocity", "avg_amount", "transaction_count"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    feature_data = assembler.transform(transactions)

    # KMeans Clustering
    kmeans = KMeans(k=2, seed=1)
    model = kmeans.fit(feature_data)
    predictions = model.transform(feature_data)

    # Save Results
    suspicious_transactions = predictions.filter(predictions.prediction == 1)
    suspicious_transactions.write.csv(output_file, mode="overwrite", header=True)

    print(f"Suspicious transactions saved to {output_file}")

if __name__ == "__main__":
    main()
