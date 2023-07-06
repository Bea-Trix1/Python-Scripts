#Tipos de Dados
string = str
numeroInteiro = int
realFalso = float
booleano = bool

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1+ num2

# f ou .format(variavel) pode ser usado para inserir um valor no meio do print,
# sem utilizar , ou + tornando mais simples.

#exemplo usando o .format
print('A soma entre {0} e {1} vale: {2}'.format(num1,num2,soma))

#Exemplo usando f
print(f'A soma entre {num1} e {num2} vale: {soma}')

input()