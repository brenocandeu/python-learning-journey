# Variáveis para armazenar a opção da pessoa, a quantidade de pessoas que gostaram de cada produto
pessoa = 1
primeiro_produto = 0
segundo_produto = 0
terceiro_produto = 0

# Loop while para solicitar a opção de produto que a pessoa gostou
while pessoa != 0:
    pessoa = int(input("Qual produto você gostou? Digite 1, 2 ou 3: "))

    # Verifica qual produto foi escolhido e incrementa a contagem correspondente
    if pessoa == 1:
        primeiro_produto += 1
    elif pessoa == 2:
        segundo_produto += 1
    elif pessoa == 3:
        terceiro_produto += 1

# Exibe a quantidade de pessoas que gostaram de cada produto
print(f"Quantidade de pessoas que gostaram do produto 1: {primeiro_produto}")
print(f"Quantidade de pessoas que gostaram do produto 2: {segundo_produto}")
print(f"Quantidade de pessoas que gostaram do produto 3: {terceiro_produto}")
