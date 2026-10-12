def quick_sorte(valores):
    if len(valores) <= 1:
        return valores

    meio = len(valores) // 2
    pivo = valores[meio]

    menores = []
    iguais = []
    maiores = []

    for valor in valores:
        if valor < pivo:
            menores.append(valor)
            continue
        if valor == pivo:
            iguais.append(valor)
            continue
        maiores.append(valor)

    return quick_sorte(menores) + iguais + quick_sorte(maiores)

print(quick_sorte([5, 2, 9, 1, 6, 3]))