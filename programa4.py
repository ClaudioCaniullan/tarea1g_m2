import paquete_cientifico as fnx

def calcular4():
    valor_ponderado = fnx.valorPonderadoProducto()
    print(valor_ponderado)

    calcular_sueldo = fnx.calcularSueldo()
    print(calcular_sueldo)

    pago_aduana = fnx.pagoAduana()
    print(pago_aduana)

    add_iva = fnx.agregarIVA()
    print(add_iva)

    if __name__ == "__main__":
        calcular4()
        input()