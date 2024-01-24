b=float(input("Ingrese la base del triangulo: "))
a=float(input("Ingrese la altura del triagulo"))
area=(a*b)/2

if area > 1000:
    print("DATOS NO VALIDOS")
else:
    print(area)