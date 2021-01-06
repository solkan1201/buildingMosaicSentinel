#-*- coding utf-8 -*-
import ee
import os
import sys
import random
from datetime import date
import copy
import math
import json
# import arqNewparamcopy as aparam
import lsTiles
try:
  ee.Initialize()
  print('The Earth Engine package initialized successfully!')
except ee.EEException as e:
  print('The Earth Engine package failed to initialize!')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
sys.setrecursionlimit(1000000000)


class ClassCalcIndicesSpectral(object):

    # default options
    bndInd = []  
    options = {        
        "bandas": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],        
        # "Feature" :['ndwi', 'osavi', 'lai', 'soil', 'evi','gv','ndfia'], 
        "Feature" :['osavi','ndwi','ndvi','lai', 'soil',  'gcvi', 'npv', 'ndfia'], 
        'bandsFraction': ['gv','npv','soil','cloud', 'shade'] 
        # "pmtRF" : {'numberOfTrees': 50, 'variablesPerSplit': 3,  'seed': 2}
    }  

    dictClassifRef = {}

    geomet = None

    imgUltima = None

    maskMapbiomas = None

    classificadorTrained = None

    # cloudsMascara = True

    imgColClouds = None

    def __init__(self, idRef):

        self.imgRef_ = ee.Image(idRef)
        
        geomRef = self.imgRef_.geometry()

        self.imgRef_  = self.imgRef_.select(self.options['bandas'])              
    
        self.imgRef_  = self.strecht_Images(self.imgRef_, geomRef)

        # salvando em um diccionario as propiedades dde Classify da ref
        self.equalizeRef(geomRef)

        self.classificadorTrained = ClassifTrained
    
    
    def updateParametros(self, uImg, mMapBiomas, geomet):
        
        self.imgUltima = uImg

        self.maskMapbiomas = mMapBiomas.set('system:footprint', geomet)

        self.geomet = geomet

    def getImgCollectionCloud(self, imgColCC):
        self.imgColClouds = imgColCC
    

    def maskS2clouds(self, imgP):

        iDimgP = imgP.id()        
        imgMask = ee.Image(self.imgColClouds.filter(ee.Filter.eq('system:index', iDimgP)).first())

        # creando Mascara para pixels uties         
        return  imgP.updateMask(imgMask.lt(15))  
    
    def NomalizeImg(self, image, bnd, geomet):
        
        imgTemp = image.select(bnd)        

        optRed = {
            'reducer': ee.Reducer.minMax(),
            'geometry': geomet,
            'scale': 10,
            'maxPixels': 1e13
        } 

        extremos =  ee.Dictionary(imgTemp.reduceRegion(**optRed))
            
        imgTemp = imgTemp.unitScale(extremos.getNumber(bnd + "_min"), extremos.getNumber(bnd + "_max"))\
                    .multiply(10000).uint16()

        imgTemp = imgTemp.rename(bnd)

        return imgTemp

    def strecht_Images(self, image, geomet):        

        matching = ee.Image().int16()  

        for band in self.options['bandas']:

            imgTemp = self.NomalizeImg(image, band, geomet)

            imgTemp = imgTemp.rename(band)        

            matching = matching.addBands(imgTemp)

        matching = ee.Image.cat(matching.select(self.options['bandas'])) 

        # matching = matching.set()       

        return matching

    def getFC(self, image_, bnd, geomet):
        
        #Histogram equalization start:      
            
        optRed = {
            'reducer': ee.Reducer.histogram(maxBuckets= 10000),
            'geometry': geomet,
            'scale': 10,
            'maxPixels': 1e13,
            'tileScale': 4
            }

        histo = image_.reduceRegion(**optRed)         

        valsList = ee.List(ee.Dictionary(histo.get(bnd)).get('bucketMeans'))    

        freqsList = ee.List(ee.Dictionary(histo.get(bnd)).get('histogram'))

        cdfArray = ee.Array(freqsList).accum(0)

        total = cdfArray.get([-1])

        normalizedCdf = cdfArray.divide(total)

        lists = valsList.zip(normalizedCdf.toList())

        expLists = lists.reduce(ee.Reducer.toCollection(['dn', 'probability']))

        return ee.FeatureCollection(expLists)
    
    def equalizeRef(self, geomR):

        for bnd in self.options['bandas']:           

            propertImgRef = self.getFC(self.imgRef_.select(bnd), bnd, geomR)        

            ClassfImgRef = ee.Classifier.smileRandomForest(50).setOutputMode('REGRESSION')\
                .train(features= propertImgRef, classProperty= 'dn', inputProperties= ['probability'])

            self.dictClassifRef[bnd] = ClassfImgRef
    

    def equalize(self, image_, bnd, geomet):        

        propertImg = self.getFC(image_.select(bnd), bnd, geomet)        

        Classfimg = ee.Classifier.smileRandomForest(50).setOutputMode('REGRESSION')\
            .train(features= propertImg, classProperty= 'probability', inputProperties= ['dn'])

        imgExport = image_.select(bnd).rename('dn')

        #print "ja rodou a classification"
        # classifier from DigitalNivel   ---> probability  depois # classifier from probability   ---> DigitalNivel
        
        return imgExport.classify(Classfimg, 'probability')\
            .classify(self.dictClassifRef[bnd], bnd)    

    def match_Images(self, image):

        geom = image.geometry()
        
        matching = ee.Image().int16()    
        
        for band in self.options['bandas']:

            imgTemp = self.equalize(image, band, geom)
            
            imgTemp = imgTemp.toInt()

            matching = matching.addBands(imgTemp)

        matching = ee.Image.cat(matching.select(self.options['bandas']))

        return matching
    






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

datasetSent2 = ee.ImageCollection('COPERNICUS/S2_SR')\
    .filterDate(params['start'], params['end'])\
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert']))\
    .select(params["bandasAll"])

datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
    .filterDate(params['start'], params['end'])



operadorMosaic = ClassCalcIndicesSpectral()


for tile in lsTiles.lsTiles:
    
    print(tile)
    newDataset = datasetSent2.filter(ee.Filter.eq('MGRS_TILE', tile))