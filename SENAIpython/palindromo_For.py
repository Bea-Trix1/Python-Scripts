frase = input('Digite um palavra: ').upper().replace(' ', '')

if frase == frase[:: -1]:
    print('A palavra é frasendroma')
    print('Palavra Invertida: {}'.format(frase))
else:
    print('A palavra não é ndroma')
    print('Palavra Digitada: {} '.format(frase))
