try:
    a = int(input("Ingrese el dividendo: "))
    b = int(input("Ingrese el divisor: "))

    cociente = a / b
    print("La division es: ", cociente)
except Exception:
    print("Error al realizar la division")

print("Fin del programa")