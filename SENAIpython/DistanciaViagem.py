km = float(input('Digite a distância da viagem em Km: '))

if km <= 200:
    valor1 = (km * 0.50)
    print('O preço da passagem de {}km é de R${}'.format(km, valor1))
else:
    valor2 = (km * 0.45)
    print('O preço da passagem de {}km é de: R${}'.format(km, valor2))

input()

