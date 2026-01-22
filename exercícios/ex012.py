valor = float(input('Qual é o valor do produto? R$'))
desconto = valor - (valor * 5/100)
print('O produto que custava {}, na promoção com desconto de 5% vai custar {}'.format(valor, desconto))
