##parar
soma = 0
while True:
    n = int(input('digite um número(999 para parar):'))
    if n == 999:
        break
    soma += n
print(f'A soma foi{soma}')
