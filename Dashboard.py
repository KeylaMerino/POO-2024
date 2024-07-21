import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script.

    Parámetros:
    ruta_script (str): La ruta relativa del script a mostrar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except PermissionError:
        print(f"No tienes permisos para leer el archivo {ruta_script}.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_script}: {e}")

def buscar_termino_en_codigo(ruta_script, termino):
    """
    Busca un término específico dentro del contenido de un archivo de script.

    Parámetros:
    ruta_script (str): La ruta relativa del script a buscar.
    termino (str): El término a buscar dentro del script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            contenido = archivo.read()
            if termino in contenido:
                print(f"\n--- Código de {ruta_script} (contiene '{termino}') ---\n")
                print(contenido)
            else:
                print(f"El término '{termino}' no se encontró en el archivo {ruta_script}.")
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_script}: {e}")

def mostrar_menu():
    """
    Muestra el menú principal del dashboard y maneja las opciones del usuario.
    """
    ruta_base = os.path.dirname(__file__)
    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
        '3': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-1. Ejemplo - Carro y Acciones.py',
        "4": 'Unidad 1/2.2. Caracteristicas de la POO/2.2-3. Ejemplo - Print Atributos Clase.py',
        "5": "Unidad 2/1.1. Tipos de Datos e Identificadores/2.1.1-1 - Nomenclatura en Python.py",
        "6": "Unidad 2/2.1. Constructores y Destructores/2.2.1-1 - Uso de constructor.py",
        # Agrega aquí más rutas de scripts según sea necesario
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")
        print("b - Buscar término en un script")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion == 'b':
            script_key = input("Elige un script para buscar un término: ")
            if script_key in opciones:
                termino = input("Ingresa el término a buscar: ")
                ruta_script = os.path.join(ruta_base, opciones[script_key])
                buscar_termino_en_codigo(ruta_script, termino)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()