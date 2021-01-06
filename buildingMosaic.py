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
import arqNewparametros as aparam
# import arqNewparamcopy as aparam
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
    "ccobert": 80,
    "start": None,
    "end": None,
    'corte': None,
    "dateAnalysis": None,    
    "mes": None,
    "ano": 2020,
    'region': 1,
    'nomeRegion': None,
    "bandaM": "classification_2019",
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],        
    "listclassesMB": [1,2,3,4,5,9,10,12], 
    "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/',
    "gradeS2": 'users/CartasSol/shapes/shapeGrideNordeCorr',
    "gradeS2Corr": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeNordeC',
    "assetMapbiomas": "projects/mapbiomas-workspace/public/collection5/mapbiomas_collection50_integration_v1",
    "folderROIs": {'id':'projects/mapbiomas-arida/ALERTAS/ROIs/trainingF/'},
    "folderGroupROIs": 'projects/mapbiomas-arida/ALERTAS/ROIs/trainingV42/',
    "classeIds": [1,2,3,4,5,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33], 
    "classeIdsNew": [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
    "limiarImg": 4,    
    "Feature" :['osavi','ndwi','ndvi','lai', 'soil',  'gcvi', 'npv', 'ndfia'], 
    "FeatureSVM": ['ndwi', 'lai', 'soil'],   
    "allBand": ['osavi','ndwi','ndvi','lai', 'soil',  'gcvi', 'npv', 'ndfia','class'],  
    'pathHome': "/home/superusuario/Dados/projAlertas/tabFeitas/",
    'path_TF': "/tabFeitas/",
    'numeroTask': 0,
    'numeroLimit': 85,
    'conta' : {
        '0': 'caatinga01',
        '10': 'caatinga02',
        '20': 'caatinga03',
        '24': 'caatinga04',
        '32': 'caatinga05',        
        '42': 'solkan1201',
        '54': 'diegoGmail',
        '27': 'rodrigo',
        '64': 'Rafael',
        '75': 'Nerivaldo',
        #'39': 'solkanCengine',
        # '45': 'soltangalano',
        # '45': 'ellen'        
    },
}

