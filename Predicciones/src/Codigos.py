# -*- coding: utf-8 -*-
import requests
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.Equipos import *


#Devuelve un diccionario con los partidos de la quiniela
#param: url de la pagina web
#return: {1: 'RAYO - LAS PALMAS', 2: 'GRANADA - AT.MADRID', 3: 'VALENCIA - ATH.CLUB', 4: 'CELTA - R.SOCIEDAD', 5: 'OSASUNA - GETAFE', 6: 'R.MADRID - ALMERÍA', 7: 'BETIS - BARCELONA', 8: 'GIRONA - SEVILLA', 9: 'ESPANYOL - VILLARREAL B', 10: 'TENERIFE - SPORTING', 11: 'R.FERROL - R.OVIEDO', 12: 'RACING S. - CARTAGENA', 13: 'HUESCA - EIBAR', 14: 'ELCHE - VALLADOLID', 16: 'MALLORCA'}
def extraer_equipos_quiniela(url):
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
    
#Devuelve una lista con los partidos de la quiniela
def lista_partidos_quiniela():
    partidos = extraer_equipos_quiniela(url)
    lista_partidos = []
    for x  in partidos.values():
        lista_partidos.append(x[0])
        lista_partidos.append(x[1])
    return lista_partidos

#####################################################################################################################################

#urls de estadisticas de los equipos 
def urls_estadisticas_equipos():
    res={}
    for equipo in lista_equipos_primera():
        res.update(parsear_nombres_url(equipo))
    return res    

#Base url_pagina_flashcore = 'https://www.flashscore.es/partido/'+codigo+'/#/resumen-del-partido/estadisticas-del-partido/0'
#Códigos de las urls de las estadisticas de los partidos
#Devuelve un diccionario con los codigos de los partidos de la quiniela

def guardar_en_fichero(data, file='data\codigosFlashcore.txt'):
    with open(file, 'w', encoding='utf-8') as file:
        for equipo, codigos in data.items():
            codigo = ', '.join(codigos)
            file.write(f'{equipo}: [{codigo}]\n')

def codigo_flashcore(n):
    dict_codigos = {}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  #Para cargar el contenido de la pagina sin abrir una ventana del navegador
    driver = webdriver.Chrome(options=chrome_options)
    for equipo,url in urls_estadisticas_equipos().items() :
        if equipo in lista_partidos_quiniela():
            driver.get(url)    # Acceder a la página web
            time.sleep(5) 

            ids = WebDriverWait(driver, 5).until( # Localizar elementos con el xpath de la web
                EC.presence_of_all_elements_located((By.XPATH, '//div[@title="¡Haga click para detalles del partido!"]'))
            )
          #Quitar el index 0 y poner o buscar un estado para que solo añada los  finalizados  o arriba cogiendo el container de últimos resultados
            lista_codigos=[]
            for index, element in enumerate(ids):
                if index == 0:
                    continue  # Saltar el primer elemento
                if len(lista_codigos) < n: #Añadir solo 5 códigos a la lista
                    lista_codigos.append(element.get_attribute('id').replace('g_1_','') )            
                dict_codigos[equipo] = lista_codigos

    driver.quit()    # Cerrar el navegador
    guardar_en_fichero(dict_codigos)  # Llamar a la función para guardar en el archivo




    

if __name__ == "__main__":
    url='https://www.mundodeportivo.com/servicios/quiniela'
    print('#################################################### Partidos Quiniela ###############################################')
    print(extraer_equipos_quiniela(url))
    print('#################################################### Códigos Flashcore ###############################################')
    codigo_flashcore(2) #Numero de codigos que queremos que nos devuelva por equipo
    print('Los códigos se encuentra en: data/codigosFlashcore.txt')
