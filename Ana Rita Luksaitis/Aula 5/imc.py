'''
Cálculo do IMC
'''

peso = 0.0
alt = 0.0
imc = 0.0

#Entrada
peso = float(input("Informe seu peso: "))
alt = float(input("Informe sua altura: "))

#Processamento
imc = peso / alt**2

#Saída
if imc < 18.5:
    print(f"Seu IMC é de: {round(imc,1)}, e está abaixo do peso.")
elif imc < 24.9:
    print(f"Seu IMC é de: {round(imc,1)}, e está com peso normal.")
elif imc < 29.9:
    print(f"Seu IMC é de: {round(imc,1)}, e está em sobrepeso.")
elif imc < 34.9:
    print(f"Seu IMC é de: {round(imc,1)}, e está em obesidade 1.")
elif imc < 39.9:
    print(f"Seu IMC é de: {round(imc,1)}, e está em obesidade 2.")
else:
    print(f"Seu IMC é de: {round(imc,1)}, e está em obesidade 3.")
    


