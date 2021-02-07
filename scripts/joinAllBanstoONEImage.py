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


def exportarClassification(imgTransf, nameAl, geomGrade):
    
    IdAsset = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mCaatS2_SR/' + nameAl 
    # IdAsset = 'users/mapbiomascaatinga05/mosaicSentinel2/' + nameAl
    # IdAsset = 'users/mapbiomascaatinga05/mosaicTestS2/'  + nameAl 
    print(" Salvando en id Asset:")
    print("   <> {}".format(IdAsset))
    
    optExp = {
        'image': imgTransf, #.toInt16()
        'description': nameAl, 
        'assetId':IdAsset, 
        'pyramidingPolicy': {".default": "mode"},  
        'region': geomGrade.getInfo()['coordinates'],
        'scale': 10,
        'maxPixels': 1e13 
    }

    task = ee.batch.Export.image.toAsset(**optExp)    
    task.start()
    print("reporte do status")

    for keys, vals in dict(task.status()).items():
        print ( "  {} : {}".format(keys, vals))
    
    print ("salvando ... ! ")




####################################################################################
### https://code.earthengine.google.com/4aa004aae390f0c4dc5708ece511796b        ####
### https://code.earthengine.google.com/f308b42668bed2d6917a03ad362fd1e8        ####
####################################################################################
params = {
    "max16bit": 65536,
    "ccobert": 40,
    "start": None,
    "end": None,   
    "mes": None,
    "ano": 2020,
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],   
    "assetLimBra": 'users/CartasSol/shapes/Brasil_Buffer3km',  
    "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/', 
    "gradeS2Corr": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat',  
    "gradeS2Div": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeNordeC',    
    'pathHome': "/home/superusuario/Dados/projAlertas/tabFeitas/",
    'pathMosaic': 'users/mapbiomascaatinga05/mosaicSentinel2',
    'pathMosaicMB' : 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics',
    'path_TF': "/tabFeitas/",    
    'isCaatinga': True,
    'periodo': 'year',    # 'dry', 'wet'
    'imgRef': {
        'year': 'COPERNICUS/S2_SR/20200702T130251_20200702T130252_T24MVS',
        'dry': 'COPERNICUS/S2_SR/20200930T130251_20200930T130253_T24MVS'
    },
    'numeroLimit': 50,
    'numeroTask': 6,
    'conta' : {
        # '0':  'caatinga01',
        '0': 'caatinga02',
        '6': 'caatinga03',
        '12': 'caatinga04',
        '18': 'caatinga05',        
        '24': 'solkan1201',
        '30': 'diegoGmail',
        '36': 'rodrigo',
        '42': 'diegoUEFS',
        # '64': 'Rafael',
        # '75': 'Nerivaldo',
        #'39': 'solkanCengine',
        # '45': 'soltangalano',
        # '88': 'ellen'        
    },
}


def gerenciador(cont):    
    
    #=====================================
    # gerenciador de contas para controlar 
    # processos task no gee   
    #=====================================
    
    numberofChange = [kk for kk in params['conta'].keys()]
    print(cont)
    print(numberofChange)
    if str(cont) in numberofChange:
        
        gee.switch_user(params['conta'][str(cont)])
        gee.init()
        #relatorios.write("Conta de: " + params['conta'][str(cont)] + '\n')

        tarefas = gee.tasks(
            n= params['numeroTask'],
            return_list= True)
        
        # for lin in tarefas:            
        #     relatorios.write(str(lin) + '\n')
    
    elif cont > params['numeroLimit']:
        cont = 0
    
    cont += 1    
    return cont



grades_Solape = [
            '25LBL','25MBM','25MBN','25MBP','24KTG','24LTH','24LTJ','24LTK',
            '24LTL','24LTM','24LTN','24LTP','24LTQ','24LTR','24MTA','24MTB',
            '24MTS','24MTT','24MTU','24MTV','23KKB','23LKC','23LKD','23LKE',
            '23LKF','23LKG','23LKH','23LKJ','23LKK','23LKL','23MKM','23MKN',
            '23MKP','23MKQ','23MKR','23MKS','23MKT','23MKU'  #,'24MXU'
        ]
bandasInd = ['median_blue', 'median_green', 'median_red', 
            'median_nir', 'median_swir1', 'median_siwr2']

bandasIndCorr = ['median_blue', 'median_green', 'median_red', 
            'median_nir', 'median_swir1', 'median_swir2']

lsBND_ind = ['B2', 'B3', 'B4', 'B8', 'B11', 'B12']

listException = tiles_Orb.lsICsizeZero

imgRefCaat = params['imgRef']['year']

suf = 'year'
# 'ano',    # 'seco', 'chuvoso'
if params['periodo'] == 'year': 
    params['start'] = '2020-01-01'
    params['end'] = '2020-12-31'

elif params['periodo'] == 'dry': 
    params['start'] = '2020-07-01'
    params['end'] = '2020-12-31'
    suf = 'dry'
    imgRefCaat = params['imgRef']['dry']

else:
    params['start'] = '2020-01-01'
    params['end'] = '2020-12-31'
    suf = 'wet'
    

gradeS2 = ee.FeatureCollection(params['gradeS2Corr'])
gradeDiv = ee.FeatureCollection(params['gradeS2Div'])
limiteCaat = ee.FeatureCollection(params["assetLimBra"])


mosaicS2 = ee.ImageCollection(params['pathMosaic'])
mS2Caat = ee.ImageCollection(params['pathMosaicMB'])
mS2Caat = mS2Caat.merge(mosaicS2)

del(mosaicS2)

datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
    .filterDate(params['start'], params['end'])


contador = 30
limiteImg = 7

for orbNo, lsTiles in tiles_Orb.dictArqRegCaat.items():

    for tile in lsTiles:  

        print("Processando imagens de orbita  📡 {} >>  e tile 📡 {} >> ".format(orbNo, tile))
        item = str(orbNo) + '_' + tile
        geomet = gradeS2.filter(ee.Filter.And(
                                            ee.Filter.eq('MGRS_TILE', tile),
                                            ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))
                                        )).geometry() 

        
        geometDiv = gradeDiv.filter( ee.Filter.eq('NAME', tile)).geometry()
        gradeInter = ee.Geometry(geometDiv.intersection(geomet).intersection(limiteCaat))         
        footprint = gradeInter.getInfo()['coordinates']        
        areaInt = gradeInter.area(1).getInfo()
        print("area ", areaInt)
        if int(areaInt) < 1000:
            continue
        
        else:
            
            if item in listException:
                newDataset = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(
                            params['start'], params['end']).filter(
                                    ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))).filter(
                                        ee.Filter.eq('MGRS_TILE', tile)).filter(
                                            ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert'])).sort(
                                                'CLOUDY_PIXEL_PERCENTAGE').select(params["bandasAll"]).limit(limiteImg)
                # https://code.earthengine.google.com/2d3d0ac8c8d1c9e0a8c9a2356495f3a1
            
            else:
                newDataset = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(
                                params['start'], params['end']).filter(
                                        ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))).filter(
                                            ee.Filter.eq('MGRS_TILE', tile)).filter(
                                                ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert'])).filter(
                                                ee.Filter.lt('NODATA_PIXEL_PERCENTAGE', 20)).sort(                                                
                                                    'CLOUDY_PIXEL_PERCENTAGE').select(params["bandasAll"]).limit(limiteImg)

            
            
            imgOring = ee.Image(newDataset.median())
            # exemplo da função desenvolvida abaixo
            #https://code.earthengine.google.com/192489de3ae1f9e6ac2e95b03c648180
            numImg = 0
            imgMos = None
            imgMasking = ee.Image(0).clip(geomet)

            for cc, mbnd in enumerate(bandasInd):
                print("✅ Join band 🔰 " + mbnd + " 🔰")
                imgTemp = mS2Caat.filter(ee.Filter.And(
                                                ee.Filter.eq('MGRS_TILE', tile),
                                                ee.Filter.eq('SENSING_ORBIT_NUMBER', orbNo),
                                                ee.Filter.eq('banda', mbnd)
                                            )).limit(2)
                if numImg == 0:
                    numImg = imgTemp.first().get('NUM_IMAGENS')
                
                imgTemp = imgTemp.median().rename(bandasIndCorr[cc])
                imgMasking = imgMasking.add(imgTemp.unmask(-1).clip(gradeInter).lte(0))

                imgBanda = imgOring.select(lsBND_ind[cc])
                imgBanda = imgBanda.updateMask(imgMasking)
                
                if mbnd == 'median_blue':
                    imgMos = imgTemp.add(imgBanda)
                else:
                    imgMos = imgMos.addBands(imgTemp.add(imgBanda))

            imgMos = ee.Image.cat(imgMos.select(bandasIndCorr))
            imgMos = imgMos.clip(gradeInter)
            
            # set properties
            print("set all properties")
            imgMos = imgMos.set('system:footprint', footprint)
            imgMos = imgMos.set('year', params['ano'])
            imgMos = imgMos.set('MGRS_TILE', tile)
            imgMos = imgMos.set('SENSING_ORBIT_NUMBER', orbNo)
            imgMos = imgMos.set('NUM_IMAGENS', numImg)        
            imgMos = imgMos.set('periodo', params['periodo'])        

            # save imagens 
            nameAl = str(params['ano']) + '_' + str(orbNo)  + '_' + tile + '_' +  params['periodo']  #  
            exportarClassification(imgMos, nameAl, gradeInter)

            contador = gerenciador(contador)
