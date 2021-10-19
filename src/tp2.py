import sys

from src.lector import Lector

class TP2:
    def __init__(self,args):
        if 1 != len(args):
            self.imprimirAyuda()
        try:
            nombreArchivo = args[0]
            lector = Lector(nombreArchivo)
        except FileNotFoundError as ex:
            print("El achivo es inexistente o inaccesible: "+nombreArchivo+"\n")
            print("Error original:"+str(ex),file=sys.stderr)            
        except Exception as ex:
            print("Se produjo un error inesperado\n")
            print("Error original:"+str(ex),file=sys.stderr)            

    def imprimirAyuda(self):
        margen = "            "
        print("Por favor, ingrese el nombre del archivo a procesar como primer parámetro del script.")
        print("Por ejemplo:")
        print(margen+"python -m src.tp2 depositos.csv\n\n")
        print("El archivo debe contener una ruta por línea; con origen, destino y costo separados por coma.")
        print("Por ejemplo:")
        print(margen+"A,B,54\n"+margen+"A,D,-3,\n"+margen+"B,C,8\n")

if "__main__" == __name__:
    TP2(sys.argv[1:])
