num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2))

elif num2 > num1:
    print('O número {} é maior que {}'.format(num2, num1))

elif num1 == num2:
    print('Os dois numeros {} e {} são iguais!'.format(num1, num2))

input()