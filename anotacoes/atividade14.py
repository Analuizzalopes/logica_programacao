##par ou impar brincando
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número: ')) computador = randint(0, 10) total = jogador + computador escolha =''
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
        if escolha == 'P' and total % 2 == 0 or escolha == 'I' and total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
print(f'Você venceu {vitorias} vezes.')
