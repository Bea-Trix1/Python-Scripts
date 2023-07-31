nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

# print('Aprovado' if media >= 7.0 else 'Reprovado')

if media >= 7.0:
 print('Você foi aprovado com a media {}!'.format(media))
else:
    print('Você foi reprovado com a media {}!'.format(media))


