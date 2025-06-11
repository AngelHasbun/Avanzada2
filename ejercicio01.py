#crear un programa que muestre el total de la compra de un solo 
#producto calculando el impuesto sobre venta y dar el descuento 
#solamente cuando el importe de la compra sea mayor a 10 mil el descuento sera de un 25%

#Solicitar datos al usuario

precio=float(input("ingrese el precio del producto: "))
cantidad=int(input("ingrese la cantidad comprada: "))

#Calculo del subtotal
subtotal = precio * cantidad

#calculo el impuesto(15%)
impuesto = subtotal * 0.15

#Sumar el impuesto al subtotal
total_con_impuesto = subtotal + impuesto

#verificar si aplicamos el descuento
if subtotal < 10000:
    descuento = total_con_impuesto * 0.25
    total_final = total_con_impuesto - descuento
    print("Se aplica un descuento del 25%")
else:
    descuento = 0
    total_final = total_con_impuesto
    print("No se aplica descuento")

# Mostrar resultados
print("Subtotal: $", round(subtotal, 2))
print("Impuesto (15%): $", round(impuesto, 2))
print("Descuento: $", round(descuento, 2))
print("Total a pagar: $", round(total_final,2))