
nombre_trab=input("ingrese el nombre del trabajador: ")
horas_trab=float(input("ingrese las horas trabajadas: "))
precio_hora=float(input("precio por hora: "))

sueldo_bruto=horas_trab*precio_hora
desc_imp_renta=sueldo_bruto*0.15
salario_pagar=sueldo_bruto-desc_imp_renta

print("nombre: "+nombre_trab)
print("el sueldo bruto es: "+str(sueldo_bruto))
print("descuento por impuesto a la renta: "+str(desc_imp_renta))
print("salario a pagar: "+str(salario_pagar))


