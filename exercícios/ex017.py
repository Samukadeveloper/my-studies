import math
catetoO = float(input('Comprimento do cateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoO, catetoA)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))