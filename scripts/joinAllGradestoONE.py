#-*- coding utf-8 -*-
import ee
import gee 
import sys
import random
import math
import copy
import json
import arquivoparametros as aparam
try:
  ee.Initialize()
  print('The Earth Engine package initialized successfully!')
except ee.EEException as e:
  print('The Earth Engine package failed to initialize!')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
sys.setrecursionlimit(1000000000)

def exportFeat (feature, name):

    idAsset = 'projects/mapbiomas-arida/ALERTAS/auxiliar/'
    
    optExp = {
        'collection': feature, 
        'description': name, 
        'assetId': idAsset + name             
    }

    task = ee.batch.Export.table.toAsset(**optExp)    
    task.start()
       
    print ("salvando 💾 ROI para o  asset... 📥 !" + name)    


params = {
    # 'pathOut': 'projects/mapbiomas-arida/ALERTAS/SHP/shp/',
    'pathOut': 'projects/mapbiomas-arida/ALERTAS/auxiliar/',
    'pathInt': {'id': 'projects/mapbiomas-arida/ALERTAS/shps'}
}


def getAllFeatsfromFolder():

    getParam = ee.data.getList(params['pathInt'])    

    # featTotal = ee.List([])
    featTotal = ee.FeatureCollection([])
    
    for item in getParam:
        print(item['id'])
        featC = ee.FeatureCollection(item['id'])
        featTotal = featTotal.merge(featC)

    print("carregou {} features".format(len(getParam)))
    return featTotal




grades = getAllFeatsfromFolder()
exportFeat (grades, 'shpGradeSent_IC_Caat')
