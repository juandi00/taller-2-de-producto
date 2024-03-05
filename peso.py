peso = float(input("ingresa tu peso en kilogramos:"))
alt = float(input("Ingrese su altura en metros:"))
imc = peso / (alt ** 2)
if imc < 18.5:
    estado = "Bajo peso"
print(f"tu indice de masa muscular es:{imc} - Estado: {estado}")