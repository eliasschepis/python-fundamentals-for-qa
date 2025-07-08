'''
permite agrupar data e informacion como data y viarables en una sola unidad
pueden organizarse 1 x archivo o contener muchas clases en un solo archivo
todas las clases en python son objetos

En Python, __init__ es un método especial llamado constructor,
y self se refiere a la instancia actual de la clase.
__init__ se ejecuta automáticamente al crear un objeto, permitiendo inicializar sus atributos.
self permite acceder y modificar los atributos y métodos de ese objeto específico dentro de la clase.

En resumen:
__init__ se utiliza para configurar el estado inicial de un objeto.
self permite que los métodos de la clase operen sobre la instancia específica del objeto que se está utilizando.
'''

#create class

class Person:

    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def status_change(self):
        self.health = (self.health - 25)
        if self.health == 100:
            print("{} is fully healthy!".format(self.firstname))
        elif self.health == 85:
            print("{} feels tired.".format(self.firstname))
        elif self.health == 75:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <= 50:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 100, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()
