#Exibir os números de 1 a 5
for numero in range(1,6):
    print("Numero da sequencia:",numero)
    
print("Fim do laço FOR")

#Exibir elemento da lista um por vez
lista=[1,5,7,11,4,8,9]

for i in lista:
    print("Valor do i:",i)
print("fim do laço com a lista")

#MOSTRAR NÚMEROS E SEU DOBRO 
numeros=[1,2,3,4]
for num in numeros:
    print(f"{num}x2= {num*2}")
print("fim do laço min tabuada")

#somar todos os números de uma lista
valores=[5,8,2,10,11,-7,71,51]
soma=0 
for v in valores:
    soma +=v
    
print(f"soma total: {soma}")

#exemplo While com numeros fixos
contador=40
while contador<50:
    print(contador)
    contador+=5
print("fim do laço while")

#exemplo de while criando um vetor
quantidade = int(input("quantos valores deseja adicionar?"))
valores = []
i=0
while i < quantidade:
    valor=input(f"digite o {i+1}° valor:")
    valores.append(valor)
    i+=1
print("lista criada:",valores)

#exemplo de while com texto
dados=[]
while True:
    item=input("Digite um valor (ou 'sair' para terminar):")
    if item=='sair':
        break
    dados.append(item)
print("Valores digitados:",dados)
    