# -*- coding: utf-8 -*-

def lista_equipos_primera():
    return ['GIRONA','R.MADRID','ATH.CLUB','BARCELONA','AT.MADRID','R.SOCIEDAD','BETIS','VALENCIA','LAS PALMAS','GETAFE','RAYO','OSASUNA','ALAVÉS','MALLORCA','VILLARREAL','CELTA','SEVILLA','CÁDIZ','GRANADA','ALMERÍA']

def lista_equipos_segunda():
    return []

#Diccionario con los equipos(nombres parseados) y sus url
def parsear_nombres_url(equipo):
    res={}
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