# Variáveis para armazenar o nome e as notas do aluno
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

# Solicita ao usuário para inserir o nome do aluno
nome = input("Informe o Nome do aluno: ")

# Solicita ao usuário para inserir a nota 1 do aluno
nota1 = float(input("Informe a Nota 1: "))

# Solicita ao usuário para inserir a nota 2 do aluno
nota2 = float(input("Informe a Nota 2: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Exibe a média do aluno
print(f"{nome}, a sua média é: {media}")
