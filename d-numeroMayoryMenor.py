numero=input("ingrese el numero de 4 cifras: ")

mayor=0
for i in range(len(numero)):
    if int(numero[i])>mayor:
        mayor=int(numero[i])
menor=9999
for i in range(len(numero)):
    if int(numero[i])<menor:
        menor=int(numero[i])

print("el numero mayor es: "+str(mayor))
print("el numero menor es: "+str(menor))