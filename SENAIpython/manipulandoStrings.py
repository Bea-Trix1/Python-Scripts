nome = str(input('Qual seu nome completo? '))

print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))

nome = nome.strip()
print('Seu nome tem: {} letras'.format(len(nome) - len(' ')))

nome = nome.split()
print('O primeiro nome é "{}" e ele tem {} letras.'.format(nome[0], len(nome[0])))

