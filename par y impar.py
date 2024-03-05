def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(str(numero) + " es un número par")
    else:
        print(str(numero) + " es un número impar")

numero_ingresado = int(input("Ingresa un número: "))
verificar_par_impar(numero_ingresado)