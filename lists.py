frutas = ["manzana", "banana", "mora", "frutilla"]
años = ["2025", 2, 3.5, "2000"]
numeros = [3, 5, 34, 29304230, 9.8, 2,5, 7]
print(frutas)

'''
lista + .append method
se usa para sumar algo a la lista, pero no puede ser mas de una cosa
'''

frutas.append("uva")
print(frutas)

'''
lista + .extend method
se usa para agregar una lista dentro de otra
'''

frutas.extend(años)
print(frutas)

'''
lista + .remove method
se usa para eliminar un elemento en especifico de la lista
'''

frutas.remove("uva")
print(frutas)

'''
lista + pop method
se usa para eliminar un elemento por su index, que se asigna a partir del 0
usando -1 podemos ir de atras para adelante
en especial cuando queremos eliminar el ultimo elemento
y no sabemos que tan larga es la lista
'''

frutas.pop(0)
print(frutas)

'''
lista + sort method
solo se puede utilizar para ordenar ciertos tipos de data, por ejemplo, integers
'''

numeros.sort()
print(numeros)

'''
in function
nos permite chequear la lista para ver si se encuentra el elemento que buscamos
devolviendo un boolean
'''

print("pera" in frutas)
print("banana" in frutas)

'''
count function
nos permite contar cuantas veces se encuentra un elemento en la lista
'''

print(frutas.count("banana"))
print(frutas.count("piña"))

'''
index function
nos permite contar en que lugar del index se encuentra el elemento
'''

print(frutas.index("frutilla"))