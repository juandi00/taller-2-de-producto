def sumar(a, b):def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"


def mostrar_menu():
    print("Seleccione una operación:")
    print("1. nombre ")
    print("2. suma, resta")
    print("3. peso")
    print("4. par y impar")
    print("5. edad")
    print("6. cuadrado")
    print("7. triangulo")
    print("8. salario")
    print("9. extras")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número correspondiente a la operación deseada: ")

    if opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = restar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '4':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '5':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '6':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '7':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '8':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '9':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")


    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")