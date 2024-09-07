# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.__titulo_autor = (titulo, autor)  # Usamos una tupla para que sea inmutable
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo_autor(self):
        return self.__titulo_autor

    def __str__(self):
        return f"{self.__titulo_autor[0]} por {self.__titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase que representa a un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para manejar los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase que gestiona la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para gestionar libros por ISBN
        self.usuarios = set()  # Conjunto para asegurar IDs únicos de usuarios

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in {u.id_usuario for u in self.usuarios}:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado.")

    def dar_baja_usuario(self, id_usuario):
        self.usuarios = {u for u in self.usuarios if u.id_usuario != id_usuario}
        print(f"Usuario con ID {id_usuario} dado de baja.")

    def prestar_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario and isbn in self.libros:
            libro = self.libros.pop(isbn)  # Quitamos el libro de la colección disponible
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"No se puede prestar el libro con ISBN {isbn} o el usuario no existe.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.devolver_libro(isbn)
                self.libros[isbn] = libro  # Volvemos a añadir el libro a la colección disponible
                print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultado = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultado.append(libro)
            elif criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultado.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultado.append(libro)
        return resultado

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.libros_prestados
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return []


# Pruebas del sistema
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Escalofrios", "George Orwell", "Romance", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "67890")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Keyla Merino", "001")
biblioteca.registrar_usuario(usuario1)

# Prestar libros
biblioteca.prestar_libro("001", "12345")

# Listar libros prestados
prestados = biblioteca.listar_libros_prestados("001")
for libro in prestados:
    print(libro)

# Devolver libros
biblioteca.devolver_libro("001", "12345")
