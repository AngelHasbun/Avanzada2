# Programa que realiza las tablas de multiplicar con ciclo while

numero = int(input("Ingrese un Número para la tabla de multiplicar: "))
i = 1
while i <= 10:
    resultado = numero * i
    print (f"{numero}", "x", i, "=", resultado)
    i += 1

    