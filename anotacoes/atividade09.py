##categorias
idade = int(input('Digite a idade do atleta: '))
if idade <=9:
    print('Categoria: MIRIM')
elif idade <=14:
    print('Categoria: Infantil')
elif idade<= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('categoria: SENIOR')
else:
    print('cAtegoria: Master')