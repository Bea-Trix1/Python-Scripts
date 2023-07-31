velocidade = float(input('Digite a velocidade: '))

# valorMulta = 7 * (velocidade - 80)

if velocidade > 80.0:
    print('Você foi multado!')

valorMulta = 7 * (velocidade - 80)
print('O valor da multa é: R${}'.format(valorMulta))

input()
