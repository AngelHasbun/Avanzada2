#Funciones

#Definimos la funcion
def saludo(nombre):
    print(f"Hola {nombre}!")

#Definimos la funcion PI
def _PI():
    return 3.14159

#Definimos la funcion suma
def suma(a, b):
    return a + b

#Invocamos la funcion
saludo("Juan")

#Calcular el diametro de un circulo
r=1
diametro=2*_PI()*r
print(f"El diametro del circulo es: {diametro}")

#Funcion suma
print(f"Funcion suma: {suma(1,1)}")