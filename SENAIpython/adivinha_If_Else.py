import random

num = int(input('Adivinhe qual número o computador escolheu de 0 a 5: '))

escolhaNumero = random.randint(0, 5)

if num == escolhaNumero:
    print('Você acertou! O numero escolhido foi: {}'.format(escolhaNumero))
else:
    print('Você errou! O numero que o computador escolheu foi {}'.format(escolhaNumero))

input()


