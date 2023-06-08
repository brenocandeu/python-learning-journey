# Variáveis para armazenar o número digitado, o maior número, o menor número e o contador
numero = 1
maior = 0
menor = 0
cont = 1

# Loop while para solicitar números ao usuário até que seja digitado o número 0
while numero != 0:
    numero = int(input("Digite um número: "))

    if cont == 1:
        maior = numero
        menor = numero
        cont += 1
    else:
        if numero > maior:
            maior = numero
        
        if numero < menor and numero != 0:
            menor = numero

# Exibe o maior número digitado e o menor número digitado
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
