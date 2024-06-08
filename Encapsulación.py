# encapsulacion

class Personaje:
    def __init__(self, nombre, vida):
        self.__nombre = nombre
        self.__vida = vida

    def get_nombre(self):
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def set_vida(self, vida):
        if vida >= 0:
            self.__vida = vida
        else:
            print("La vida no puede ser negativa")

    def mostrar_info(self):
        print(f"{self.__nombre} - Vida: {self.__vida}")

# Ejemplo de uso
p = Personaje("Juan", 100)
p.mostrar_info()

p.set_vida(80)
p.mostrar_info()

p.set_vida(-10)  # Intento de establecer un valor negativo