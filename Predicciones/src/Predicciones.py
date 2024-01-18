 # -*- coding: utf-8 -*-


from collections import namedtuple
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Prediccion = namedtuple('Prediccion','equipo, resultados, golesF, golesC, posesion, bajas,posicionLiga,faltasxPartido')

def lee_datos(fichero):
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            if linea:  # Check if linea is not empty
                equipo = linea[0]
                res = linea[1]
                golesF = int(linea[2])
                golesC = int(linea[3])
                pos = linea[4]
                bajas = linea[5]
                posicionLiga = int(linea[6])
                faltasxPartido = int(linea[7])
                tupla=Prediccion(equipo, res ,golesF, golesC, pos, bajas, posicionLiga, faltasxPartido)
                registros.append(tupla)
    return registros


def mapa_prediccion(predicciones, equipoLocal, equipoVisitante):
    dicc = dict()
    for res in predicciones:
        if res.equipo == equipoLocal or res.equipo == equipoVisitante:
            clave = res.equipo
            if clave in dicc:
                dicc[clave].add(res)
            else:
                dicc[clave] = {res}
    return dicc