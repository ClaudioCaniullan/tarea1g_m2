import paquete_cientifico as pc

print()
print("En el siguiente programa puede calcular: Tasa de actividad; Tasa de ocupación; tasa de paro ; Rentabilidad economica")
print()

pa = int(input("Ingrese poblacion activa: "))
pt = int(input("ingrese poblacion total: "))
ta = pc.tasa_actividad(pa, pt)
print("La tasa de actividad es: " + str(ta))
print()

po = int(input("Ingrese poblacion ocupada: "))
pa = int(input("Ingrese poblacion activa: "))
tao = pc.tasa_ocupacion(pa, po)
print("La tasa de ocupacion corresponde a : " + str(tao))
print()

pp = int(input("Ingrese poblacion parada: "))
pac = int(input("Ingrese poblacion activa: "))
tp = pc.tasa_paro(pp, pac)
print("La tasa de paro corresponde a: " + str(tp))
print()

re = int(input("Ingrese bait: "))
ac = int(input("Ingrese activo: "))
reco = pc.rentabilidad_economica(re, ac)
print("Su rentabilidad economica es de: " + str(reco))
print()
