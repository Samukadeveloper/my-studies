lado = float(input('qual a largura da parede?'))
alto = float(input('qual a altura da parede?'))
resultado = lado*alto
print('Sua parede tem dimensão de {}x{} e sua área é de {}m\u00B2'.format(lado, alto, resultado))
tinta = resultado/2
print('Para pintar essa parede, você precisa de {}l de tinta'.format(tinta))