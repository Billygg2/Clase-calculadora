import tkinter as tk
from operaciones import sumar, restar, multiplicar, dividir
# Billy
def iniciar_ui():
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("300x400")

    entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
    entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

    operacion = {"op": None, "valor": None}

    def click(valor):
        entrada.insert(tk.END, valor)

    def limpiar():
        entrada.delete(0, tk.END)
        operacion["op"] = None
        operacion["valor"] = None

    def set_operacion(op):
        operacion["valor"] = float(entrada.get())
        operacion["op"] = op
        entrada.delete(0, tk.END)
# Isaac
    def calcular():
        b = float(entrada.get())
        a = operacion["valor"]
        op = operacion["op"]

        if op == "+":
            resultado = sumar(a, b)
        elif op == "-":
            resultado = restar(a, b)
        elif op == "*":
            resultado = multiplicar(a, b)
        elif op == "/":
            resultado = dividir(a, b)
        else:
            return

        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)

    botones = [
        ("7", lambda: click("7")), ("8", lambda: click("8")), ("9", lambda: click("9")), ("/", lambda: set_operacion("/")),
        ("4", lambda: click("4")), ("5", lambda: click("5")), ("6", lambda: click("6")), ("*", lambda: set_operacion("*")),
        ("1", lambda: click("1")), ("2", lambda: click("2")), ("3", lambda: click("3")), ("-", lambda: set_operacion("-")),
        ("0", lambda: click("0")), ("C", limpiar), ("=", calcular), ("+", lambda: set_operacion("+")),
    ]

    fila = 1
    col = 0
    for texto, accion in botones:
        tk.Button(ventana, text=texto, width=5, height=2, command=accion)\
            .grid(row=fila, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            fila += 1

    ventana.mainloop()
