def user_info(nombre, edad, ciudad):
    '''Esta funcion imprime el nombre, la edad y la ciudad
    del argumento provisto a la function'''

    print("{} tiene {} y vive en {}".format(nombre, edad, ciudad))

user_info(
    nombre = input("Ingrese su nombre: "),
    edad = input("Ingrese su edad: "),
    ciudad = input("Ingrese su ciudad: ")
)

'''
kargs: un poco mas complejo, adapta el input a un valor especificado, por ejemplo:
'''

def user_info_kargs(nombrekarg, edad=0, ciudad="Barcelona"):
    print("{} tiene {} y vive en {}".format(nombrekarg, edad, ciudad))

user_info_kargs(nombrekarg = "Elias")