import math

oposto = int(input('Digite o comprimento do cateto oposto: '))
adjacente = int(input('Digite o comprimento do adjacente: '))
soma = math.cos(oposto) + math.tan(adjacente)
hipotenusa = math.sqrt(2)

print('A hipotenusa é igual a: {:}'.format(hipotenusa))

