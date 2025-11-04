#exemplo de rifa com sorteio no python
from random import choice
nomes = []
c = 0 #variável iniciadora laço WHILE

while c < 11:
    nome = input("Nome do comprador: ")
    nomes.append(nome)
    c+=1
print(f"Nomes do sorteio: {nomes}")
sorteado = choice(nomes)
print(f"O ganhador foi {sorteado}")

