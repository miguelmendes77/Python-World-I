l = int(input('Digite a largura da parede: '))
a = int(input('Digite a altura da parede: '))

area = l * a
tinta = area // 2

print('Área da parede é {} m². A quantidade necessária de tinta para pitar toda a área da parede é de {}.' .format(area, tinta))