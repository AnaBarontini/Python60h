#biblioteca nativa do python para sorteio de valores
import random

#sorteio de números inteiros definidos pelo usuário entre um menor e um maior
numero = random.randint(1, 10)
print(numero) #pode ser qualquer número de 1 a 60

#sorteio de múmeros decimais entre 0 e 1
decimal = random.random()
print(round(decimal,2))

#sorteio de um valor determinado por uma lista
cores =  ["vermelho", "verde", "azul"]

cor = random.choice(cores)
print(cor) #Pode ser 'vermelho', 'azul' ou 'verde'

#cria uma lista de uma quantidade de elementos definidos pelo usuário
numeros = list(range(1, 61))
sorteio = random.sample(numeros, 6)
print(sorteio)

#embaralha os valores d euma lista e apresenta em ordens aleatórias
cartas = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(cartas)
print(cartas)

#reorganiza valores de uma lista
valores = [8, 12, 5, 3, 71, 9, 101]
print(sorted(valores))

#compara duas listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comuns = list(set(lista1) & set(lista2))
print(comuns)