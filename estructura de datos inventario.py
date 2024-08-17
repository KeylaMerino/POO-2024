class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar si el ID es único
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: ID de producto duplicado.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")
            inventario.actualizar_producto(
                id_producto,
                int(nueva_cantidad) if nueva_cantidad else None,
                float(nuevo_precio) if nuevo_precio else None
            )

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
