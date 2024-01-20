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



def extraer_estadisticas():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    url_pagina_flashcore = 'https://www.flashscore.es/partido/GAuEdjfJ/#/resumen-del-partido/estadisticas-del-partido/0'
    driver.get(url_pagina_flashcore)
    time.sleep(5)

    # Extraer estadisticas
    estadisticas = {}
    elementos_estadisticos = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, '_row_rz3ch_9'))
    )
    for stats in elementos_estadisticos:
        partes = stats.text.split('\n')
        # Utilizar la parte del medio como clave y las partes restantes como valores en una lista
        clave = partes[1].lower().replace(' ', '_').replace('_(xg)','')  # Convertir a minúsculas y reemplazar espacios con guiones bajos
        if clave == 'goles_esperados':
            valores = [float(partes[0]) , float(partes[2])] 
        else:
            valores = [int(partes[0].replace('%','')), int(partes[2].replace('%',''))]    

        estadisticas[clave] = valores

     # Extraer nombres de los participantes
    equipos = []
    nombre_equipos = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'participant__participantName'))
    )
    for equipo in nombre_equipos:
        if equipo.text not in equipos:
            equipos.append(equipo.text)

    # Extraer resultado
    resultado = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="detailScore__wrapper"]'))
    )
    numero_resultados = resultado[0].text  
    res = [int(num) for num in numero_resultados.split('-')]

    driver.quit()
    return {'equipos': equipos, 'resultados': res, 'estadisticas': estadisticas}


if __name__ == "__main__":
    print(extraer_estadisticas())
