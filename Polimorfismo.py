# polimorfismo
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} ataca con una espada"

class Hechicero(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza un hechizo"

# Ejemplo de uso
personajes = [Guerrero("Keyla"), Hechicero("Cloe")]

for personaje in personajes:
    print(personaje.atacar())