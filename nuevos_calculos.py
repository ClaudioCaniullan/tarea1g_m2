
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



