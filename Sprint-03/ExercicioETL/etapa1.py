filmes = {
    'ator/atriz': None,
    'quantidade': 0
}

def try_parse_float(value):
    try:
        float(value)
        return True
    except:
        return False


with open(r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-03\ExercicioETL\actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator_ou_atriz = campos[0]

        if try_parse_float(campos[1]):
            quantidade_filmes = float(campos[2])
        else:
            quantidade_filmes = float(campos[3])

        if quantidade_filmes > filmes['quantidade']:
            filmes['ator/atriz'] = ator_ou_atriz
            filmes['quantidade'] = quantidade_filmes

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-03\\ExercicioETL\\etapa-1.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"O ator/atriz com o maior número de filmes é {filmes['ator/atriz']} com {filmes['quantidade']} filmes.")
