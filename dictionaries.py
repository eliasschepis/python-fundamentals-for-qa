stuff = {"salud":15, "comida":20, "enemigos":100}

'''
se componen de
nombre de diccionaro = {"key":value, "key2":value}
'''

'''
diccionario + get method
devuelve el value de una key del diccionario
'''

print(stuff.get("enemigos"))

'''
diccionaro + items method
devuelve los keys del diccionario con su value asignado
'''

print(stuff.items())

'''
diccionario + keys method
devuelve todos los keys del diccionario sin su valor
'''

print(stuff.keys())

'''
diccionario + pop method
nos permite eliminar el ultimo item del diccionario
'''

print(stuff.popitem())
print(stuff)

'''
diccionario + setdefault method
nos permite saber o añadir una key con su value
'''

print(stuff.setdefault("comida"))
print(stuff)
print(stuff.setdefault("aliados", 200))
print(stuff)

'''
diccionario + update method
nos permite agregar un diccionario dentro de otro diccionario
tambien podemos actualizar los values de una key dentro del diccionario
'''

new_items = {"sword": 3, "axe":5}
stuff.update(new_items)
print(stuff)

new_items = {"sword": 15, "axe":45}
stuff.update(new_items)
print(stuff)
