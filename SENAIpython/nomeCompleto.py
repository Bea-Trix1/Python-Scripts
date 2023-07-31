nome = input('Digite seu nome completo: ')
print('Seu nome completo é: {}'.format(nome))

nome = nome.split()
# nome = nome.split(), nome.strip()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu Ultimo nome é: {}'.format(nome[-1]))

input()
