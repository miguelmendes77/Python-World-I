v = int(input('Digite a velocidade do carro na avenida (KM): '))

print('\nO LIMITE DE VELOCIDADE DA AVENIDADE É 80 KM!\n')

if v <= 80: 
    print('Você está DENTRO dos limites de velocidade.')
else:
    print('\nVocê ULTRAPASSOU os limites de velocidade e, para cada KM violado, terá uma multa de R$7,00.')
    multa = (v - 80) * 7
    print('\nO total da multa a pagar é de R${:.2f}.' .format(multa))