v1=float(input("Ingrese el primer voltaje:"))
v2=float(input("Ingrese el segundo voltaje:"))
v3=float(input("Ingrese el tercer voltaje:"))
v4=float(input("Ingrese el cuarto voltaje:"))
v5=float(input("Ingrese el quinto voltaje:"))
vt=(v1+v2+v3+v4+v5)/5

if vt >= 220:
    print("<ALTO VOLTAJE=")
else:
    print("<VOLTAJE CORRECTO=")