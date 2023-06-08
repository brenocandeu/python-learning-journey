# Variáveis para as posições de linha e coluna e para a matriz de tamanho 3x3
linha = 0
coluna = 0
mat = [[0] * 3, [0] * 3, [0] * 3]

# Loop for aninhado para preencher a matriz com valores informados pelo usuário
for linha in range(0, 3, 1):
    for coluna in range(0, 3, 1):
        mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))

# Loop for aninhado para exibir os valores da matriz
for linha in range(0, 3, 1):
    for coluna in range(0, 3, 1):
        print(f"[{mat[linha][coluna]}]", end=' ')
    print()
