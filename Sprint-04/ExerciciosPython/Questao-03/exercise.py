from functools import reduce

def calcula_saldo(lancamentos) -> float:

    valores_transformados = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)

    saldo_final = reduce(lambda x, y: x + y, valores_transformados, 0)

    return saldo_final

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

resultado = calcula_saldo(lancamentos)
print("Saldo final:", resultado)
