#função sem argumento e sem retorno 
def primeiraFuncao():
    print("Olá Mundo!!!")
    
#invocando a função sem argumento e sem retorno
primeiraFuncao()

#função com argumento e sem retorno
def somarValores(x,y):
    v1=x
    v2=y
    print(f"{v1}+{v2}={v1+v2}")
#invocando função com argumento
a=int(input("digite o primeiro valor:"))
b=int(input("digite o segundo valor:"))
somarValores(a,b)

#função sem argumento e com retorno 
def mostrarTexto():
    return "Olá meu nome é ximbinha"
texto=mostrarTexto()
print(texto)

#função com argumento e com retorno 
def areaQuad(x):
    return x**2
#invocando a função
z=int=int(input("informe a medida que deseja calcular:"))
y=areaQuad(z)
print("Area ao quadrado",y)