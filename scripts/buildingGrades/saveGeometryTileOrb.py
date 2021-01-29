#-*- coding utf-8 -*-
import ee
import os
import sys
import random
from datetime import date
import copy
import math
import json
import compararTiles_listwithOrb as tiles_Orb

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

    idAsset = 'users/mapbiomascaatinga04/Panpa/'
    
    optExp = {
        'collection': feature, 
        'description': name, 
        'assetId': idAsset + name             
    }

    task = ee.batch.Export.table.toAsset(**optExp)    
    task.start()
       
    print ("salvando 💾 ROI para o  asset... 📥 !" + name)    


datasetSent2 = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2020-11-01', '2020-12-01')


for orb, lsTiles in tiles_Orb.dictArqRegPanpa.items():

    for tile in lsTiles:
        
        print("orbita: {} ===  tile: {}".format(orb, tile))
        lsImTemp = datasetSent2.filter(ee.Filter.eq('MGRS_TILE', tile))\
                                .filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orb)))
        
        print("carregadas {} imagens sentinel ".format(lsImTemp.size().getInfo()))
        geomet = lsImTemp.geometry()
        dictFeat = {
            'MGRS_TILE': tile,
            'SENSING_ORBIT_NUMBER': int(orb)
            }
        
        feat = ee.Feature(geomet, dictFeat) 

        exportFeat (ee.FeatureCollection([feat]), orb + '_' + tile)