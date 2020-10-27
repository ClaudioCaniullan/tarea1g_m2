import paquete_cientifico1 as p1



def calcular1(): 
    
    # area y perimetro circulo
	r = int(input('ingrese el radio de la circulo : '))
	print(p1.area_circulo(r))
	print(p1.perimetro_circulo(r))
	
    # area y perimetro triangulo rec
	b = int(input('ingrese la base del triangulo rectangulo : '))
	h = int(input('ingrese la altura del triangulo rectangulo : '))
	print(p1.area_triangulo_rec(b,h))
	print(p1.perimetro_triangulo_rec(b,h))

    # area y perimetro rectangulo
	b = int(input('ingrese la base del rectangulo : '))
	h = int(input('ingrese la altura del rectangulo : '))
	print(p1.area_rectangulo(b,h))
	print(p1.perimetro_rectangulo(b,h))

    # distancia recorrida
	t = int(input('ingrese el tiempo del recorrido : '))
	v = int(input('ingrese la velocidad: '))
	print(p1.distancia_recorrida(t,v))


	
if __name__ == '__main__':
	calcular1()
	input()

