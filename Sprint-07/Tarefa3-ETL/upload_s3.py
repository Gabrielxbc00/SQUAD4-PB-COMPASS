import boto3
import pandas as pd
from datetime import datetime

aws_access_key_id = 'ASIAUYXM75TNEPYGQEF3'
aws_secret_access_key = 'g/AjOJqRBHb+0961A9EIFw37nhqsCbo3qEQrVDYY'
aws_session_token = 'IQoJb3JpZ2luX2VjEDEaCXVzLWVhc3QtMSJHMEUCICvQO8yvjGyJWcOv67E1N0Qnx2pCCxVKlixxtn81V+sDAiEAodbSSzkdorhaePS9ku2SpluNhihHmemxctJtNGt2g8gqpwMIGhAAGgwzMjc5ODgyNzY0NDIiDC4xIymgrMMsi+BI1iqEA6056D3R2Xp/Ertt96+NKxI0GWK1G8KNJaSaAc4di7z50NC0dCqKnY6+Za3DmzhBEFQywCZA/q4BfJYGfWXkPeVJQ7aAPtHPIWcX0zY/5zvwuvoW91Fd3to8tuc2NUwX4F9eZN7Ifu7G17UboiQ+eyx/M0WeDBzN8EoRoIk/uHzpf9hCqXuzohUbLNvEWiPzbJ3QnjPeZUo/g+BUgis6QFacy9uPxnXsImNFqsWWb5TgtrwcABI+vEGWI9mLAwPcS9g6Na+6CjW1/X4G74WAt13tpFA7i7u5BIC9ucPBW8OlEXDNvYfSTplLt8har7AspW/jZ5S7IO898dQ7lwBQ0leDG8MG08I4BN7YvjzbIezmEsGc//rvdr0uUqdsvoCnB275zwf2n4BVlAmdRi0ie8YLeLdc3uD148VsTFTgZWdygliqFR8BN4BwtDvc9tokV4D/erJrrfwy3bgxr/ti21oXdI4JWTD3D5CYowSUXf7VXRI+ky/znxgUZOdbfGmlQ7pMUHcwio/OrgY6pgH0MnPWZDLNlojO0dBfYxBA7RHFxY1S6TJ4hetYOp9yQTudSbFFUG9fCO4bjPGsuV0hf5j3IkT4MtbdX1O6jmxBZtLvN1mxUVA6uFMlAsH71H1aDgEaSOihBQvL0Jpil5poA66zEp9jkSlYFUYNhV5fSxgZiOIK67uAqd7273tTTcsHc1MTML+a2KFh83zxd/xKPWHySeM6aTKBE9EOlLsXNiGTyw53'
region_name = 'us-east-1'

bucket = 'sprint7-desafio-etl'
destino = 'Raw/Local/CSV'

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  aws_session_token=aws_session_token,
                  region_name=region_name)

def upload_s3(nome_arquivo, caminho_arquivo, tipo_arquivo):
    data_atual = datetime.now().strftime('%Y/%m/%d')

    caminho_s3 = f"{destino}/{tipo_arquivo}/{data_atual}/{nome_arquivo}"

    df = pd.read_csv(caminho_arquivo, sep='|', header=0)

    csv_buff = df.to_csv(index=False)

    s3.put_object(Body=csv_buff, Bucket=bucket, Key=caminho_s3)

    print(f"Arquivo {nome_arquivo} enviado para o S3 com sucesso!")

upload_s3('movies.csv', '/app/movies.csv', 'Movies')
upload_s3('series.csv', '/app/series.csv', 'Series')
