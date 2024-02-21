p = float(input('Digite o preço do produto: '))

d = p * 0.05
pd = p - d

print('O valor do produto (R${:.0f}) com 5% de desconto (R${:.2f}) é de R${:.2f}.' .format(p, d, pd))