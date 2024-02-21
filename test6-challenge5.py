frase = str(input('Digite uma frase: '))
frase = frase.upper()

print('Quantidade de vezes que aparece a letra "A":', frase.count('A'))
print('A letra "A" aparece pela primeira vez na posição:', frase.find('A')+1)
print('A letra "A" aparece pela última vez na posição:', frase.rfind('A')+1)