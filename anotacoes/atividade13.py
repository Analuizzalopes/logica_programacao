while True:
idade = int(input('Idade: '))
sexo =
while sexo not in 'MF':
sexo = input('Sexo [M/F]: ').strip().upper()[0]
if idade > 18: maior18 += 1
if sexo == 'M':
homens += 1
if sexo == 'F' and idade < 20:
mulheres20 += 1
continuar =
while continuar not in 'SN':
continuar = input('Quer continuar? [S/N] ').strip().upper() [0]
if continuar == 'N':
    break
print(f'{maior18} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres20} mulheres têm menos de 20 anos.')
