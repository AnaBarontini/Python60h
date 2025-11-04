import tkinter as tk

calc = tk.Tk()
calc.title("Calculadora Básica")
calc.geometry("300x500")

tk.Label(calc, text= "Valor 1:").grid(row=0, column=0, padx=3, pady=3)
txtValor1 = tk.Entry(calc)
txtValor1.grid(row=0, column=1, padx=3, pady=3)

tk.Label(calc, text= "Valor 2:").grid(row=1, column=0, padx=3, pady=3)
txtValor2 = tk.Entry(calc)
txtValor2.grid(row=1, column=1, padx=3, pady=3)

#funções

resposta = tk.StringVar()
    
def somar():
    v1 = float(txtValor1.get())
    v2 = float(txtValor2.get())
    somar = v1 + v2
    resposta.set(somar)
    
def subtrair():
    v1 =float( txtValor1.get())
    v2 = float(txtValor2.get())
    subtrair = v1 - v2
    resposta.set(subtrair)
    
def multiplicar():
    v1 = float(txtValor1.get())
    v2 = float(txtValor2.get())
    multiplicar = v1 * v2
    resposta.set(multiplicar)
    
def dividir():
    v1 = float(txtValor1.get())
    v2 = float(txtValor2.get())
    if v2 == 0:
        resposta.set("Não é possível dividir por zero.")
    else:   
        dividir = v1 / v2
        resposta.set(dividir)
    
def potencia():
    v1 = float(txtValor1.get())
    v2 = float(txtValor2.get())
    potencia = v1 ** v2
    resposta.set(potencia)
    
    
#botões de comando
btnSomar = tk.Button(calc, text = "+", command = somar)
btnSomar.grid(row=2, column=0, padx=3, pady=3)
btnSubtrair = tk.Button(calc, text = "-", command = subtrair)
btnSubtrair.grid(row=2, column=1, padx=3, pady=3)
btnMultiplicar = tk.Button(calc, text = "*", command = multiplicar)
btnMultiplicar.grid(row=2, column=2, padx=3, pady=3)
btnDividir = tk.Button(calc, text = "/", command = dividir)
btnDividir.grid(row=2, column=3, padx=3, pady=3)
btnPotencia = tk.Button(calc, text = "^", command = potencia)
btnPotencia.grid(row=2, column=4, padx=3, pady=3)

#resultado
tk.Label(calc, text="Resultado: ").grid(row=3, column=0, padx=3, pady=3)
tk.Label(calc, textvariable = resposta).grid(row=3, column=1, padx=3, pady=3)


calc.mainloop()