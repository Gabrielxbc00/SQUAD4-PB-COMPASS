# Questão 01

ano_atual = 2023

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_100 = ano_atual + (100 - idade)

print(ano_100)


# Questão 02

for i in range(3):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)


# Questão 03

for numero in range(0, 21, 2):
    print(numero)


# Questão 04

def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

for numero in range(1, 101):
    if is_primo(numero):
        print(numero)


# Questão 05

dia = 22
mes = 10
ano = 2022

print(f"{dia}/{mes}/{ano}")
