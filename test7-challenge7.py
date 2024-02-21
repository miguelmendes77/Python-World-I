from datetime import date

ano = int(input('Digite o ano que deseja analisar (Digite 0 para analisar o ano atual): '))

if ano == 0:
    ano = date.today().year 

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Use "and" para colocar mais condições.
    print('\nO ano {} é BISSEXTO.' .format(ano))
else:
    print('\nO ano {} não é BISSEXTO.' .format(ano))