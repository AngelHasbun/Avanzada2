#Condicionales en python

a = 10  

if a == 0:
    print("0 es un número especial: divisible por 2, pero no suele clasificarse como par o impar.")
elif a % 2 == 0:
    print(f"{a} es un número par.")
else:
    print(f"{a} es un número impar.")