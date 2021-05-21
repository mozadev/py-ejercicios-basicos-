
dist_vehi=float(input("ingrese la distancia entre vehiculos km: "))
velocidad_vehi_rapido=float(input("ingrese la velocida del vehiculo mas rapido (km/h) : "))
velocidad_vehi_lento=float(input("ingrese la velocidad del vehiculo mas lento (km/h) : "))
tiempo_alcance=dist_vehi/(velocidad_vehi_rapido-velocidad_vehi_lento)

print("el tiempo de alcance es: "+str(tiempo_alcance*60)+" minutos")
