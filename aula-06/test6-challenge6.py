nome = str(input('Digite seu nome: '))

nome = nome.title()
nome = nome.split()

primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print('Primeiro nome: {}' .format(primeiro_nome))
print('Último nome: {}' .format(ultimo_nome))