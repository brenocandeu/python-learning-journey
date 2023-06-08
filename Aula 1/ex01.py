# Variáveis para armazenar o salário e o salário final
salario = 0.0
salario_final = 0.0

# Solicita ao usuário para inserir o salário
salario = float(input("Digite o seu salário: "))

# Calcula o salário final, aplicando um desconto de 10% e adicionando 50
salario_final = (salario * 90 / 100) + 50

# Exibe o salário final
print(f"Seu salário é de: {salario_final}")
