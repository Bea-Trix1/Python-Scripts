from datetime import date

data = date.today()
dataAtual = data.year

ano = int(input('Digite o ano do seu nascimento: '))
calc = (dataAtual - ano)

if calc < 18:
    tempo = calc - 18
    print('Você ainda vai se alistar! Falta {} anos'.format(tempo))

elif calc == 18:
    print('Está na hora de você se alistar!')

else:
    tempo = calc - 18
    print('Já passou {} anos para o seu alistamento!'.format(tempo))

