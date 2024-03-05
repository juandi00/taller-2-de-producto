# Salario mínimo en Colombia (ejemplo)
salario_minimo = 1900000  # Este valor puede variar, asegúrate de usar el valor actual

# Solicitar al usuario que ingrese su salario
salario = float(input("Ingresa tu salario: "))

# Validar si el salario es mayor o igual que el salario mínimo
if salario >= salario_minimo:
    print("El salario ingresado es mayor.")
else:
    print("El salario ingresado es menor que el salario mínimo.")