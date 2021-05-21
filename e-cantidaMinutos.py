cant_minutos=float(input(" ingrese la cantidad de minutos: "))

horas=int(cant_minutos/60)
min_restantes=cant_minutos-horas*60

print("Horas: "+str(horas))
print("minutos: "+str(min_restantes))