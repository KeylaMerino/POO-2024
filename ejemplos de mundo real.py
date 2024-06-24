# archivo: cine.py

class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Película: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Duración: {self.duracion} minutos")


class Cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre del cliente: {self.nombre}")
        print(f"Edad: {self.edad} años")


class Boleto:
    def __init__(self, pelicula, cliente, precio):
        self.pelicula = pelicula
        self.cliente = cliente
        self.precio = precio

    def mostrar_informacion(self):
        print("--- Información del Boleto ---")
        self.pelicula.mostrar_informacion()
        self.cliente.mostrar_informacion()
        print(f"Precio del boleto: ${self.precio}")


class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.ventas = []

    def agregar_pelicula(self, pelicula):
        self.catalogo.append(pelicula)
        print(f"Se agregó la película {pelicula.titulo} al catálogo del cine.")

    def vender_boleto(self, titulo_pelicula, nombre_cliente, edad_cliente):
        pelicula_encontrada = None
        cliente = Cliente(nombre_cliente, edad_cliente)

        for pelicula in self.catalogo:
            if pelicula.titulo == titulo_pelicula:
                pelicula_encontrada = pelicula
                break

        if pelicula_encontrada:
            precio_boleto = 10  # Precio base del boleto
            nuevo_boleto = Boleto(pelicula_encontrada, cliente, precio_boleto)
            self.ventas.append(nuevo_boleto)
            print(f"¡Venta realizada! Boleto para {cliente.nombre} para la película {pelicula_encontrada.titulo}.")
        else:
            print(f"La película {titulo_pelicula} no está disponible en este cine.")

    def mostrar_ventas(self):
        print(f"--- Ventas realizadas en el cine {self.nombre} ---")
        for boleto in self.ventas:
            boleto.mostrar_informacion()
            print()


# Función principal para probar el sistema
def main():
    # Crear algunas películas
    pelicula1 = Pelicula("El Señor de los Anillos", 180, "Fantasía")
    pelicula2 = Pelicula("Interestelar", 169, "Ciencia ficción")

    # Crear un cine
    cine_polanco = Cine("Cinepolis Polanco")

    # Agregar películas al catálogo del cine
    cine_polanco.agregar_pelicula(pelicula1)
    cine_polanco.agregar_pelicula(pelicula2)

    # Vender boletos
    cine_polanco.vender_boleto("El Señor de los Anillos", "Ana García", 25)
    cine_polanco.vender_boleto("Interestelar", "Pedro Martínez", 30)

    # Mostrar las ventas realizadas
    cine_polanco.mostrar_ventas()


if __name__ == "__main__":
    main()

