from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True, sep='\t')

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes.show(10)

df_nomes.printSchema()
