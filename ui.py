import tkinter as tk
from operaciones import sumar, restar, multiplicar, dividir
# Billy #
def iniciar_ui():
    ventana = tk.Tk()
    ventana.title("Calculadora Simple")

    entrada = tk.Entry(ventana, width=20)
    entrada.grid(row=0, column=0, columnspan=4)

    def click(valor):
        entrada.insert(tk.END, valor)

    def limpiar():
        entrada.delete(0, tk.END)

    tk.Button(ventana, text="1", command=lambda: click("1")).grid(row=1, column=0)
    tk.Button(ventana, text="2", command=lambda: click("2")).grid(row=1, column=1)
    tk.Button(ventana, text="+", command=lambda: click("+")).grid(row=1, column=2)
    tk.Button(ventana, text="C", command=limpiar).grid(row=1, column=3)

    ventana.mainloop()
