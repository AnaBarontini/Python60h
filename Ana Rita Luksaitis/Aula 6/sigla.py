"""Crie um sistema onde o usuário informa o estado (SIGLA) que está fazendo a compra e o valor total da compra.
Se o estado for SP ou a compra maior que R$100, exibir a mensagem "CUPOM DE FRETE GRÁTIS".
Senão exibir "FRETE para o seu estado de R$19,99"""

#Entrada
estado = str(input("Informe a sigla do estado da compra: "))
valorTotal = float(input("Informe o valor totl da compra:"))

#Processamento
if (estado=="SP" or valorTotal > 100.00):
    frete = "CUPOM DE FRETE GRÁTIS!!!"
else:
    frete = "FRETE para o seu estado de R$19,99."

#Saída    
print(frete)