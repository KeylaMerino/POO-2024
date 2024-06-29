# Este programa calcula el área de un rectángulo basándose en la entrada del usuario.
# Incluye el uso de diferentes tipos de datos: int, float, string, boolean.

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.

    Args:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Returns:
    float: El área del rectángulo.
    """
    area = base * altura
    return area
def verificar_numero_entero(numero_str: str) -> bool:
    """
    Verifica si una cadena puede convertirse en un número entero.

    Args:
    numero_str (string): La cadena a verificar.

    Returns:
    bool: True si la cadena puede convertirse en entero, False en caso contrario.
    """
    try:
        int(numero_str)
        return True
    except ValueError:
        return False

def main():
    """
    Función principal que solicita las dimensiones del rectángulo al usuario
    y muestra el área calculada. También verifica si los valores de entrada son enteros.
    """
    print("Programa para calcular el área de un rectángulo")

    # Solicitar la base del rectángulo
    base_str = input("Introduce la base del rectángulo: ")

    # Verificar si la base es un número entero
    es_base_entero = verificar_numero_entero(base_str)

    if es_base_entero:
        base = int(base_str)
    else:
        base = float(base_str)

    # Solicitar la altura del rectángulo
    altura_str = input("Introduce la altura del rectángulo: ")

    # Verificar si la altura es un número entero
    es_altura_entero = verificar_numero_entero(altura_str)

    if es_altura_entero:
        altura = int(altura_str)
    else:
        altura = float(altura_str)

    # Calcular el área
    area = calcular_area_rectangulo(base, altura)

    # Mostrar el resultado
    print(f"El área del rectángulo es: {area}")


if __name__ == "__main__":
    main()