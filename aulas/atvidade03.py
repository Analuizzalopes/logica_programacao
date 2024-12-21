# entrada da informação do usuário >> Número para calcular
# Pedir para que o usuário digite um número qualquer

# processamento dessa informação >> Calcular tabuada
# Com base no número digitado eu quero que a tabuada dele seja calculada

# resultado do processamento >> Exibir tabuada
# Com base no resultado da tabuada calculada que ela seja exibida para mim


# Tabuada do número 9
numero = 9
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")