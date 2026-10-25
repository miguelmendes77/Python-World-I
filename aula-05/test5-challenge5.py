from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.' .format(ang, seno, cosseno, tangente))