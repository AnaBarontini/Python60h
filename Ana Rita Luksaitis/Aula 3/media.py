#Criar um sistema que receba o nome de um aluno e a nota de 4 bimestres, calcule e exiba a média aritimética dessas notas.
'''
FLUXOGRAMA
Informar o nome do aluno
Guardar o nome do aluno
Informar a nota do primeiro bi
Guardar a nota do primeiro bi
Informar a nota do segundo bi
Guardar a nota do segundo bi
Informar a nota do terceiro bi
Guardar a nota do terceiro bi
Informar a nota do quarto bi
Guardar a nota do quarto bi
Guardar a media pela soma das notas de todos os bimestres e dividir por 4
Informar nome e media do aluno
Se a média final do aluno for maior ou igual a 7, então ele está aprovado.
Se a média final do aluno for maior que 6.5, então ele está de conselho de classe.
Se a média final do aluno for maior ou igual a 5, então ele está de recuperação.
Senão, ele está reprovado.
'''

n1= 0.0
n2= 0.0
n3= 0.0
n4= 0.0
media= 0.0
nome = ""

#início das entradas do usuário
nome = input("Informe o nome do aluno: ")
n1 = float(input("Informe a nota do primeiro bimestre: "))
n2 = float(input("Informe a nota do segundo bimestre: "))
n3 = float(input("Informe a nota do terceiro bimestre: "))
n4 = float(input("Informe a nota do quarto bimestre: "))

#processamento das informações
media = (n1 + n2 + n3 + n4) / 4

#saída dos resultados
if (n1 < 0 or n1 > 10) or \
(n2 < 0 or n2 > 10) or \
(n3 < 0 or n3 > 10) or \
(n4 < 0 or n4 > 10):
    print("Nota inválida. Por favor digite um número entre 0 e 10")
else:
    if media >= 7:
        print(f"O aluno {nome} teve média final de {media} e foi aprovado.")
    elif media > 6.5 :
        print(f"O aluno {nome} teve média final de {media} e está de conselho de classe.")
    elif media >= 5 :
        print(f"O aluno {nome} teve média final de {media} e está de recuperação.")
    else:
        print(f"O aluno {nome} teve média final de {media} e foi reprovado.")





