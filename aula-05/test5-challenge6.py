from random import choice

aluno1 = str(input('Digite o nome: '))
aluno2 = str(input('Digite o nome: '))
aluno3 = str(input('Digite o nome: '))
aluno4 = str(input('Digite o nome: '))
aluno5 = str(input('Digite o nome: '))

lista = [aluno1, aluno2, aluno3, aluno4, aluno5] 
escolhido = choice(lista)

print('O aluno escolhido foi {}.' .format(escolhido))