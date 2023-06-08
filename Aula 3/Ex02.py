# Variáveis para o contador e o vetor
i = 0
vet = [0] * 10

# Algoritmo para preencher o vetor
for i in range(0, 10, 1):
    vet[i] = int(input(f"Informe um número para a posição {i + 1}: "))

# Algoritmo para imprimir os elementos do vetor em ordem reversa
for i in range(9, -1, -1):
    print(f"{vet[i]}", end=' ')
