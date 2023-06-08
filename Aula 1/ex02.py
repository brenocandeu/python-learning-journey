# Variáveis para armazenar o preço de fábrica, percentual de lucro, percentual de imposto e o custo total
preco_fabrica = 0.0
porcentual_lucro = 0
porcentual_imposto = 0
total = 0.0

# Solicita ao usuário para inserir o preço de fábrica do veículo
preco_fabrica = float(input("Informe o preço de fábrica do veículo: "))

# Solicita ao usuário para inserir o percentual de lucro do distribuidor
porcentual_lucro = int(input("Informe o percentual de lucro do distribuidor: "))

# Solicita ao usuário para inserir o percentual de imposto a ser pago
porcentual_imposto = int(input("Informe o percentual de imposto a ser pago: "))

# Calcula o valor do lucro do distribuidor
porcentual_lucro = preco_fabrica * porcentual_lucro / 100

# Calcula o valor do imposto a ser pago
porcentual_imposto = preco_fabrica * porcentual_imposto / 100

# Calcula o custo total para o consumidor
total = preco_fabrica + porcentual_lucro + porcentual_imposto

# Exibe o lucro do distribuidor
print(f"O lucro do distribuidor é de: {porcentual_lucro:,.2f}")

# Exibe o valor do imposto a ser pago
print(f"O valor do imposto a ser pago é de: {porcentual_imposto:,.2f}")

# Exibe o custo total para o consumidor
print(f"O custo ao consumidor é: {total:,.2f}")
