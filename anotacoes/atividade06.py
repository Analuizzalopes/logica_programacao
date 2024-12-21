##Análise de uma frase
frase = input('Digite uma frase: ').upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes.') 
print(f'A primeira aparece na posição {frase.find("A") + 1}.')
print(f'A última aparece na posição {frase.rfind("A") + 1}.')
