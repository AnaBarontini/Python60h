#comentário de uma linha no python

'''
comentário
de
múltiplas
linhas
'''

"""
esse também
"""
'''
nome = "Ana Rita" #criando uma váriavel do tipo string
v1 = int(input("Digite um valor: "))
v2 = 2.5
v3 = int(input("Digite um número inteiro qualquer: "))

print("Olá mundo!")
print("Meu nome é", nome)
print("12² é igual a", 12**2)
print(f"{v3} x {v1} = {v3 * v1}")
'''


#calculadora com 4 operações

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

#processamento das informações

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
#excessão
if (n2 == 0):
    div = "Não é possível dividir por zero."
else:
    div = n1 / n2

#saída do programa
print(f"Soma de {n1} + {n2} = {soma}")
print(f"Subtração de {n1} - {n2} = {sub}")
print(f"Multiplicação de {n1} x {n2} = {multi}")
print(f"Divisão de {n1} / {n2} = {div}")

