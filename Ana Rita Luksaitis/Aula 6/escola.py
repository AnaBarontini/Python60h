"""Crie um sistema que receba a média final do aluno e a quatidade de faltas,
caso a nota seja maior ou igual a 7 e a quantidade de faltas for menor ou igual a 4,
então mostrar ALUNO APROVADO, senão mostrar ALUNO REPROVADO.
"""

mediaFinal = float(input("Informe a média final do aluno: "))
qntdFaltas = int(input("Informe a quantidade de faltas do aluno: "))

if(mediaFinal >= 7 and qntdFaltas <= 4):
    print("ALUNO APROVADO")
else:
    print("ALUNO REPROVADO")