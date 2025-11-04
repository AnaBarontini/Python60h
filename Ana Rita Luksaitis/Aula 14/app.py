import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Valores fixos para os meses de janeiro a junho
valores_fixos = [200,200, 200, 200, 200, 200]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

def gerar_grafico():
    try:
        # Coleta os pesos digitados
        pesos = [float(entry.get()) for entry in entradas]
        # Aplica os pesos aos valores fixos
        valores_ponderados = [v * p for v, p in zip(valores_fixos, pesos)]

        # Gera o gráfico
        plt.figure(figsize=(8, 4))
        plt.bar(meses, valores_ponderados, color='skyblue')
        plt.title("Evolução Semestral com Pesos")
        plt.xlabel("Meses")
        plt.ylabel("Valor Ponderado")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos nos campos de peso.")

# Interface gráfica
root = tk.Tk()
root.title("App de Evolução Semestral")

tk.Label(root, text="Digite os pesos para cada mês:").grid(row=0, column=0, columnspan=2, pady=10)

entradas = []
for i, mes in enumerate(meses):
    tk.Label(root, text=f"{mes} (valor fixo: {valores_fixos[i]})").grid(row=i+1, column=0, sticky='e', padx=5)
    entrada = tk.Entry(root)
    entrada.grid(row=i+1, column=1, padx=5)
    entradas.append(entrada)

btn = tk.Button(root, text="Gerar Gráfico", command=gerar_grafico)
btn.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()