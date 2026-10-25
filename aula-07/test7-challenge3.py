from random import randint
from time import sleep # Temporizador.

num = randint(1, 5)

print('-' * 45)
print('O COMPUTADOR ESCOLHEU UM NÚMERO ENTRE 1 A 5!')
print('-' * 45)
n1 = int(input('Tente acertar o número entre 1 e 5: '))

print('\nPROCESSANDO\n')
sleep(5)

print('PARABÉNS! Você acertou o número selecionado pelo computador.' if n1 == num else 'ERRO! Infelizmente você errou o número selecionado pelo computador.')
