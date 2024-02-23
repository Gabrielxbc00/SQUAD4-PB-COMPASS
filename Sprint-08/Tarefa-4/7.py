from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import lit, rand, when, col

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True, sep='\t')

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', 
    when(F.lit(F.rand(seed=42) * 3).cast("int") == 0, "Fundamental")
    .when(F.lit(F.rand(seed=42) * 3).cast("int") == 1, "Médio")
    .otherwise("Superior")
)

paises_sulamericanos = [
    "Brasil", "Argentina", "Colombia", "Venezuela", "Peru",
    "Chile", "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn("Pais",
    F.element_at(
        F.array([F.lit(p) for p in paises_sulamericanos]),
        (F.floor(F.rand() * F.size(F.array([F.lit(p) for p in paises_sulamericanos]))) + 1).cast("int")
    )
)

df_nomes = df_nomes.withColumn("AnoNascimento",
    (lit(rand(seed=42) * (2010 - 1945 + 1) + 1945)).cast("int")
)

df_select = df_nomes.filter(col("AnoNascimento") >= 2000)


df_nomes.createOrReplaceTempView("pessoas")

query = "SELECT * FROM pessoas WHERE AnoNascimento >= 2000"
df_select_sql = spark.sql(query)

df_select_sql.show(10)


