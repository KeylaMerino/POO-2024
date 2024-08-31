import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data['id'], data['nombre'], data['cantidad'], data['precio'])


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(
                f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    def guardar_en_archivo(self, filename='inventario.json'):
        with open(filename, 'w') as file:
            productos_dict = {id: producto.to_dict() for id, producto in self.productos.items()}
            json.dump(productos_dict, file, indent=4)

    def cargar_desde_archivo(self, filename='inventario.json'):
        try:
            with open(filename, 'r') as file:
                productos_dict = json.load(file)
                self.productos = {id: Producto.from_dict(data) for id, data in productos_dict.items()}
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido con éxito.")

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado.")

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (o presione Enter para saltar): ")
            precio = input("Nuevo precio (o presione Enter para saltar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
            print("Producto actualizado.")

        elif opcion == '4':
            nombre = input("Nombre del producto: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(
                    f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("Producto no encontrado.")

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            inventario.guardar_en_archivo()
            print("Inventario guardado con éxito.")

        elif opcion == '7':
            inventario.guardar_en_archivo()
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()

