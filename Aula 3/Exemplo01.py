# Variáveis para o contador e para o vetor de tamanho 5
cont = 0
vet = [0] * 5

# Loop for para preencher o vetor com valores informados pelo usuário
for cont in range(0, 5, 1):
    vet[cont] = int(input(f"Informe um número para a posição {cont}: "))

# Loop for para exibir os valores do vetor
for cont in range(0, 5, 1):
    print(f"{vet[cont]}", end=' ')
