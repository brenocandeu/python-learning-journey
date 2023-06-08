# Variáveis para armazenar a idade, sexo, contador, soma das idades, idade média, quantidade de mulheres e quantidade de maiores de idade
idade = 0
sexo = ""
i = 0
soma_idade = 0
idade_media = 0.0
quant_mulheres = 0
quant_maiores = 0

# Loop for para solicitar a idade e o sexo de cada pessoa
for i in range(1, 21, 1):
    idade = int(input(f"Informe a idade da {i}ª pessoa: "))
    sexo = input(f"Informe o sexo da {i}ª pessoa (M/F): ")
    sexo_final = sexo.upper()
    soma_idade += idade

    # Verifica se a turma já está lotada (20 pessoas)
    if i >= 20:
        print("Turma já está lotada!!!")

    # Verifica se o sexo é feminino e incrementa a quantidade de mulheres
    if sexo_final == "F":
        quant_mulheres += 1

    # Verifica se a idade é maior ou igual a 18 e incrementa a quantidade de maiores de idade
    if idade >= 18:
        quant_maiores += 1

# Calcula a idade média dos candidatos
idade_media = soma_idade / 20

# Exibe a idade média, a quantidade de mulheres inscritas e a quantidade de alunos maiores de idade
print(f"A idade média dos candidatos é: {idade_media}")
print(f"A quantidade de mulheres inscritas é: {quant_mulheres}")
print(f"A quantidade de alunos maiores de idade é: {quant_maiores}")
