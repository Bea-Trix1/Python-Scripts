largura = float(input('Digite a Largura da parede: '))
altura = float(input('Digite a Altura da parede: '))
area = largura * altura

tinta = area / 2

print('A largura é de: {} \nE a altura é de: {} \nA Soma total da área é de: {}m²'.format(largura,altura,area))
print('A quantidade necessaria para pintar a parede é de: {}'.format(tinta))
