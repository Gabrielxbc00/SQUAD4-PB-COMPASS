# Apresentar o nome do ator/atriz com a maior média por filme

import pandas as pd

arquivo = r'C:/Users/Gabriel/OneDrive/Documentos/compass/SQUAD4-PB-COMPASS/Sprint-07/Tarefa1-python/actors.csv'
df = pd.read_csv(arquivo)

media_ator = df.loc[df['Average per Movie'].idxmax(), 'Actor']
media_valor = df['Average per Movie'].max()
print(f'Ator/atriz com maior media por filme: {media_ator}, media: {media_valor} ')