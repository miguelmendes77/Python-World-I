cidade = str(input('Digite o nome da sua cidade: '))

cidade = cidade.title()

print(cidade)

print('Sua cidade começa com santos? (TRUE - SIM | FALSE - NÃO)')
print(cidade.find('Santo'))
print('Santo' in cidade)

