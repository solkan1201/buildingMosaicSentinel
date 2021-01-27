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
import arquivoparametros as aparam
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

def exportFeat (feature, name):

    idAsset = 'users/mapbiomascaatinga05/Pantanal/'
    
    optExp = {
        'collection': feature, 
        'description': name, 
        'assetId': idAsset + name             
    }

    task = ee.batch.Export.table.toAsset(**optExp)    
    task.start()
       
    print ("salvando 💾 ROI para o  asset... 📥 !" + name)    


datasetSent2 = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2020-11-01', '2020-12-01')
# dictArqReg ={
#     '138': ['23MPP', '23MQS', '24MTA', '24MTB', '24MTT', '24MTU', '24MTV'],
#     '9': ['25LBL','25MBM','25MBN','25MBP'],
#     '38': ['23LPH', '24LTP', '24LTQ', '24LTP', '24LTQ', '24LTR']
# }


dictArqRegPan = {    
    '24': [
        '21KVR','21KWA','21KWR','21KWS','21KWT','21KWU',
        '21KWV','21KXA','21KXB','21KXR','21KXS','21KXT',
        '21KXU','21KXV','21KYA','21KYB','21KYS','21KYT',
        '21KYU','21KYV','21KZA','21KZB','21KZU','21KZV',
        '21LXC','21LXD','21LXE','21LYC','21LYD','21LYE',
        '21LZC','22KBD','22KBE','22KBF','22KBG','22LBH'
    ],
    '67' : [
        '21KUA','21KUB','21KUR','21KUS','21KUT','21KUU',
        '21KVA','21KVB','21KVR','21KVS','21KVT','21KVU',
        '21KVV','21KWA','21KWB','21KWR','21KWS','21KWT',
        '21KWU','21KWV','21KXA','21KXB','21KXU','21KXV',
        '21LUC','21LUD','21LVC','21LVD','21LVE','21LWC',
        '21LWD','21LWE','21LXC','21LXD','21LXE','21LYD',
        '21LYE'
    ],    
    '110': [
        '20KRG','20LRH','21KTB','21KUA','21KUB','21KVB',
        '21LTC','21LTD','21LUC','21LUD','21LUE','21LVC',
        '21LVD','21LVE'
    ],
    '124' : [
        '21KZA','21KZU','21KZV','22KBD','22KBE','22KBF'
    ]
}
# for orb, lsTiles in aparam.dictArqReg.items():
for orb, lsTiles in dictArqRegPan.items():

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