#Descueto

def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

# Ejemplo de uso
precio = float(input("Ingrese el precio original: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
print(f"El precio con descuento es: {calcular_descuento(precio, porcentaje)}")