# Apresentar a média da coluna contendo o número de filmes

import pandas as pd

arquivo = r'C:/Users/Gabriel/OneDrive/Documentos/compass/SQUAD4-PB-COMPASS/Sprint-07/Tarefa1-python/actors.csv'
df = pd.read_csv(arquivo)

media_filmes = df['Number of Movies'].mean()
print(f'Media do numero de filmes: {media_filmes:.2f}')