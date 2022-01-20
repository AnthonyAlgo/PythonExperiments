
from pyspark.sql import *
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("Pyspark Experiments").getOrCreate()
df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])
print(df.show())

def test_transformation(x):
  return x+100
df.filter('int > 1').show()
df.select(transform('int',test_transformation)).show()


