frase = input('Digite uma frase: ')

# frase = frase.lower(), frase.split(), frase.count('a'), frase.find('a', 0, 20), frase.rfind('a', 0, 20),
print('Sua frase é: {} \n '
      'A frase cortada é: {} \n'
      'A letra A aparece: {} vezes \n'
      'A posição da letra A na primeira vez é: {} \n'
      'A posição na segunda vez é: {} \n'
      .format(frase,
               frase.split(),
                frase.count('a'),
                frase.find('a', 0, 20),
                frase.rfind('a', 0, 20)))

