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


millennials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()

print(f"Número de pessoas da geração Millennials: {millennials}")


df_nomes.createOrReplaceTempView("pessoas")

millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")

millennials_sql.show()



df_nomes.createOrReplaceTempView("pessoas")
query_baby_boomers = """
    SELECT Pais, 'Baby Boomers' as Generacao, COUNT(*) as Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1944 AND 1964
    GROUP BY Pais
"""
query_geracao_x = """
    SELECT Pais, 'Geração X' as Generacao, COUNT(*) as Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1965 AND 1979
    GROUP BY Pais
"""
query_millennials = """
    SELECT Pais, 'Millennials' as Generacao, COUNT(*) as Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
    GROUP BY Pais
"""
query_geracao_z = """
    SELECT Pais, 'Geração Z' as Generacao, COUNT(*) as Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1995 AND 2015
    GROUP BY Pais
"""

df_baby_boomers = spark.sql(query_baby_boomers)
df_geracao_x = spark.sql(query_geracao_x)
df_millennials = spark.sql(query_millennials)
df_geracao_z = spark.sql(query_geracao_z)

df_resultado = df_baby_boomers.union(df_geracao_x).union(df_millennials).union(df_geracao_z)
df_resultado = df_resultado.orderBy("Pais", "Generacao", "Quantidade")
df_resultado.show()