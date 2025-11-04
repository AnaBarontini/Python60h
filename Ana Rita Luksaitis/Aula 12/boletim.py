import tkinter as tk
#from tkinter import Tk

comb= tk.Tk() #criando a tela do app
comb.title("Boletim do aluno")
comb.geometry("400x500")
comb.maxsize(800,600)
comb.minsize(300,400)

#funções dos botões

def executar():
    m1= float(n1.get())
    m2= float(n2.get())
    m3= float(n3.get())
    m4= float(n4.get())
    m= (m1 + m2 + m3 + m4) / 4
    
    if n1 > 10 or n2 > 10 or n3 > 10 or n4 > 10:
       mediafinal.set("Nota Inválida.")
       situacao.set("Digite valores de 0 a 10.")
    elif n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0:
       mediafinal.set("Nota Inválida.")
       situacao.set("Digite valores de 0 a 10.")
    elif m>= 7:
        mediafinal.set(m)
        situacao.set("APROVADO")
    elif m>= 5:
        mediafinal.set(m)
        situacao.set("Conselho de Classe")
    else:
        mediafinal.set(m)
        situacao.set("REPROVADO")
        
def limpar():
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n3.delete(0, tk.END)
    n4.delete(0, tk.END)
    mediafinal.set("")
    situacao.set("")
    
#frame do topo do app
topo = tk.Frame(comb, bg="dark blue", padx= 10, pady= 10)
topo.pack(fill= "x")
tk.Label(topo,text="Boletim do Aluno").grid(row=0,column=0)

#frame do conteúdo do app
conteudo = tk.Frame(comb, bg = "dark gray", padx= 10, pady= 10)
conteudo.pack(fill= "both", expand="True")

tk.Label(conteudo, text="Primeira Nota:", font= ("Arial, 16")).grid(row= 0, column= 0, padx= 5, pady= 5)
n1= tk.Entry(conteudo)
n1.grid(row=0, column=1, padx= 5, pady= 5)

tk.Label(conteudo, text="Segunda Nota: ", font= ("Arial, 16")).grid(row= 1, column= 0, padx= 5, pady= 5)
n2= tk.Entry(conteudo)
n2.grid(row=1, column=1, padx= 5, pady= 5)

tk.Label(conteudo, text="Terceira Nota: ", font= ("Arial, 16")).grid(row= 2, column= 0, padx= 5, pady= 5)
n3= tk.Entry(conteudo)
n3.grid(row=2, column=1, padx= 5, pady= 5)

tk.Label(conteudo, text="Quarta Nota: ", font= ("Arial, 16")).grid(row= 3, column= 0, padx= 5, pady= 5)
n4= tk.Entry(conteudo)
n4.grid(row=3, column=1, padx= 5, pady= 5)

tk.Button(conteudo, text= "Calcular", command= executar).grid(row= 6, column= 0, padx= 5, pady= 5)
tk.Button(conteudo, text= "Limpar", command= limpar).grid(row= 6, column= 1, padx= 5, pady= 5)

#frame do rodapé do app
rodape = tk.Frame(comb, bg= "dark orange", padx= 10, pady= 10)
rodape.pack(fill= "x")

tk.Label(rodape, text="Média Final: ", font= ("Arial, 16")).grid(row= 0, column= 1, padx= 5, pady= 5)
mediafinal = tk.StringVar()
tk.Label(rodape, textvariable= mediafinal, font= ("Arial, 18")).grid(row= 1, column= 1)

tk.Label(rodape, text="Situação: ", font= ("Arial, 16")).grid(row= 0, column= 2, padx= 5, pady= 5)
situacao = tk.StringVar()
tk.Label(rodape, textvariable= situacao, font= ("Arial, 18")).grid(row= 1, column= 2)

comb.mainloop() #exibe a tela do aplicativo