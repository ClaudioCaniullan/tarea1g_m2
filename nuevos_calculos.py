<<<<<<< HEAD
import math
from math import pi 

#definicion de las funciones matematicas

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


=======









































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



# if __name__ == "__main__":
    
# tasa_actividad()

# tasa_actividad()

# tasa_paro()

# rentabilidad_economica()
>>>>>>> e2858318d5ead4d8ba1012e43105efae42f6e71a
