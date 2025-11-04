# Criar um sista que calcule o volume de um cilindro, ao receber do usuário o valor do raio e o valor da altura

'''
Fluxograma
1- Declarar variáveis
2 - Pedir ao usuário o raio
3 - Armazenar raio
4 - Pedir ao usuário a altura
5 - Armazenar altura
6 - Calcular volume
7 - Informar volume
'''

import math
raio = 0.0
altura = 0.0
volume = 0.0

#entrada das informações do usuário
raio = float(input("Informe o raio do cilindro: "))
altura = float(input("Informe a altura do cilindro: "))

#processamento das informações

volume = (math.pi*(raio**2))*altura

#resposta pro usuário
print(f"O volume desse cilindro é {volume}")