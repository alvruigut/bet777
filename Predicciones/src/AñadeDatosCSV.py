# -*- coding: utf-8 -*-
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
from pyppeteer import launch

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

#Mapa de urls de estadisticas de los equipos 
def urls_estadisticas_equipos():
    res={}
    for equipo in lista_equipos():
        if equipo == 'Girona':
            res[equipo] = 'https://www.flashscore.es/equipo/girona-fc/nNNpcUSL/'
        elif equipo == 'Real Madrid':
            res[equipo] = 'https://www.flashscore.es/equipo/real-madrid/W8mj7MDD/'
        elif equipo == 'Athletic Club':
            res[equipo] = 'https://www.flashscore.es/equipo/athletic-club/IP5zl0cJ/'
        elif equipo == 'Barcelona':
            res[equipo] = 'https://www.flashscore.es/equipo/fc-barcelona/SKbpVP5K/'
        elif equipo == 'Atlético de Madrid':
            res[equipo] = 'https://www.flashscore.es/equipo/atletico-madrid/jaarqpLQ/'
        elif equipo == 'Real Sociedad':
            res[equipo] = 'https://www.flashscore.es/equipo/real-sociedad/jNvak2f3/'
        elif equipo == 'Real Betis':
            res[equipo] = 'https://www.flashscore.es/equipo/real-betis/vJbTeCGP/'
        elif equipo == 'Valencia':
            res[equipo] = 'https://www.flashscore.es/equipo/valencia-cf/CQeaytrD/'
        elif equipo == 'Cádiz':
            res[equipo] = 'https://www.flashscore.es/equipo/cadiz-cf/hdWjLJUJ/'
        elif equipo == 'Granada':
            res[equipo] = 'https://www.flashscore.es/equipo/granada/EXuxl1xP/'
        elif equipo == 'Almería':
            res[equipo] = 'https://www.flashscore.es/equipo/ud-almeria/nF2Vy2D0/'
        elif equipo == 'Sevilla':
            res[equipo] = 'https://www.flashscore.es/equipo/sevilla/h8oAv4Ts/'
        elif equipo == 'Celta de Vigo':
            res[equipo] = 'https://www.flashscore.es/equipo/celta-vigo/8pvUZFhf/'
        elif equipo == 'Villareal':
            res[equipo] = 'https://www.flashscore.es/equipo/villarreal-cf/lUatW5jE/'
        elif equipo == 'Mallorca':
            res[equipo] = 'https://www.flashscore.es/equipo/rcd-mallorca/4jDQxrbf/'
        elif equipo == 'Osasuna':
            res[equipo] = 'https://www.flashscore.es/equipo/ca-osasuna/ETdxjU8a/'
        elif equipo == 'Getafe':
            res[equipo] = 'https://www.flashscore.es/equipo/getafe-cf/dboeiWOt/'
        elif equipo == 'Las Palmas':
            res[equipo] = 'https://www.flashscore.es/equipo/las-palmas/IyRQC2vM/'
        elif equipo == 'Rayo Vallecano':
            res[equipo] = 'https://www.flashscore.es/equipo/rayo-vallecano/8bcjFy6O/'
        elif equipo == 'Alavés':
            res[equipo] = 'https://www.flashscore.es/equipo/alaves/hxt57t2q/'
    return res

# urls_estadisticas_equipos() devuelve un diccionario con los equipos y sus urls de estadisticas, y de esas urls vamos a extraer los codigos de las urls de las estadisticas de los partidos
#Base url https://www.flashscore.es/partido/'codigo'/#/resumen-del-partido/resumen-del-partido
def codido_flashcore2():
    codigos={}
    lista_codigos=[]
    for equipo,url in urls_estadisticas_equipos().items():
            respuesta = requests.get(url) # Realizar la solicitud HTTP a la página web
            if respuesta.status_code == 200:
                arbol = html.fromstring(respuesta.content)
                

                elementos = arbol.xpath('//div[@class="event__match event__match--static event__match--twoLine"]')
                for elemento in elementos:
                    lista_codigos.append(elemento.attrib.get('id', None))
                    codigos[equipo]=lista_codigos
            else:
                print(f"Error en la solicitud HTTP: {respuesta.status_code}")
                return None
            
   

    return respuesta
def codigo_flashcore4():
    driver = webdriver.Firefox()  # Asegúrate de tener el driver de Firefox (geckodriver) instalado
    driver.get('https://www.flashscore.es/equipo/girona-fc/nNNpcUSL/')
    
    # Encontrar todos los elementos cuyos IDs comienzan con 'g_1_'
    elementos = driver.find_elements(By.XPATH, '//*[starts-with(@id, "g_1_")]')

    for elemento in elementos:
        print(elemento.get_attribute('innerHTML'))  # Imprimir el contenido interior de cada elemento

    driver.quit()

async def codigo_flashcore():
    browser = await launch()
    try:
        page = await browser.newPage()
        await page.goto('https://www.flashscore.es/equipo/girona-fc/nNNpcUSL/')

        # Esperar a que al menos un elemento cuyo ID comience con 'g_1_' esté presente en el DOM
        await page.waitForXPath("//*[contains(@id, 'g_1_')]", {'timeout': 60000})  # Aumenta el tiempo de espera a 60 segundos

        # Encontrar todos los elementos cuyos IDs comienzan con 'g_1_'
        elementos = await page.xpath("//*[contains(@id, 'g_1_')]")
        
        for elemento in elementos:
            contenido = await elemento.getProperty('innerHTML')
            contenido_texto = await contenido.jsonValue()
            print(contenido_texto)  # Imprimir el contenido interior de cada elemento
    finally:
        await browser.close()  # Asegurarse de que el navegador se cierre correctamente

async def main():
    await codigo_flashcore()


if __name__ == "__main__":
   # url_pagina_flashcore = 'https://www.flashscore.es/partido/'+codido_flashcore()+'/#/resumen-del-partido/estadisticas-del-partido/0'
    url='https://www.mundodeportivo.com/servicios/quiniela'
    #print('#################################################### Partidos Quiniela ###############################################')
    #print(extraer_informacion(url))
    print('#################################################### Equipos Quiniela ###############################################')
    #print(lista_partidos_quiniela())
    asyncio.run(main())
