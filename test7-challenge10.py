print('-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-' * 20)

r1 = float(input('Digite um segmento: '))
r2 = float(input('Digite um segmento: '))
r3 = float(input('Digite um segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segments acima NÃO PODEM FORMAR um triângulos')