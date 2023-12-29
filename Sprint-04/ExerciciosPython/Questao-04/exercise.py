def calcular_valor_maximo(operadores, operandos) -> float:

    resultados = map(lambda x: eval(f"{x[1][0]} {x[0]} {x[1][1]}"), zip(operadores, operandos))

    return max(resultados)

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado = calcular_valor_maximo(operadores, operandos)
print("Maior valor obtido:", resultado)
