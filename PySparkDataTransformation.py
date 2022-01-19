from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Pyspark Experiments").getOrCreate()
df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])
print(df.show())
df.filter('int > 1').show()
