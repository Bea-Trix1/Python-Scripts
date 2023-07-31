nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('REPROVADO!Média: {}'.format(media))

elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO! Média: {}'.format(media))

elif media >= 7.0:
    print('APROVADO!Média: {}'.format(media))

input('')
