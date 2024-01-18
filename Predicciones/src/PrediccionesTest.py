 # -*- coding: utf-8 -*-

import csv as csv
from Predicciones import *


fichero = ('data/data.csv')
REGISTROS=lee_datos(fichero)
        
def test_lee_datos(fichero):
    print("Número total de registros leídos :", len(REGISTROS),'\n')
    for indx,tupla in enumerate(REGISTROS):
        print (f'{indx+1}-{tupla}')   


def test_prediccion(registros,equipoLocal,equipoVisitante):
    print("Predicción del partido",equipoLocal,"-",equipoVisitante)
    print(mapa_prediccion(registros,equipoLocal,equipoVisitante))

def main():
    
    test_lee_datos(fichero)
    test_prediccion(REGISTROS,'Madrid','Betis')
    
if __name__=="__main__":
    print("########################################################### DATOS  ###########################################################\n")
    main()     
