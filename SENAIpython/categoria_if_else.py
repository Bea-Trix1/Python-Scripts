from datetime import date

data = date.today()
dataAtual = data.year

ano = int(input('Digite o ano do seu nascimento: '))
calc = (dataAtual - ano)

if calc >= 9:
    print('Classificação: MIRIM! Idade: {}'.format(calc))

elif 9 > calc <= 14:
    print('Classificação: INFANTIL! Idade: {}'.format(calc))

elif 14 > calc <= 19:
    print('Classificação: JÚNIOR! Idade: {}'.format(calc))

elif 19 > calc <= 20:
    print('Classificação: SÊNIOR! Idade: {}'.format(calc))

elif calc > 20:
    print('Classificação: MASTER!')

