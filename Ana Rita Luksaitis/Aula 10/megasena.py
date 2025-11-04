#Criar um sistema que o usuário escolhe 6 dezenas entre 1 e 60 e armazene em uma lista vazia,
# o python vai fazer um sorteio de 6 números aleatórios entre 1 e 60 e armazenar em uma outra lista vazia. 
#O programa deve mostrar os números sorteados e os escolhidos pelo usuário na ordem crescente,
#comparar os resultados e caso o resultado da comparação for igual a 6 então apresentar a ,ensagem "NOVO MILIONÁRIO",
#caso o resultado da comparação for igual a 5 então apresentar a mensagem "Parabéns você acertou a quina",
#caso o resultado da comparação for igual a 4 então apresentar a mensagem "Pelo menos ganhou alguma coisa",
#caso contrário exibir "Tente outra vez".


import random

numerosEscolhidos = []
numerosSorteados = []
comuns = []
c = 0 #variável iniciadora laço WHILE

while c < 6:
    nums = int(input("Escolha um números entre 1 e 60: "))
    numerosEscolhidos.append(nums)
    c+=1
print(f"Os números escolhidos por você foram {sorted(numerosEscolhidos)}")
numerosSorteados = list(range(1, 60))
sorteio = random.sample(numerosSorteados, 6)

print(f"Os números sorteados foram {sorted(sorteio)}")

comuns = list(set(numerosEscolhidos) & set(sorteio))
print(f"Os números que você acertou foram: {comuns}")

if comuns == 6:
    print("NOVO MILIONÁRIOOOOOOOOOOOOOOOOOOO! PARABÉNS!!!!!!!!")
elif comuns == 5:
    print("Acertou a quina! UAUUUUUU")
elif comuns == 4:
    print("Acertou a tranca! Muito bom!")
else:
    print("Não foi dessa vezzzzzzzzzzz")