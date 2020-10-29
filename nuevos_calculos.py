
import math
from math import pi 

# matematicas

def area_circulo(r):
	area = pi*r**2
	return print('el area del ciruclo es: ' + str(area))

def perimetro_circulo(r):
	perimetro = 2*pi*r
	return print('el perimetro del circulo es: ' + str(perimetro))



def area_triangulo_rec(b,h):
	area = (b*h)/2
	return print('El area del triangulo rectangulo es:'+ str(area))

def perimetro_triangulo_rec(b,h):
	perimetro = b + h + (b**2 + h**2)**0.5
	return print('El perimetro del triangulo rectangulo es:'+ str(perimetro))



def area_rectangulo(b,h):
	area = (b*h)
	return print('El area del rectangulo es: '+ str(area))

def perimetro_rectangulo(b,h):
	perimetro = 2*(b + h)
	return print('El perimetro del rectangulo es: '+ str(perimetro))


def distancia_recorrida(t,v):
	distancia = t*v
	return print('La distancia recorrida es: '+ str(distancia))



# economia

def tasa_actividad(poblacion_activa, poblacion_total):
    return (poblacion_activa / poblacion_total) * 100
    

def tasa_ocupacion(poblacion_ocupada, poblacion_activa):
    resultado = (poblacion_ocupada / poblacion_activa) * 100
    return resultado


def tasa_paro(poblacion_parada, poblacion_activa):
    resultado = (poblacion_parada / poblacion_activa) * 100
    return resultado

def rentabilidad_economica(bait, activo):
    resultado = (bait / activo) * 100
    return resultado


# fisica

def velocidad():
    d1=10
    t1=2
    velocidad=d1/t1
    print("velocidad es igual: " +str(velocidad )) 
    



def distancia():
    v2=5
    t2=3
    distancia=v2*t2
    return print("la distancia es:"+str(distancia))




def tiempo():
    d3=9
    v3=3
    tiempo=d3/v3
    return print("el tiempo es:"+str(tiempo))





def aceleracion():
    v4=8
    t4=4
    aceleración=v4/t4
    return print("la aceleración es:"+str(aceleración))

#logistica

def calcularSueldo():
    SueldoBase = int(input("Ingrese su Sueldo: $"))
    GratificacionLegal = SueldoBase * 0.10
    SueldoBruto = SueldoBase + GratificacionLegal
    descuento_AFP = SueldoBruto * 0.07
    descuento_AFP = int(descuento_AFP)
    descuento_ISAPRE = SueldoBruto * 0.07
    descuento_ISAPRE = int(descuento_ISAPRE)
    seguro_cesantia = SueldoBruto * 0.02
    seguro_cesantia = int(seguro_cesantia)
    SueldoLiquido = SueldoBruto - descuento_AFP - descuento_ISAPRE - seguro_cesantia
    SueldoLiquido = int(SueldoLiquido)
    return print(" ### Sueldo Liquido: $ "+ str(SueldoLiquido)+
                "\n ### Descuento AFP: $ "+ str(descuento_AFP)+
                "\n ### Descuento Isapre: $ "+ str(descuento_ISAPRE)+
                "\n ### Seguro de cesantia: $ "+ str(seguro_cesantia))         
calcularSueldo()

def valorPonderadoProducto():
    prod_x_provedoor1 = int(input("Ingrese valor del proveedor_1: $"))
    prod_x_proveedor2 = int(input("Ingrese valor del proveedor_2: $"))
    prod_x_proveedor3 = int(input("Ingrese valor del proveedor_3: $"))

    cantidad_proveedor_1 = 150 #unidades
    cantidad_proveedor_2 = 20 #unidades
    cantidad_proveedor_3 = 120 #unidades

    #logica
    valor_x_1 = prod_x_provedoor1 * cantidad_proveedor_1 #calculo valor total producto
    valor_x_2 = prod_x_proveedor2 * cantidad_proveedor_2 #calculo valor total producto
    valor_x_3 = prod_x_proveedor3 * cantidad_proveedor_3 #calculo valor total producto
    
    totalPonderado = valor_x_1 + valor_x_2 + valor_x_3 #totales productos $
    total_cantidad = cantidad_proveedor_1 + cantidad_proveedor_2 + cantidad_proveedor_3 #totalProductos

    promedioPonderadoProducto = totalPonderado / total_cantidad #Ponderado de los 3 proveedores
    promedioPonderadoProducto = int(promedioPonderadoProducto)

    
    return print("El valor ponderado es: $" +str(promedioPonderadoProducto))
valorPonderadoProducto()

def pagoAduana():
    valorFactura = int(input("Total Factura: $")) #preciofactura
    derecho_aduanero = valorFactura * 0.06 # porcentaje de cobro aduana
    agregar_IVA = (valorFactura + derecho_aduanero) * 0.19 # iba sobre impuesto aduanero
    valorFinal = valorFactura + derecho_aduanero + agregar_IVA # valor final con impuesto aduanero
    valorFinal = int(valorFinal) # transformo el valor a un numero entero
    
    return print("El costo total con impuestos de aduana es: $ " + str(valorFinal))
pagoAduana()

def agregarIVA():
        precio = float(input("Ingrese el precio de su producto: "))
        valor_iva = precio * 0.16
        print("El IVA de su producto es: ", valor_iva)
        ptotal = precio + valor_iva
        return print("El precio total es de: ", ptotal)
agregarIVA()


