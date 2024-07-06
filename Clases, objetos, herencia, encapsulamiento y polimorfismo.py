# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas


# Clase derivada 1
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"


# Clase derivada 2
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.__color = color  # Atributo privado

    def hacer_sonido(self):
        return "¡Miau!"

    def get_color(self):
        return self.__color

    def set_color(self, nuevo_color):
        self.__color = nuevo_color


# Función principal
def main():
    # Creación de instancias de las clases
    perro1 = Perro("Yogui", "Labrador")
    gato1 = Gato("Garfield", "Naranja")

    # Ejemplo de polimorfismo
    animales = [perro1, gato1]
    for animal in animales:
        print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

    # Ejemplo de encapsulación
    print(f"El color de {gato1.nombre} es {gato1.get_color()}")
    gato1.set_color("Gris")
    print(f"Ahora el color de {gato1.nombre} es {gato1.get_color()}")


if __name__ == "__main__":
    main()
