casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
meses = int(input('Em quantos meses você vai pagar? '))

mensal = casa / meses

if mensal > sal * (3/100):
    print('Emprestimo negado, você excedeu 30% do seu salario')
    print('Mensalidade: {}'.format(mensal))

else:
    print('Emprestimo aprovado!')
    print('Mensalide: R${}'.format(mensal))
