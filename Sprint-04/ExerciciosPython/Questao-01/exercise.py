def ler_numeros(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return [int(line.strip()) for line in file]

nome_arquivo = r'C:\Users\Gabriel\OneDrive\Documentos\compass\SQUAD4-PB-COMPASS\Sprint-04\Exercicios\Questao-01\number.txt'

numeros = ler_numeros(nome_arquivo)

numeros_inteiros = list(map(int, numeros))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros_inteiros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

cinco_maiores_pares = numeros_pares_ordenados[:5]

soma_cinco_maiores = sum(cinco_maiores_pares)

print(cinco_maiores_pares)
print(soma_cinco_maiores)
