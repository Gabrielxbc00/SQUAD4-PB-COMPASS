import csv

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-04\\ExerciciosPython\\Questao-05\\estudantes.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)

    relatorios = []

    for linha in leitor:
        nome = linha[0]
        notas = list(map(int, linha[1:]))

        tres_maiores_notas = sorted(notas, reverse=True)[:3]

        media_tres_maiores = round(sum(tres_maiores_notas) / 3, 2)

        notas_formatadas = [round(nota, 1) for nota in tres_maiores_notas]

        relatorio = f"Nome: {nome} Notas: {notas_formatadas} Média: {media_tres_maiores}"
        relatorios.append(relatorio)

relatorios_ordenados = sorted(relatorios)

for relatorio in relatorios_ordenados:
    print(relatorio)
