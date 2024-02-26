import boto3
import datetime
import json
import requests

AWS_ACCESS_KEY_ID = 'ASIAUYXM75TNP4EAW4RM'
AWS_SECRET_ACCESS_KEY = 'Gm9adb/Xtazz5KrE1ctaT58id1iDEuK7AnVGVajy'
AWS_SESSION_TOKEN = 'IQoJb3JpZ2luX2VjENX//////////wEaCXVzLWVhc3QtMSJIMEYCIQDf8B6KWgh2CL9/BWbP4oMXLMcBbxhJYqTW3LXFK8K0dgIhALX8eP2MKWddD2Ueen5b4DeP2WKNmOE79RbyKQz0I/rRKrADCL7//////////wEQABoMMzI3OTg4Mjc2NDQyIgyJBBMDT+z6PN5k0qsqhAPtyFQKgolJr042+WeUNrWHtMSfopBhdTt/+owMqlU+XdRldV2mguR2JYKFsEHS3WlxK9IgPXQMr62xb74xrXm3oG6OgcNwf+uBnc87mYNVa4cdfETCiCC+IMPF1EqbqBW53mvT0OAHK5KKcES5faegXMhTWS9/HQsv7wqFeemyMje/Wz3fjJGAP7ZHvV2ILAzZMpPN3LrFmqzuj+WHvFU9AWaXPlQb/757JhAUHwyTTI0qERQq43BmjDBQ5Torgf08CzV5mjde87Jt54dDyzO8D2pu8cmapiNEms9eMoHHRhYW/uHhyOtAtox4RCR2rm2ZVytN92t6l4zqAYfkdSZmFdtw/4QlRyhOptZAdc47BzXZBlGB6Iu38LjwfCAPQse4ukIV+tGFOnqpiKdYbEeSS3u53ex+IFsGzVK163JcHn3eGl2ViuowKWCRykIH/QkSj58WY51rNbKBQeGlXChjrE1FVH/K0DMUaEmWLRf3mVJ1SK9M7XaN8B71ld1vEt2gl0BLMOOJ8q4GOqUBUzrIhD3exjFuooytb2l6aaNQ2yfA0peWkdUI4MCR2mbptvzisb9rezsvfgxJp2a5w/YhBsV468ZAsINHycjxhU1/Ibshlci6kfYAS5C4zGxZ7dkRSi/srSM4Z3RUbi/RNyh9ZKSEgdWGVj9ndcUHLNgwsFWizwI95CU9IY/3JX2PvwDShTgf7QISY86oTUTUqne2YtGXhuXf1NMU8SBwDWSdTuXC'
AWS_REGION = 'us-east-1'

BUCKET_NAME = 'desafio-etl-gx'
omdb_api_key = '6dde2c8d'
movie_title = 'Blade Runner 2049'

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

def lambda_handler(event, context):
    def obter_detalhes_filme_omdb(titulo_filme):
        url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={titulo_filme}"
        resposta = requests.get(url)
        return resposta.json()

    detalhes_filme_omdb = obter_detalhes_filme_omdb(movie_title)

    tempo_atual = datetime.datetime.now().strftime("%Y/%m/%d")
    chave_arquivo = f"raw/omdb/json/{tempo_atual}/blade_runner_2049_details_omdb.json"
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=chave_arquivo,
        Body=json.dumps(detalhes_filme_omdb),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Detalhes do filme Blade Runner 2049 do OMDb inseridos com sucesso no S3!')
    }
