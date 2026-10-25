nome = str(input('Digite seu nome e sobrenome: '))

print('Seu nome em maiúsculo', nome.upper())
print('Seu nome em minúsculo', nome.lower())
print('Seu nome tem ao todo {} letras.' .format( len(nome.replace(' ', ''))))

nome1 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.' .format(nome1[0], len(nome1[0])))