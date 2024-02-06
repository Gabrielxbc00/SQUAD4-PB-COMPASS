# Apresentar o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência

import pandas as pd

arquivo = r'C:/Users/Gabriel/OneDrive/Documentos/compass/SQUAD4-PB-COMPASS/Sprint-07/Tarefa1-python/actors.csv'
df = pd.read_csv(arquivo)

filme_mais_frequente = df['#1 Movie'].value_counts().idxmax()
numero_frequencia = df['#1 Movie'].value_counts().max()

print(f'Filme(s) mais frequente(s): {filme_mais_frequente}, Frequencia: {numero_frequencia}')