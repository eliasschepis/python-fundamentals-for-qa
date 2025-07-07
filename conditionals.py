def add():
    a = float(input("Ingresa un numero: "))
    b = float(input("Ingresa otro numero: "))
    print(a + b)

def sub():
    a = float(input("Ingresa un numero: "))
    b = float(input("Ingresa otro numero: "))
    print(a - b)

def mult():
    a = float(input("Ingresa un numero: "))
    b = float(input("Ingresa otro numero: "))
    print(a * b)

def div():
    a = float(input("Ingresa un numero: "))
    b = float(input("Ingresa otro numero: "))
    print(a / b)


operation = input ("Ingresa una operacion: +, -, *, / ")
if operation == "+":
    print("Haz elegido suma")
    add()
elif operation == "-":
    print("Haz elegido resta")
    sub()
elif operation == "*":
    print("Haz elegido multiplicacion")
    mult()
elif operation == "/":
    print("Haz elegido dividir")
    div()
else:
    print("Operacion invalida")

