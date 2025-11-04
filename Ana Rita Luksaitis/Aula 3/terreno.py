'''Criar um sistema que calcule o perímetro de um terreno onde o 
usuário vai informar as medidas de largura e profundidade do terreno 
e exibir o total de contorno desse terreno.'''

'''
Fluxograma
Informar a variável da largura
Guardar a largura
Informar a variável da profundidade
Guardar a profundidade
Declarar o perímetro por meio do dobro da largura mais o dobro da profundidade 
'''

#Declaração de variáveis
larg = 0.0
prof = 0.0
perim = 0.0

#Entrada das informações
larg = float(input("Digite a largura do terreno em metros: "))
prof = float(input("Digite a profundidade do terreno em metros: "))

#Processamento das informações
perim = (larg * 2) + (prof * 2)

#Saída dos resultados
print(f"A medida do perímetro do terreno é {perim} metros.")
