##lista sem repetir
numeroS = []
while True:
  n = int(input('Digite um número: '))
  if n not in numeros:
  numeros.append(n)
    print('Número adicionado.')
else:
  print('Número duplicado, não adicionado.')
  continuar = input('Quer continuar? [S/N]: ').strip().upper()
  if continuar == 'N':
    break
numeros.sort()
print(f'Os números digitados foram: {numeros}')
