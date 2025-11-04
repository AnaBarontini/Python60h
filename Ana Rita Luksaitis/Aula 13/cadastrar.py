import csv
import os

arquivo = "cadastro.csv"

'''
if not os.path.exists(arquivo):
    with open(arquivo, "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email"])
        
def cadastrar():
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone:")
    email = input("Digite seu email:")
    with open(arquivo, "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, telefone, email])
        
    print("Cadastro realizado com sucesso!\n")
    
    
def listar():
    print("\nlista de Cadastros")
    with open(arquivo, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print("|".join(linha))
    print()
    
    while True:
        print("1 Cadastrar pessoa")
        print("2 Ver lista de contatos")
        print("3 Sair")
        opcao = input("Escolha uma opção:")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção Inválida, tente novamente.\n")
listar()
'''




import tkinter as tk
comb = tk.Tk()
comb.title("Sistema de Cadastro Senai")
comb.geometry("400x500")

if not os.path.exists(arquivo):
    with open(arquivo, "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email"])
def cadastrar():
    nome = str(nom.get())
    telefone = str(tel.get())
    email = str(eml.get())
    with open(arquivo, "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, telefone, email])
    
def listar():
    print("\nlista de Cadastros")
    with open(arquivo, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print("|".join(linha))
    print()
listar()

def sair():
    comb.destroy()

topo = tk.Frame(comb, padx=10, pady=10)
topo.pack(fill="x")
tk.Label(topo, text="Sistema de Cadastro Senai").grid(row=0, column=0)

conteudo = tk.Frame(comb, bg="white",padx=10, pady=10)
conteudo.pack(fill="both", expand=True)
tk.Label(conteudo, text="Nome", font=("Arial", 16)).grid(row=0, column=0, padx=5, pady=5)
nom = tk.Entry(conteudo)
nom.grid(row=0, column=1, padx=5, pady=5)
tk.Label(conteudo, text="Telefone", font=("Arial", 16)).grid(row=1, column=0, padx=5, pady=5)
tel = tk.Entry(conteudo)
tel.grid(row=1, column=1, padx=5, pady=5)
tk.Label(conteudo, text="Email", font=("Arial", 16)).grid(row=2, column=0, padx=5, pady=5)
eml = tk.Entry(conteudo)
eml.grid(row=2, column=1, padx=5, pady=5)






rodape = tk.Frame(comb, padx=10, pady=10)
rodape.pack(fill="x")
tk.Button(rodape, text="Cadastrar", command=cadastrar).grid(row=0, column= 0)
tk.Button(rodape, text= "Listar", command=listar).grid(row=0, column=1, padx=5, pady=5)
tk.Button(rodape, text="Sair", command=sair).grid(row=0, column= 2)




comb.mainloop()