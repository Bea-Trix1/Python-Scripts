sal = float(input('Digite seu salario: '))

if sal > 1250:
    aumento = sal + (sal * 10/100)
    print('Seu salario agora é R${}'.format(aumento))

else:
    aum = sal +(sal * 15/100)
    print('Seu salario agora é {}'.format(aum))


