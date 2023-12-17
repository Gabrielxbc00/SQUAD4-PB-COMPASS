filmes_maior_bilheteria = []

contagem_filmes = {}

with open(r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-03\ExercicioETL\actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas[1:]:
        campos = linha.strip().split(',')
        filme_maior_bilheteria = campos[4]

        filmes_maior_bilheteria.append(filme_maior_bilheteria)

        if filme_maior_bilheteria in contagem_filmes:
            contagem_filmes[filme_maior_bilheteria] += 1
        else:
            contagem_filmes[filme_maior_bilheteria] = 1

contagem_ordenada = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-03\\ExercicioETL\\etapa-4.txt', 'w', encoding='utf-8') as output_file:
    for sequencia, (filme, quantidade) in enumerate(contagem_ordenada, start=1):
        output_file.write(f"{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset.\n")
