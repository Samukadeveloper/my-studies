'''numero = float(input('Vou pensar em um número entre 0 e 5. Tente adivinhar: '))
print('PROCESSANDO...')
if numero  >= 2:
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez')'''

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensaer em um numero entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você acertou!')
else:
    print('GANHEI! Eu pensei no numero {}'.format(computador))