# numeros = int(input('Numero: '))
# numeros = int(numeros)

n1 = int(input('Numero: '))
n2 = int(input('Numero: '))
n3 = int(input('Numero: '))
n4 = int(input('Numero: '))
n5 = int(input('Numero: '))
n6 = int(input('Numero: '))

lista = [n1, n2, n3, n4, n5, n6]
par = 0

for i in lista:
    if i % 2 == 0:
        par += i
        print('Pares:', i)

print('Soma:', par)



