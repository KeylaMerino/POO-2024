class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def mostrar_info(self):
        print(f"{self.nombre} - Vida: {self.vida}, Fuerza: {self.fuerza}")

class Hechicero(Personaje):
    def __init__(self, nombre, vida, inteligencia):
        super().__init__(nombre, vida)
        self.inteligencia = inteligencia

    def mostrar_info(self):
        print(f"{self.nombre} - Vida: {self.vida}, Inteligencia: {self.inteligencia}")

# Ejemplo de uso
g = Guerrero("Keyla", 100, 20)
h = Hechicero("Cloe", 80, 25)

g.mostrar_info()
h.mostrar_info()