'''
Cria um sistema que receba o número do usuário.
caso este número for 1, então o dia é "DOMINGO",
caso este número for 2, então o dia é "SEGUNDA-FEIRA",
caso este número for 3, então o dia é "TERÇA-FEIRA",
caso este número for 4, então o dia é "QUARTA-FEIRA",
caso este número for 5, então o dia é "QUINTA-FEIRA",
caso este número for 6, então o dia é "SEXTA-FEIRA",
senão o dia é "SÁBADO"
'''

dia = int(input("Informe um número referente ao dia da semana: "))

if (dia == 1):
    print("O dia é DOMINGO")
elif (dia == 2):
    print("O dia é SEGUNDA-FEIRA")
elif (dia == 3):
    print("O dia é TERÇA-FEIRA")
elif (dia == 4):
    print("O dia é QUARTA-FEIRA")
elif (dia == 5):
    print("O dia é QUINTA-FEIRA")
elif (dia == 6):
    print("O dia é SEXTA-FEIRA")
elif (dia == 7):
    print("O dia é SÁBADO")
else: 
    print("Número inválido")