'''
Criar um sistema onde o usuário irá informar o “salário bruto” e o número de dependentes, e a partir deste valor o sistema irá realizar alguns descontos como mostrado abaixo:
Vale refeição: 4.8% sobre o salário bruto
Vale transporte: 6% sobre o salário bruto
INSS: seguir alíquota da tabela
IRRF: seguir alíquota da tabela
Convenio médico: 4% por dependente + o funcionário
Mostrar a soma de todos os descontos
Mostrar o Salário Liquido

Deve ter o fluxograma de todo o programa e a programação em python salva na pasta aula 5.

Fórmulas para desconto:
Valor * porcentagem
OBS: não é para mostrar o salário bruto mais o desconto, e sim somente o quanto equivalente de desconto para cada situação.
'''

#Entrada das informações
salarioBruto = float(input("Informe o salário bruto: "))
dependentes = int(input("Informe a quantidade de dependentes: "))

#Determinação das variáveis
valeRef = salarioBruto * 0.048
valeTrans = salarioBruto * 0.06

if salarioBruto <= 1518.00:
    inss = salarioBruto * 0.075
elif salarioBruto <= 2793.88:
    inss = salarioBruto * 0.09
elif salarioBruto <= 4190.83:
    inss = salarioBruto * 0.12
else:
    inss = salarioBruto * 0.14
    
if salarioBruto <= 1903.98:
    irrf = 0
elif salarioBruto <= 2826.65:
    irrf = salarioBruto * 0.075
elif salarioBruto <= 3751.05:
    irrf = salarioBruto * 0.15
elif salarioBruto <= 4664.68:
    irrf = salarioBruto * 0.225
else:
    irrf = salarioBruto * 27.5
    
convMed = salarioBruto * (0.04 * (1 + dependentes))

#Processamento
descTotal = valeRef + valeTrans + inss + irrf + convMed

salarioLiquido = salarioBruto - descTotal

#Saída
print(f"Os descontos aplicados foram: Vale refeição: R${round(valeRef,2)}, Vale Transporte: R${round(valeTrans,2)}, INSS: R${round(inss,2)}, IRRF: R${round(irrf,2)}, Convênio Médico: R${round(convMed,2)}")
print(f"O total de desconto foi R${round(descTotal,2)}, e o salário líquido é R${round(salarioLiquido,2)}.")