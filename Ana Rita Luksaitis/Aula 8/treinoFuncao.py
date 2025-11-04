#Exercícios sem argumento e sem retorno:
#Crie uma função sequencia() que imprima a quantidade de números sequenciais até o informado pelo usuário.

def sequencia():
    num2=int(input("escolha um numero:"))
    contador=1
    while contador<=1:
        print(contador)
        contador+=1
    
#Exercícios com argumento e sem retorno:
#Crie uma função area(L,C) que receba dois número e mostre a área de um ambiente LxC.

def area(l,c):
    print(f"Àrea é igual a {l*c}")
a=int(input("digite a largura:"))
b=int(input("digite o comprimento:"))
print(area(a,b))


#Crie uma função tabuadas(n) que mostre a tabuada do número e dos próximos número recebido.

#criando a função
def exemploTabuada(v):
    while v <= 10:
        print(f"*Tabuada do {v}*")
        i=1
        while(i<=10):
            print(f"{i}x{v}={i*v}")
            i+=1
        
        v += 1
#chamando a função   
num1 = int(input("Informe um número de 1 a 10: "))   
exemploTabuada(num1)


#Exercícios sem argumento e com retorno:
#Crie uma função pi() que retorne o valor 3.14159.

def pi():
    return 3.14159
print(f"Valor de pi é {pi()}")


#Crie uma função converterTemperatura () que retorne a temperaturas de Celsius para Fahrenheit.

def converterTeperatura():
    C = float(input("Digite uma temperatura em graus celsius:"))
    F = (C * 1.8) + 32
    return F
print(f"O valor dessa temperatura em fhdhsgf é {round(converterTeperatura(), 2)}")

#Exercícios com argumento e com retorno:
#Crie uma função perCirculo(raio) que calcule e retorne a área P = 2 * PI * r.

def perCirculo(r):
    return 2 * pi() * r
r = float(input("Digite o raio do círculo:"))
print(f"O valor do perímetro desse círculo é {round(perCirculo(r), 2)}")

#Crie uma função maiorValor(a, b) que retorne o maior valor entre dois números.

def maiorValor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "nenhum, os dois valores são iguais"
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
print(f"O maior valor entre os dois números é {maiorValor(a, b)}")
    
