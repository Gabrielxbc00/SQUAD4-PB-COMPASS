from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, rand, when

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True, sep='\t')

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', 
                when(lit(rand(seed=42) * 3).cast("int") == 0, "Fundamental")
                .when(lit(rand(seed=42) * 3).cast("int") == 1, "Médio")
                .otherwise("Superior"))

df_nomes.show(10)
