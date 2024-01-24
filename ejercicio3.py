v1=float(input("Ingrese el primer Voltaje: "))
v2=float(input("Ingrese el segundo Voltaje: "))
v3=float(input("Ingrese el tercer Voltaje: "))
prom=(v1+v2+v3)/3

if prom < 115:
    print("<VOLTAJE CORRECTO=")
elif prom > 115 and prom < 220:
    print("<ALTO VOLTAJE=")
else:
    print("<PELIGRO=")