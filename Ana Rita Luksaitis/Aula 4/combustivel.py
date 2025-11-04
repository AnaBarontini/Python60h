#Criar um sistema que receba do usuário o valor de um litro de álcool e o valor de um litro de gasolina. 
#Calcular a relação custo benefício entre os combustíveis.
#Caso a relação for superior a 0.7, então o melhor combst. é GASOLINA, senão, é o ÁLCOOL

'''
Fluxograma
1- Receber valores do preço do álcool por um litro.
2- Receber valores do preço da gasolina por um litro.
3- Calcular o custo benefício divindo álcool pela gasolina.
4- Se o custo for maior que 0.7 exibir que a gasolina é melhor.
5- Senão, exibir que o álcool é melhor.
'''

#Determinação das variáveis
alcool = 0.0
gasolina = 0.0
custoBeneficio = 0.0

#Entrada dos valores
alcool = float(input("Digite o valor do litro do álcool: "))
gasolina = float(input("Digite o valor do litro da gasolina: "))

#Processamento das informações
custoBeneficio = alcool / gasolina

#Saída correspondente
if custoBeneficio > 0.7:
    print("O melhor combustível é a gasolina.")
else:
    print("O melhor combustível é o álcool.")