from random import choice
nomeA = str(input('Primeiro aluno: '))
nomeB = str(input('Segundo aluno: '))
nomeC = str(input('Terceiro aluno: '))
nomeD = str(input('Quarto aluno: '))
lista = [nomeA, nomeB, nomeC, nomeD]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

