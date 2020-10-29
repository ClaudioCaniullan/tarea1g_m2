import paquete_cientifico as p1
import paquete_cientifico as pc
import paquete_cientifico as p2
import paquete_cientifico as fnx

def menu_principal():

	print("""
		Seleccione el area de interes para ver algunos calculos:
		1. matemáticas
		2. física
		3. economía
		4. logística

		""")

	n = int(input('ingrese opcion: '))

	if n == 1:

		r = int(input('ingrese el radio de la circulo : '))
	    print(p1.area_circulo(r))
	    print(p1.perimetro_circulo(r))
	
        
	    b = int(input('ingrese la base del triangulo rectangulo : '))
	    h = int(input('ingrese la altura del triangulo rectangulo : '))
	    print(p1.area_triangulo_rec(b,h))
	    print(p1.perimetro_triangulo_rec(b,h))

        
	    b = int(input('ingrese la base del rectangulo : '))
	    h = int(input('ingrese la altura del rectangulo : '))
	    print(p1.area_rectangulo(b,h))
	    print(p1.perimetro_rectangulo(b,h))

        
	    t = int(input('ingrese el tiempo del recorrido : '))
	    v = int(input('ingrese la velocidad: '))
	    print(p1.distancia_recorrida(t,v)) 



	elif n == 2:
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



	elif n == 3:
		resultado=p2.velocidad()
        print("resultado" +str(resultado)) 
        resultado1=p2.distancia()
        print("resultado" +str(resultado1)) 
        resultado2=p2.tiempo()
        print("resultado" +str(resultado2)) 
        resultado3=p2.aceleracion()
        print("resultado" +str(resultado3)) 



	elif n == 4:
		valor_ponderado = fnx.valorPonderadoProducto()
        print(valor_ponderado)

        calcular_sueldo = fnx.calcularSueldo()
        print(calcular_sueldo)

        pago_aduana = fnx.pagoAduana()
        print(pago_aduana)

        add_iva = fnx.agregarIVA()
        print(add_iva)

	else:
		pass



if __name__ == '__main__':
	menu_principal()
	input()