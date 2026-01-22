from random import shuffle
nomeA = str(input('Primeiro aluno: '))
nomeB = str(input('Segundo aluno: '))
nomeC = str(input('Terceiro aluno: '))
nomeD = str(input('Quarto aluno: '))
lista = [nomeA, nomeB, nomeC, nomeD]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)