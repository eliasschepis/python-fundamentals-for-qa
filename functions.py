'''
partes de una function

comienza con def + nombre unico de la function + ():
+ body de la function

'''

def addition():
    a = 90.900657
    b = 378998.70
    print(a + b)


addition()

'''
input function
'''

def addition_input():
    print("vamos a sumar y trastear lo aprendido")
    a = int(input("digite un numero: "))
    b = int(input("digite un numero: "))
    print("{} + {} es igual a {}".format(a, b, a + b))


addition_input()