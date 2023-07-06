preco = float(input('Digite o preço do produto: '))

desconto = preco * 5 / 100
valorFinal = preco - desconto

print('O preço do seu produto com Desconto é de: {}'.format(valorFinal))
