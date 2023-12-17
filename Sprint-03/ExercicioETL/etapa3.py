maior_media_receita = {
    'ator/atriz': None,
    'media': 0
}

with open(r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-03\ExercicioETL\actors.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:
        campos = linha.strip().split(',')
        ator_ou_atriz = campos[0]

        media_receita = float(campos[3])

        if media_receita > maior_media_receita['media']:
            maior_media_receita['ator/atriz'] = ator_ou_atriz
            maior_media_receita['media'] = media_receita

with open(r'C:\\Users\\Gabriel\\OneDrive\\Documentos\\compass\\SQUAD4-PB-COMPASS\\Sprint-03\\ExercicioETL\\etapa-3.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"O ator/atriz com a maior média é {maior_media_receita['ator/atriz']} com média de {maior_media_receita['media']:.2f} milhões de dólares por filme.")
