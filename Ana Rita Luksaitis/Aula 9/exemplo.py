#bibliotecas do python
#import math
from math import pi, pow, sqrt
import math as mat
#import numpy as np
import ana as aninha
from ana import dividir

print(f"Valor do pi é {round(pi,)}")
print(f"2 elevado ao cubo é {pow(2,3)}")
print(f"Raíz quadrada de 81 é {sqrt(81)}")
#print(np.array[1, 2, 3, 4])

nome = input("Informe seu nome: ")
print(aninha.boasVindas(nome))

v1 = int(input("Informe um valor qualquer: "))
v2 = int(input("Informe um valor qualquer: "))
print (f"A soma dos valores {v1} e {v2} é: {aninha.somar(v1, v2)}")

a = int(input("Informe o número: "))
b = int(input("Informe o divisor: "))
result = dividir(a, b)
print (f"Resultado da divisão de {a}/{b} é: {result}")