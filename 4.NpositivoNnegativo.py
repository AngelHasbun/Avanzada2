# 4. Numero positivo, numero negativo o cero
# Pide un número al usuario y muestra si es positivo, negativo o cero.

numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El numero es positivo.")
elif numero < 0:
    print("El numero es negativo.")
else:
    print("El numero es cero")  