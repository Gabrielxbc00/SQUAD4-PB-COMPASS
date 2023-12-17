def parse_gross(gross):
    try:
        return float(gross)
    except ValueError:
        return 0.0

atores_dados = []

with open(r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-03\ExercicioETL\actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator_nome = campos[0]
        receita_total = parse_gross(campos[1])
        atores_dados.append((ator_nome, receita_total))

atores_ordenados = sorted(atores_dados, key=lambda x: x[1], reverse=True)

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-03\\ExercicioETL\\etapa-5.txt', 'w', encoding='utf-8') as output_file:
    for ator, receita_total in atores_ordenados:
        output_file.write(f"{ator} - {receita_total:.2f} milhões de dólares\n")
