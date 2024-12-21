##Nome completo
nome = input('Digite seu nome completo: ').strip() 
print(f'Maiúsculas: {nome.upper()}') 
print(f'Minúsculas: {nome.lower()}') 
print(f'Letras ao todo (sem espaços): {len(nome.replace("", ""))}') 
print(f'Primeiro nome: {nome.split() [0]} ({len(nome.split()[0])} letras)')
