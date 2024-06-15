# Programación POO
class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio


def main():
    print("Bienvenido al programa de promedio semanal del clima.")
    clima_semanal = ClimaSemanal()

    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima_semanal.ingresar_temperatura(temp)

    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")


if __name__ == "__main__":
    main()