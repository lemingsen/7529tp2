import sys

class TP2:
    def __init__(self,args):
        self.imprimirAyuda()

    def imprimirAyuda(self):
        print("Por favor, ingrese el nombre del archivo a procesar como primer parámetro del script.")
        print("Por ejemplo:\n            python tp2.py depositos.csv\n\n")
        print("El archivo debe contener una ruta por línea; con origen, destino y costo separados por coma.")
        print("Por ejemplo:\n            A,B,54\nA,D,-3,\nB,C,8\n")

if "__main__" == __name__:
    TP2(sys.argv[1:])
