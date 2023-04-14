from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("TestParser").config()
spark.sql('drop table if exists tab1')