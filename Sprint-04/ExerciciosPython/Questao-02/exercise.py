def conta_vogais(texto: str) -> int:

    vogais = ['a', 'e', 'i', 'o', 'u']

    vogais_presentes = list(filter(lambda x: x.lower() in vogais, texto))

    return len(vogais_presentes)

texto_exemplo = "Oi testando"
resultado = conta_vogais(texto_exemplo)
print("Contagem de vogais:", resultado)