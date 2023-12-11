# Questão 06

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

set_a = set(a)
set_b = set(b)

intersecao = set_a.intersection(set_b)

print(list(intersecao))


# Questão 07

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numeros_impares = [numero for numero in a if numero % 2 != 0]

print(numeros_impares)


# Questão 08

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")


# Questão 09

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")


# Questão 10

def remove_duplicatas(lista):
    return list(set(lista))

lista_original = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista_sem_duplicatas = remove_duplicatas(lista_original)
print(lista_sem_duplicatas)


# Questão 11

nome_arquivo = 'arquivo_texto.txt'

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')


# Questão 12

import json

with open('person.json', 'r') as file:
    data = json.load(file)

print(data)


# Questão 13

def my_map(lista, funcao):
    return [funcao(elemento) for elemento in lista]

lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcao_potencia_2 = lambda x: x**2

resultado = my_map(lista_entrada, funcao_potencia_2)

print(resultado)


# Questão 14

def imprimir_parametros(*args, **kwargs):
    result = ""

    result += "\n".join(map(str, args))

    result += "\n" if args and kwargs else ""

    result += "\n".join([f"{key}: {value}" for key, value in kwargs.items()])

    return result

saida = imprimir_parametros(1, 3, 4, 'hello', 'alguma coisa', 20)

print(saida)


# Questão 15

class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lampada = Lampada()

print("A lâmpada está ligada?" if lampada.esta_ligada() else "A lâmpada está desligada.")

lampada.liga()
print("A lâmpada está ligada?" if lampada.esta_ligada() else "A lâmpada está desligada.")

lampada.desliga()
print("A lâmpada está ligada?" if lampada.esta_ligada() else "A lâmpada está desligada.")


# Questão 16

def soma_numeros_string(string_numeros):
    numeros = [int(numero) for numero in string_numeros.split(',')]
    soma = sum(numeros)
    return soma

string_numeros = "1,3,4,6,10,76"

soma_total = soma_numeros_string(string_numeros)
print(soma_total)


# Questão 17

def dividir_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte:2*tamanho_parte]
    parte3 = lista[2*tamanho_parte:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resultado = dividir_lista(lista)
print(*resultado)


# Questão 18

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

valores_unicos = list(dict.fromkeys(sorted(set(speed.values()), key=lambda x: [44, 47, 52, 53, 54].index(x))))

print(valores_unicos)


# Questão 19

import random

random_list = random.sample(range(500), 50)

random_list_sorted = sorted(random_list)

mediana = random_list_sorted[len(random_list_sorted) // 2] if len(random_list_sorted) % 2 != 0 else \
          (random_list_sorted[len(random_list_sorted) // 2 - 1] + random_list_sorted[len(random_list_sorted) // 2]) / 2

media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f"Media: {media:.2f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")


# Questão 20

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a[::-1])
