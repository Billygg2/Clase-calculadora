def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


print("Calculadora básica Practica")
print("Suma:", sumar(5, 3))
print("Resta:", restar(5, 3))
print("Multiplicación:", multiplicar(5, 3))
print("División:", dividir(5, 3))
