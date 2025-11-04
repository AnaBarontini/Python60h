import tkinter as tk #chamando biblioteca de criação de telas
from tkinter import messagebox

#variável de criação do aplicativo
app = tk.Tk() #criando a tela da interface
app.title("Exemplo de APP")
app.geometry("900x700")
label = tk.Label(app, text="Olá mundo!!!!", font="verdana, 22")
label.pack()
texto= tk.Entry(app)
texto.pack()
def clique():
    nome = texto.get()
    messagebox.showinfo ("Bem vindo!!!", "Oi " +nome+" você clicou no botão :)")
botao = tk.Button(app, text="Clique em mim", command = clique)
botao.pack()

app.mainloop() #mantem a aplicação aberta 