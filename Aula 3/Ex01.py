# Variáveis para o contador e o vetor
cont = 0
vet = [0] * 30

# Algoritmo para preencher o vetor
for cont in range(0, 30, 1):
    vet[cont] = int(input(f"Informe um número para a posição {cont + 1}: "))

# Algoritmo para imprimir os elementos nas posições ímpares do vetor
for cont in range(0, 30, 1):
    if cont % 2 != 0:
        print(f"{vet[cont]}", end=' ')
