'''
Exemplo 1
num = 51
res = num % 2
print(f"O Palmeiras tem {res} mundial!!!!")
'''
#Se o resto da divisão de um número por 2 for igual a zero, então o número é PAR, senão o número é ÍMPAR
num = int(input("Digite um número inteiro qualquer: "))

res = num%2
if (res == 0):
    print(f"O número {num} é par, o resto é {res}")
else: print(f"O número {num} é ímpar, o resto é {res}")