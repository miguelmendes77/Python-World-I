v1 = int(input('Digite um valor para soma: '))
v2 = int(input('Digite um valor para soma: '))

s = v1 + v2
m = v1 * v2
d = v1 / v2
e = v1 ** v2

print('O valor da soma é {}.\nO valor da multiplicação é {}.\nO valor da divisão é {}.\nO valor da exponenciação é {}.' .format(s, m, d, e)) # \n é usado para quebrar a linha dentro de um "print".
print('Obrigado por usar o programa!', end=' ') # end='' é usado para não ter quebra de linha entre dois "print", como mostrado no exemplo.
print('Até mais!')