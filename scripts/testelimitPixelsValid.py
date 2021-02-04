#-*- coding utf-8 -*-
import ee
import gee
import os
import sys
import random
from datetime import date
import copy
import math
import json
import compararTiles_listwithOrb as tiles_Orb
# import lsTiles as auxiliar
try:
  ee.Initialize()
  print('The Earth Engine package initialized successfully!')
except ee.EEException as e:
  print('The Earth Engine package failed to initialize!')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
sys.setrecursionlimit(1000000000)


params = {
    "max16bit": 65536,
    "ccobert": 40,
    "start": None,
    "end": None,       
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],     
    "assetLimBra": 'users/CartasSol/shapes/Brasil_Buffer3km',  
    "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/', 
    "gradeS2Corr": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat',  
    "gradeS2Div": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeNordeC',    
    'pathHome': "/home/superusuario/Dados/projAlertas/tabFeitas/",
    'path_TF': "/tabFeitas/",    
    'isCaatinga': True,
    'periodo': 'year',    # 'dry', 'wet'
   
}

params['start'] = '2020-01-01'
params['end'] = '2020-12-31'
limiteImg = 7
lstTiles_sizeZero = []
for orbNo, lsTiles in tiles_Orb.dictArqRegCaat.items():

    for tile in lsTiles:  

        item = str(orbNo) + '_' + tile       
        
        newDataset = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(
                        params['start'], params['end']).filter(
                                ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))).filter(
                                    ee.Filter.eq('MGRS_TILE', tile)).filter(
                                        ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert'])).filter(
                                        ee.Filter.lt('NODATA_PIXEL_PERCENTAGE', 20)).sort(
                                            'CLOUDY_PIXEL_PERCENTAGE').select(params["bandasAll"]).limit(limiteImg)

        tam = newDataset.size().getInfo()
        print("tiem {} com numero de imagens {} ".format(item, tam))
        lstTiles_sizeZero.append(item)



for tile in lstTiles_sizeZero:
    print(tile)