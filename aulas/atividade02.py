peso = float(input('Insira seu peso (kg):'))
altura = float(input('Insira sua altura(metros):'))

imc = peso /(altura ** 2)

if imc < 18.5:
    print('Abaixo do peso') 

elif imc > 18.5 and imc < 25:
    print('peso ideal')

elif imc > 25 and imc < 30:
    print('acima do peso')  
    
else:
    print('obesidade mórbida')

# and=
# not=
# or=
# if
# passar_na_prova = false
# ficou_de_recuperação = True
# .
# if 1 and 1:
#     print('não fez mais que obrigação')

#     if not passar_na_prova:
#         print('ficou de castigo')
