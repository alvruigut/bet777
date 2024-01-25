# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def guardar_ranking(ranking):
    with open('data\estadisticasFlashcore.txt', 'w', encoding='utf-8') as file:
        file.write('Ranking:\n')
        for posicion, equipo in ranking.items():
            file.write(f'{posicion}:{equipo} \n')

def extrae_posiciones_liga(url):
    ranking={}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)

    equipos = driver.find_elements(By.XPATH, '//div[@class="tflex__content"]/p/a[@href]')
    for ind,equipo in enumerate(equipos,start=1):
        valor=equipo.text
        if valor=='ATLÉTICO DE MADRID':
            valor='AT.MADRID'
        elif valor=='REAL MADRID':
            valor='R.MADRID'
        elif valor=='ATHLETIC CLUB':
            valor='ATH.CLUB'
        elif valor=='REAL SOCIEDAD':
            valor='R.SOCIEDAD'
        elif valor=='REAL BETIS':
            valor='BETIS'
        elif valor=='VALENCIA CF':
            valor='VALENCIA'
        elif valor=='GRANADA CF':
            valor='GRANADA'
        elif valor=='CELTA DE VIGO':
            valor='CELTA'
        elif valor=='RAYO VALLECANO':
            valor='RAYO'
        ranking[ind]=valor
    driver.quit()
    guardar_ranking(ranking)

if __name__ == "__main__":
    url='https://www.mundodeportivo.com/resultados/futbol/laliga/clasificacion'
    print('#################################################### Ranking ###############################################')
    print(extrae_posiciones_liga(url))
