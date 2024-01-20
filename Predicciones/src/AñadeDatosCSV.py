# -*- coding: utf-8 -*-
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Lee equipos.txt y devuelve una lista con los equipos de la Liga
def lista_equipos():
    lista_equipos= []
     # Leer equipos desde el archivo
    with open('data/equipos.txt', 'r',encoding='UTF-8') as archivo:
        next(archivo) # Saltar la primera línea (cabecera)
        for linea in archivo:
            equipos = linea.strip().strip().split(',')
            lista_equipos.extend(equipos)
    return lista_equipos

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
    
#Devuelve una lista con los partidos de la quiniela
def lista_partidos_quiniela():
    partidos = extraer_informacion(url)
    lista_partidos = []
    for x  in partidos.values():
        lista_partidos.append(x[0])
        lista_partidos.append(x[1])
    return lista_partidos

#####################################################################################################################################

#urls de estadisticas de los equipos 
def urls_estadisticas_equipos():
    res={}
    for equipo in lista_equipos():
        if equipo == 'GIRONA':
            res[equipo] = 'https://www.flashscore.es/equipo/girona-fc/nNNpcUSL/'
        elif equipo == 'R.MADRID':
            res[equipo] = 'https://www.flashscore.es/equipo/real-madrid/W8mj7MDD/'
        elif equipo == 'ATH.CLUB':
            res[equipo] = 'https://www.flashscore.es/equipo/athletic-club/IP5zl0cJ/'
        elif equipo == 'BARCELONA':
            res[equipo] = 'https://www.flashscore.es/equipo/fc-barcelona/SKbpVP5K/'
        elif equipo == 'AT.MADRID':
            res[equipo] = 'https://www.flashscore.es/equipo/atletico-madrid/jaarqpLQ/'
        elif equipo == 'R.SOCIEDAD':
            res[equipo] = 'https://www.flashscore.es/equipo/real-sociedad/jNvak2f3/'
        elif equipo == 'BETIS':
            res[equipo] = 'https://www.flashscore.es/equipo/real-betis/vJbTeCGP/'
        elif equipo == 'VALENCIA':
            res[equipo] = 'https://www.flashscore.es/equipo/valencia-cf/CQeaytrD/'
        elif equipo == 'CÁDIZ':
            res[equipo] = 'https://www.flashscore.es/equipo/cadiz-cf/hdWjLJUJ/'
        elif equipo == 'GRANADA':
            res[equipo] = 'https://www.flashscore.es/equipo/granada/EXuxl1xP/'
        elif equipo == 'ALMERÍA':
            res[equipo] = 'https://www.flashscore.es/equipo/ud-almeria/nF2Vy2D0/'
        elif equipo == 'SEVILLA':
            res[equipo] = 'https://www.flashscore.es/equipo/sevilla/h8oAv4Ts/'
        elif equipo == 'CELTA':
            res[equipo] = 'https://www.flashscore.es/equipo/celta-vigo/8pvUZFhf/'
        elif equipo == 'VILLARREAL':
            res[equipo] = 'https://www.flashscore.es/equipo/villarreal-cf/lUatW5jE/'
        elif equipo == 'MALLORCA':
            res[equipo] = 'https://www.flashscore.es/equipo/rcd-mallorca/4jDQxrbf/'
        elif equipo == 'OSASUNA':
            res[equipo] = 'https://www.flashscore.es/equipo/ca-osasuna/ETdxjU8a/'
        elif equipo == 'GETAFE':
            res[equipo] = 'https://www.flashscore.es/equipo/getafe-cf/dboeiWOt/'
        elif equipo == 'LAS PALMAS':
            res[equipo] = 'https://www.flashscore.es/equipo/las-palmas/IyRQC2vM/'
        elif equipo == 'RAYO':
            res[equipo] = 'https://www.flashscore.es/equipo/rayo-vallecano/8bcjFy6O/'
        elif equipo == 'ALAVÉS':
            res[equipo] = 'https://www.flashscore.es/equipo/alaves/hxt57t2q/'
    return res

#Base url_pagina_flashcore = 'https://www.flashscore.es/partido/'+codigo+'/#/resumen-del-partido/estadisticas-del-partido/0'
#Códigos de las urls de las estadisticas de los partidos
#Devuelve un diccionario con los codigos de los partidos de la quiniela
def codigo_flashcore():
    dict_codigos = {}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Opción para ejecutar en segundo plano sin abrir una ventana del navegador
    driver = webdriver.Chrome(options=chrome_options)
    for equipo,url in urls_estadisticas_equipos().items() :
        if equipo in lista_partidos_quiniela():
            driver.get(url)    # Acceder a la página web
            time.sleep(10)     # Esperar 10 segundos (puedes ajustar este valor según sea necesario)

        
            elements = WebDriverWait(driver, 10).until( # Localizar elementos con el xpath proporcionado
                EC.presence_of_all_elements_located((By.XPATH, '//div[@title="¡Haga click para detalles del partido!"]'))
            )
            lista_codigos=[]
            for element in elements:  # Imprimir el id de los elementos encontrados
                if len(lista_codigos) < 5: #añadir solo 5 elementos a la lista
                    lista_codigos.append(element.get_attribute('id').replace('g_1_','') )            
                dict_codigos[equipo] = lista_codigos

    driver.quit()    # Cerrar el navegador
    
    return dict_codigos



    


    

if __name__ == "__main__":
    url='https://www.mundodeportivo.com/servicios/quiniela'
    print('#################################################### Partidos Quiniela ###############################################')
    print(extraer_informacion(url))
    print('#################################################### Equipos Quiniela  ###############################################')
    print(lista_partidos_quiniela())
    print('#################################################### Códigos Flashcore ###############################################')
    print(codigo_flashcore())
