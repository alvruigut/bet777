# -*- coding: utf-8 -*-
import csv
import requests
from lxml import html


url_pagina_flashcore = 'https://www.flashscore.es/futbol/espana/laliga-ea-sports/resultados/'
url_quiniela= 'https://juegos.loteriasyapuestas.es/jugar/la-quiniela/apuesta'
url='https://www.mundodeportivo.com/servicios/quiniela'

#Devuelve un diccionario con los partidos de la quiniela
#param: url de la pagina web
#return: {1: 'RAYO - LAS PALMAS', 2: 'GRANADA - AT.MADRID', 3: 'VALENCIA - ATH.CLUB', 4: 'CELTA - R.SOCIEDAD', 5: 'OSASUNA - GETAFE', 6: 'R.MADRID - ALMERÍA', 7: 'BETIS - BARCELONA', 8: 'GIRONA - SEVILLA', 9: 'ESPANYOL - VILLARREAL B', 10: 'TENERIFE - SPORTING', 11: 'R.FERROL - R.OVIEDO', 12: 'RACING S. - CARTAGENA', 13: 'HUESCA - EIBAR', 14: 'ELCHE - VALLADOLID', 16: 'MALLORCA'}

def extraer_informacion(url):
    partidos = {}
    respuesta = requests.get(url) # Realizar la solicitud HTTP a la página web
    if respuesta.status_code == 200: # Comprobar solicitud (código 200)
        arbol = html.fromstring(respuesta.content)  # Parsear el contenido HTML de la página con lxml
        elementos_bg_name = arbol.xpath('//div[@class="bg-name"]')# Encontrar todos los elementos <div> con la clase "bg-name"
        # Extraer la información de los partidos
        for indice, elemento in enumerate(elementos_bg_name, start=1):
            texto_partido = elemento.text_content().strip()
            texto_partido += ' - ' + elementos_bg_name[15].text_content().strip() if indice == 15 else ''  # Obtener el texto dentro del elemento <div>
            equipos = texto_partido.split('-') # Dividir el texto en dos partes usando el carácter "-"
            partidos[indice] = [equipo.strip() for equipo in equipos] # Añadir el partido al diccionario con el índice como clave
        del partidos[16]
        return partidos
    else:
        print(f"Error en la solicitud HTTP: {respuesta.status_code}")
        return None
    
def lista_partidos():
    partidos = extraer_informacion(url)
    lista_partidos = []
    for i in range(1,16):
        lista_partidos.append(partidos[i])
    return lista_partidos

if __name__ == "__main__":
    print('#################################################### Partidos ###############################################')
    print(extraer_informacion(url))
    print('#################################################### Equipos ###############################################')
    print(lista_partidos())