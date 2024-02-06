# Identificar o ator/atriz com maior número de filmes e o respectivo número de filmes

import pandas as pd

arquivo = r'C:/Users/Gabriel/OneDrive/Documentos/compass/SQUAD4-PB-COMPASS/Sprint-07/Tarefa1-python/actors.csv'
df = pd.read_csv(arquivo)

filmes_ator = df.loc[df['Number of Movies'].idxmax(), 'Actor']
numero_filmes = df['Number of Movies'].max()
print(f'Ator/atriz com maior numero de filmes: {filmes_ator}, Numero de filmes: {numero_filmes}')