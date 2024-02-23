import random

lista_numeros = [random.randint(1, 1000) for _ in range(250)]

print("Lista original:")
print(lista_numeros)

lista_numeros.reverse()

print("Lista apos aplicar o metodo reverse:")
print(lista_numeros)
