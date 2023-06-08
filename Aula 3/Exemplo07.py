# Variáveis para os números e o resultado
n1 = 0
n2 = 0
resultado = 0

# Função para somar dois números e exibir o resultado
def somar_numeros(numero1, numero2):
    resultado = numero1 + numero2
    print(f"A soma dos números é: {resultado}")

# Algoritmo Principal
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
somar_numeros(n1, n2)
