# herencia

class Personaje:
    def __init__(self, nombre, fuerza, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"{self.nombre} - Fuerza: {self.fuerza}, Defensa: {self.defensa}, Vida: {self.vida}")

class Arquero(Personaje):
    def __init__(self, nombre, fuerza, defensa, vida, precision):
        super().__init__(nombre, fuerza, defensa, vida)
        self.precision = precision

    def atributos(self):
        super().atributos()
        print(f"Precisión: {self.precision}")

# Ejemplo de uso
a = Arquero("Kyky", 17, 10, 90, 95)
a.atributos()