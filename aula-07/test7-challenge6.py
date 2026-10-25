dist = float(input('Digite a distância da sua viagem: '))

print('Você está preste a começar uma viagem de {:.2f} KM.' .format(dist))

if dist <= 200:
    preço = dist * 0.50
else: 
    preço = dist * 0.45

print('O preço da sua passagem será de R${:.2f}.' .format(preço))