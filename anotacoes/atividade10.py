##pagando
preco = float(input('Preço do produto: R$'))
print('''Formas de pagamento:[ 1 ] à vista (dinheiro/cheque) [2] à vista no cartão [3] 2x no cartão [4] 3x ou mais no cartão''')
opcao = int(input('Escolha a opção: '))
if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    print(f'2x de R${total / 2:.2f}')
elif opcao == 4:
    parcelas = int(input('Número de parcelas: '))
    total = preco * 1.2
    print(f'{parcelas}x de R${total / parcelas:.2f}')
else:
    total = preco
    print('Opção inválida.')
    print(f'Total: R${total:.2f}')