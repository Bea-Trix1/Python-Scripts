nome = input('Digite seu nome: \n')

if nome == 'Beatriz':
    print(f'Que Nome bonito,{nome}!!')

elif nome == 'João':
    print('Pé de feijão!')
    print('Bela Historia!')

elif nome in ('Bia', 'Julia', 'Gabi'):
    print('Belo nome!')

elif nome.lower() == 'edu':
    print('Oiee edu!')

elif 4+4 == 8 and 1+1 == 2:
    print('Que conta legal!!')

else:
    print('Seu nome é normal!!')


print('Tenha um bom dia {}'.format(nome))


