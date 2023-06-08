# Variáveis para a linha, coluna e matriz
linha = 0
coluna = 0
mat = [[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5]

# Algoritmo para preencher a matriz
for linha in range(0, 5, 1):
    for coluna in range(0, 5, 1):
        mat[linha][coluna] = int(input(f"Informe um número para a posição {linha} {coluna}: "))
print()

# Algoritmo para imprimir a matriz
for linha in range(0, 5, 1):
    for coluna in range(0, 5, 1):
        print(f"[{mat[linha][coluna]}]", end=' ')
    print()

print()

# Algoritmo para imprimir os elementos da diagonal principal da matriz
for linha in range(0, 5, 1):
    for coluna in range(0, 5, 1):
        if linha == coluna:
            print(f"[{mat[linha][coluna]}]", end=' ')
