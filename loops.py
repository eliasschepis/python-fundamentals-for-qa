'''
for

for se usa para iterar en los elementos de la lista, que la lista se define usando [ lista ]
'''

frutas = ["manzana", "banana", "naranja", "mora", "mora"]

for fruta in frutas:
    print("la frutas son {}".format(fruta))

print("----------final del ejercicio-----------")

'''
range

range es una funcion build in de python, en este caso para numeros
'''

for numero in range(1, 11):
    print(numero)

print("----------final del ejercicio-----------")

'''
while

while se ejecutara siempre que una condicion siga siendo T = true
'''

temp_f = 40

while temp_f > 37:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1

print("----------final del ejercicio-----------")

'''
loop controls

break
termina el loop, sigue a la siguiente declaracion fuera del loop

continue
salta la parte actual del loop y continua a la siguiente parte

pass
salta todas las partes del loop donde aparece pass, se usa mucho en testing
'''

temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    if temp_f == 38:
        break

print("----------final del ejercicio-----------")

for numero in range(1, 11):
    if numero == 9:
        print("No contamos el numero 9")
        continue
    print("Este es el numero {}".format(numero))

print("----------final del ejercicio-----------")

for numero in range(1, 11):
    if numero == 5:
        pass
    else:
        print("Este es el numero {}".format(numero))

print("----------final del ejercicio-----------")

'''
while in
'''

on = True

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


while on:
    operation = input ("Ingresa una operacion: +, -, *, / o Q ")
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
    elif operation == "Q":
        print("Haz elegido salir")
        on = False
    else:
        print("Operacion invalida")

