alunoA = float(input("Primeira nota do aluno:"))
alunoB = float(input("Segunda nota do aluno:"))
alunoC = float(input("Terceira nota do aluno:"))

resultadoSoma= (alunoA + alunoB + alunoC)
resultadoFinal = (resultadoSoma/3)

print('A média entre {}, {} e {} foi {:.2f}'.format(alunoA, alunoB, alunoC, resultadoFinal))