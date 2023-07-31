import random

aluno1 = input('Digite o nome do primero aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
aluno5 = input('Digite o nome do quinto aluno: ')

Lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
Sorteado = random.choice(Lista)

print('O sorteio foi: {}'.format(Sorteado))
input()
