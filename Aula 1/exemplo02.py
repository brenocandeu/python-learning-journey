# Variáveis para armazenar o nome, situação e notas do aluno
nome = ""
situacao = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

# Solicita ao usuário para inserir o nome do aluno
nome = input("Informe o nome do aluno: ")

# Solicita ao usuário para inserir a nota 1 do aluno
nota1 = float(input("Informe a nota 1: "))

# Solicita ao usuário para inserir a nota 2 do aluno
nota2 = float(input("Informe a nota 2: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Verifica a situação do aluno com base na média
if media >= 6:
    situacao = "Aprovado"
else:
    if 4 <= media < 6:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

# Exibe a média e a situação do aluno
print(f"{nome}, a sua média é: {media} e você está {situacao}")
