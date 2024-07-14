# Ejemplo de uso de constructores y destructores en Python
class FileManager:
    def __init__(self, filename, mode):
        """
        Constructor de la clase FileManager.
        Inicializa el objeto FileManager y abre el archivo en el modo especificado.

        :param filename: Nombre del archivo a abrir.
        :param mode: Modo en el que se abrirá el archivo ('r' para leer, 'w' para escribir, etc.).
        """
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open_file()

    def open_file(self):
        """Abre el archivo en el modo especificado y almacena el objeto de archivo."""
        self.file = open(self.filename, self.mode)
        print(f"Archivo {self.filename} abierto en modo {self.mode}.")

    def write_data(self, data):
        """
        Escribe datos en el archivo si está abierto en modo escritura.

        :param data: Datos a escribir en el archivo.
        """
        if self.mode == 'w':
            self.file.write(data)
            print(f"Datos escritos en el archivo {self.filename}.")
        else:
            print("El archivo no está abierto en modo escritura.")

    def __del__(self):
        """
        Destructor de la clase FileManager.
        Cierra el archivo si está abierto.
        """
        if self.file:
            self.file.close()
            print(f"Archivo {self.filename} cerrado.")

# Ejemplo de uso de la clase FileManager
file_manager = FileManager('example.txt', 'w')
file_manager.write_data('Esto es una prueba.')
# El destructor (__del__) se llamará automáticamente cuando el objeto file_manager sea destruido.

class DatabaseConnection:
    def __init__(self, db_name):
        """
        Constructor de la clase DatabaseConnection.
        Inicializa el objeto DatabaseConnection y establece la conexión con la base de datos.

        :param db_name: Nombre de la base de datos a la que se conectará.
        """
        self.db_name = db_name
        self.connection = None
        self.connect_to_db()

    def connect_to_db(self):
        """Simula la conexión a una base de datos."""
        self.connection = f"Conexión a la base de datos {self.db_name}"
        print(f"Conectado a la base de datos {self.db_name}.")

    def close_connection(self):
        """Simula el cierre de la conexión a la base de datos."""
        self.connection = None
        print(f"Conexión a la base de datos {self.db_name} cerrada.")

    def __del__(self):
        """
        Destructor de la clase DatabaseConnection.
        Cierra la conexión a la base de datos si está abierta.
        """
        if self.connection:
            self.close_connection()

# Ejemplo de uso de la clase DatabaseConnection
db_connection = DatabaseConnection('mi_base_de_datos')
# El destructor (__del__) se llamará automáticamente cuando el objeto db_connection sea destruido.