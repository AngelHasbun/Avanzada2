#Generador de edad de una persona dependiendo el año actual y el año en que nacio.

import os
os.system('cls' if os.name == 'nt' else 'clear')

print ("Calcular Edad")
anio=int(input("Porfavor ingresa tu anio de nacimiento:"))
anioa=2025 #(input("ingresa el anio actual-."))

edad=anioa-anio
print("La edad que tienes es: ", edad)

if edad >=21:
    print(f"Naciste en: {edad}, tas Viejo.", edad)
else:
    print(f"Naciste en: {edad}, Tas chiqui dog.", edad)
if edad>=18:
    print(f"Ya andate de la casa Viejo, ciudadano")


