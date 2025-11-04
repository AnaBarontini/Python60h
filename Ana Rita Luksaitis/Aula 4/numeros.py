#Criar um sistema que receba dois números diferentes.
#Se o primeiro for maior que o segundo, mostrar resultado valor 1 é o maior.
#Senão mostrar valor 2 é o maior.
#Mostrar junto do resultado o número do maior valor.

'''
Fluxograma
1- Receber o primeiro valor.
2- Receber o segundo valor.
3- Se o primeiro for maior que o segundo, exibir essa mensagem.
4- Senão, exibir que o segundo é maior que o primeiro.
'''

#Entrada das variáveis
n1 = float(input("Digite um número qualquer: "))
n2= float(input("Digite outro número qualquer: "))

#Processamento com saída
if n1 == n2:
    print("Os valores devem ser diferentes para comparação.")
else:
    if n1 > n2:
        print(f"O número {n1} é maior que o número {n2}")
    else:
        print(f"O número {n2} é maior que o número {n1}")