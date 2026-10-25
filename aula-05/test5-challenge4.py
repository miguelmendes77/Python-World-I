from math import sqrt

a2 = float(input('Digite o valor do cateto adjacente: '))
b2 = float(input('Digite o valor do cateto oposto: '))

resul = (a2 ** 2 + b2 ** 2)

raiz = sqrt(resul)

print('A hipotenusa dos valores inseridos é {:.0f}.' .format(raiz))