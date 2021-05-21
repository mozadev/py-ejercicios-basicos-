primer_parcial=float(input("ingrese primer examen parcial: "))
segundo_parcial=float(input("ingrese segundo examen parcial: "))
tercer_parcial=float(input("ingrese tercer examen parcial: "))

ponde_1parcial=0.3
ponde_2parcial=0.3
ponde_3parcial=0.4

calif_final=primer_parcial*ponde_1parcial+segundo_parcial*ponde_2parcial+\
            tercer_parcial*ponde_3parcial


print("la calificacion final es: "+str(calif_final))