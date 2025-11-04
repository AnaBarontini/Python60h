import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,marker="o")
plt.title("Exemplo de grafico simples")
plt.xlabel("Eixo x")
plt.ylabeç("Eixo y")


plt.show()


categorias=["A","B","C","D"]
valores=[10,15,7,12]

plt.bar(categorias,valores,color="Skyblue")
plt.title("Exemplo de Gráfico de barras")
plt.show()


valores=[30,20,25,25]
labels=["A","B""C","D"]

plt.pie(valores,labels=labels,autopct="%1.1f%%")
plt.title("Exemplo de grafico de pizza")
plt.show()

#Usuario digita valores separados por virgula
x=list(map(int,input("Digite os valores de X separados por virgula:").split(",")))
y=list(map(int,input("Digite os valores de X separados por virgula:").split(",")))
#criar grafico 
plt.plot(x,y,marker="o")
plt.title("Grafico simples com dado de usuario")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.show