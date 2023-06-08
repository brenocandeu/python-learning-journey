# Variáveis para armazenar a quantidade de pontos de água na amostra e o tipo da amostra
amostra = 0.0
tipo = ""

# Solicita ao usuário para inserir a quantidade de pontos de água presentes na amostra
amostra = float(input("Informe a quantidade de pontos de água presentes na amostra: "))

# Verifica o tipo da amostra com base na quantidade de pontos de água
if amostra <= 10:
    tipo = "Rochosa"
else:
    if 10 < amostra <= 40:
        tipo = "Firme"
    else:
        if 40 < amostra <= 80:
            tipo = "Pantanosa"
        else:
            tipo = "Quantidade inválida"

# Exibe a quantidade de pontos de água presentes na amostra e o tipo da amostra
print(f"A quantidade de pontos de água presentes na amostra é de: {amostra}. O tipo dessa amostra é: {tipo}")
