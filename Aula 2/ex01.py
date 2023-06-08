# Ex01 Aula02

# Variáveis para armazenar o número de pessoas, as idades, o contador, a média, a menor idade e a maior idade
pessoas = 0
idades = 0
i = 0
media = 0.0
menor = 0
maior = 0

# Solicita ao usuário para inserir o número de pessoas
pessoas = int(input("Digite o número de pessoas: "))

# Loop for para obter as idades e calcular a média, a menor idade e a maior idade
for i in range(1, pessoas + 1, 1):
    idades = int(input(f"Digite a idade da {i}ª pessoa: "))

    if i == 1:
        menor = idades
        maior = idades
    else:
        if idades > maior:
            maior = idades

        if idades < menor:
            menor = idades

    media += idades

media = media / pessoas

# Exibe a média das idades, a menor idade e a maior idade
print(f"A média das idades é: {media:,.2f}")
print(f"A menor idade é: {menor}")
print(f"A maior idade é: {maior}")
