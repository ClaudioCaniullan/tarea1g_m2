import paquete_cientifico as p2

def calcular2():
    resultado=p2.velocidad()
    print("resultado" +str(resultado)) 
    resultado1=p2.distancia()
    print("resultado" +str(resultado1)) 
    resultado2=p2.tiempo()
    print("resultado" +str(resultado2)) 
    resultado3=p2.aceleracion()
    print("resultado" +str(resultado3)) 

if __name__ == '__main__':
    calcular2()
    input()
    