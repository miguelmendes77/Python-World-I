n1 = 7
n2 = 77
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[30m'}

print('Os número são {}{}{} e {}{}{}.' .format(cores['pretoebranco'], n1, cores['limpa'], cores['azul'], n2, cores['limpa']))