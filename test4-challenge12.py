dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de KM rodados: '))

pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}' .format(pago))