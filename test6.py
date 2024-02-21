nome = str('Miguel Araújo Ferreira Mendes')

# print(nome[7]) - Nesse print colocamos a variável e um valor entre colchetes para exibir a letra equivalente a 7 na sequência de caracteres da String.
# print(nome[7:13]) - Nesse print segue o mesmo princípio, porém agora irá exibir os caracteres de 7 a 12, ignorando a última casa.
# print(nome[7:13:2]) - Nesse print exibirá os caracteres de 7 a 12, com salto de 2.
# print(nome[:7]) - Nesse print como não exibi valor de início, por padrão, começará do 0 e mostrará a sequência de caracteres de 0 a 6.
# print(nome[14:]) - Nesse print o valor de início é 14 e seguirá até o último caracter, independente do tamanho da sequência.
# print(nome[0::4]) - Nesse print começará do zero, irá até o final, com salto de 4.
# print(len(nome)) - Mostra a quantidade de caracteres tem a String.
# print(nome.count('e', 0, 13)) - Mostra a quantidade de caracteres colocado como valor, como no exemplo acima. É possível usar o fatiamento.
# print(nome.find('újo')) - Mostra onde começa determinado conjunto de caracteres. Se a função retornar o valor (-1) significa que a sequência de caracteres não existe dentro da String.
# print('Mendes' in nome) - Confirma se a palavra em questão está na frase.
# print(nome.replace('Mendes', 'Black')) - Substitui em "segundo plano" alguma palavra na string. Não altera a string propriamente, apenas altera a exibição, como no exemplo.
# print(nome.upper()) - Deixa todos os caracteres em maiúsculo.
# print(nome.lower()) - Deixa todos os caracteres em minúsculo.
# print(nome.capitalize()) - Pega todos os caracteres da String e somente a primeira letra de toda String fica maiúscula.
# print(nome.title()) - Pega todas as primeiras letras depois de um espaço e coloca elas maiúsculas.
# print(nome.strip()) - Remove todos os espaços inúteis no começo e fim da String. Se configurar "print(nome.rstrip())" remove somente os espaços do lado direito e "print(nome.lstrip())" somente os espaços do lado esquerdo.
# print(nome.split()) - Ocorre uma divisão dentro da sua String considerando os espaços. Ele gera tecnicamente uma lista com cada elemento será separado pelo espaço.
# print(''.join(nome)) - Junta todos os caracteres novamente.