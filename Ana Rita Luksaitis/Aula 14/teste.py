teste="aula 14"

def exemplo():
    print(teste)
    num=input("Digite um numero:")
    return num
    
    #chmada da funçõo
exemplo()
print (exemplo())
'''"ry:
    v1=float(input("informe um valor"))
    v2= float(input("Informe o divisio"))

    res=v1/v2'''


res=0
v1=float(input("informe um valor"))
v2= float(input("Informe o divisio"))
if (v2==0):
    print("Não é possivel dividir por zero")
else: 
    res=v1/v2
print(f"Resultado: {res}")