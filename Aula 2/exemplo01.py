# Variáveis para armazenar o contador e o número para a tabuada
contador = 0
numero = 0

# Solicita ao usuário para inserir o número para a tabuada
numero = int(input("Informe o número para a tabuada: "))

# Loop for para calcular e exibir a tabuada do número
for contador in range(1, 11, 1):
    print(f"{numero} X {contador} = {numero * contador}")
