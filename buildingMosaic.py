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
import lsTiles as auxiliar
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
        "Feature" :['osavi','ndwi','ndvi','lai', 'soil',  'gcvi', 'npv', 'ndfia'], 
        'bandsFraction': ['gv','npv','soil','cloud', 'shade'], 
        'scale': 300,
        'toaOrSR' : 'SR',
        'degree2radian' : 0.01745
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

        self.dem = ee.Image("USGS/SRTMGL1_003")
        
    
    def updateParametros(self, uImg, mMapBiomas, geomet):
        
        self.imgUltima = uImg

        self.maskMapbiomas = mMapBiomas.set('system:footprint', geomet)

        self.geomet = geomet

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
    

    ######################################################################################
    ## // Function to calculate illumination condition (IC). Function by Patrick Burns ###
    ## // (pb463@nau.edu) and Matt Macander                                            ###
    ## // (mmacander@abrinc.com)                                                       ###
    ######################################################################################
    def illuminationCondition(img):

        geom = img.geometry().buffer(10000)
        ### Extract image metadata about solar position  ##
        SZ_rad = ee.Image.constant(ee.Number(img.get('MEAN_SOLAR_ZENITH_ANGLE'))
                            ).multiply(3.14159265359).divide(180).clip(geom) 
        SA_rad = ee.Image.constant(ee.Number(img.get('MEAN_SOLAR_AZIMUTH_ANGLE'))
                            ).multiply(3.14159265359).divide(180).clip(geom)
        
        ####  Creat terrain layers ### 
        slp = ee.Terrain.slope(dem).clip(geom)
        slp_rad = ee.Terrain.slope(self.dem).multiply(3.14159265359).divide(180).clip(geom)
        asp_rad = ee.Terrain.aspect(dem).multiply(3.14159265359).divide(180).clip(geom)

        ###  Calculate the Illumination Condition (IC) ####
        ###  slope part of the illumination condition  ####
        cosZ = SZ_rad.cos().rename('cosZ')
        cosS = slp_rad.cos().rename('cosS')        
        slope_illumination = cosS.addBands(cosZ).expression(
                                              "float(b('cosZ') * b('cosS'))")

        sinZ = SZ_rad.sin().rename('sinZ')
        sinS = slp_rad.sin()
        cosAziDiff = (SA_rad.subtract(asp_rad)).cos().rename("cosAziDiff")
        aspect_illumination = sinZ.addBands(sinS).addBands(cosAziDiff).expression(
                                        "float(b('sinZ') * b('slope') * b('cosAziDiff'))") 
        
        ### full illumination condition (IC) ###
        ic = slope_illumination.add(aspect_illumination)

        ### Add IC to original image ###
        img_plus_ic = ee.Image(img.addBands(ic).addBands(cosZ).addBands(cosS)
                                  ).addBands(slp.rename('slope'))
        
        return img_plus_ic



    # https://code.earthengine.google.com/c20fe3602e4a99107b999d95e57752d9
    def illuminationCorrection(img):

        props = img.toDictionary()
        st = img.get('system:time_start')

        img_plus_ic = img
        mask1 = img_plus_ic.select('nir').gt(-0.1)
        mask2 = img_plus_ic.select('slope').gte(5).and(
                            img_plus_ic.select('IC').gte(0)).and(
                            img_plus_ic.select('nir').gt(-0.1))
        

        img_plus_ic_mask2 = ee.Image(img_plus_ic.updateMask(mask2))

        ### Specify Bands to topographically correct ###
        bandList = ['blue','green','red','nir','swir1','swir2']
        compositeBands = img.bandNames()
        nonCorrectBands = img.select(compositeBands.removeAll(bandList))

        geom = ee.Geometry(img.get('system:footprint')).bounds().buffer(10000)



    def agregateBandsIndexRATIO(self, img):
    
        ratioImg = img.expression("float(b('B8') / b('B4'))")\
                                .multiply(1000).rename(['ratio'])      

        return img.addBands(ratioImg)

    def agregateBandsIndexRVI(self, img):
    
        rviImg = img.expression("float(b('B4') / b('B8'))")\
                                .multiply(1000).rename(['rvi'])       

        return img.addBands(rviImg)

    
    def agregateBandsIndexNDVI(self, img):
    
        ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")\
                                .add(1).multiply(10000).rename(['ndvi'])       

        return img.addBands(ndviImg)

    
    def agregateBandsIndexWater(self, img):
    
        ndwiImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")\
                                .add(1).multiply(10000).rename(['ndwi'])       

        return img.addBands(ndwiImg)
    
    
    def AutomatedWaterExtractionIndex(img):
    
        awei = img.expression(
                            "float(4 * (b('green') - b('swir2')) - (0.25 * b('nir') + 2.75 * b('swir1')))"
                        ).add(5).multiply(10000).rename("awei")          
        
        return img.addBands(awei)


    def IndiceIndicadorAgua(img):
    
        iiaImg = img.expression(
                            "float((b('green') - 4 *  b('nir')) / (b('green') + 4 *  b('nir')))"
                        ).add(1).multiply(10000).rename("iia")
        
        return img.addBands(iiaImg)


    def agregateBandsIndexEVI(self, img):
            
        eviImg = img.expression(
            "float(2.4 * (b('B8') - b('B4')) / (1 + b('B8') + b('B4')))").divide(10)\
                .add(1).multiply(10000).rename(['evi'])     
        
        return img.addBands(eviImg)
    
    
    def agregateBandsIndexLAI(self, img):
    
        laiImg = img.expression(
            "(3.618 * float(b('evi') - 0.118))").divide(10)\
                .add(1).multiply(1000).rename(['lai'])     
    
        return img.addBands(laiImg)
    

    def agregateBandsIndexGCVI(self, img):
    
        gcviImgA = img.expression(
            "float(b('B8')) / (b('B3')) - 1")\
                .add(1).multiply(10000).rename(['gcvi'])        
        
        return img.addBands(gcviImgA)
    

    # Chlorophyll vegetation index
    def agregateBandsIndexCVI(self, img):
    
        cviImgA = img.expression(
            "float(b('B8') * (b('B3') / (b('B2') * b('B2'))))").divide(10)\
                .add(1).multiply(10000).rename(['cvi'])        
        
        return img.addBands(cviImgA)
    
    
    def agregateBandsIndexOSAVI(self,img):
    
        osaviImg = img.expression(
            "float(b('B8') - b('B4')) / (0.16 + b('B8') + b('B4'))")\
                .add(1).multiply(10000).rename(['osavi'])        
        
        return img.addBands(osaviImg)
    
    
    def agregateBandsIndexSoil(self, img):
        
        soilImg = img.expression(
            "float(b('B8') - b('B3')) / (b('B8') + b('B3'))")\
                .add(1).multiply(10000).rename(['isoil'])       
        
        return img.addBands(soilImg)    

    
    def agregateBandsIndexBAI(self, img):
    
        baiImg = img.expression(
            "float(1) / ((0.1 - b('B4'))**2 + (0.06 - b('B8'))**2)")\
                .rename(['bai']) 
        
        return img.addBands(baiImg)
    
    # Normalized Difference NIR/SWIR Normalized Burn Ratio 
    def agregateBandsIndexNBR(self, img):
    
        nbrImg = img.expression(
            "float((b('nir') - b('swir')) / (b('nir') + b('swir')))")\
                .rename(['nbr']) 
        
        return img.addBands(nbrImg)
    
    # Tasselled Cap - brightness 
    def agregateBandsIndexBrightness(self, img):
    
        tasselledCapImg = img.expression(
            "float(0.3037 * b('B2') + 0.2793 * b('B3') + 0.4743 * b('B4')  + 0.5585 * b('B8') + 0.5082 * b('B11') +  0.1863 * b('B12'))")\
                .multiply(10000).rename(['brightness']) 
        
        return img.addBands(tasselledCapImg)
    
    # Tasselled Cap - wetness 
    def agregateBandsIndexwetness(self, img):
    
        tasselledCapImg = img.expression(
            "float(0.1509 * b('B2') + 0.1973 * b('B3') + 0.3279 * b('B4')  + 0.3406 * b('B8') + 0.7112 * b('B11') +  0.4572 * b('B12'))")\
                .multiply(10000).rename(['wetness']) 
        
        return img.addBands(tasselledCapImg)
    
    # Moisture Stress Index (MSI)
    def agregateBandsIndexMSI(self, img):
    
        msiImg = img.expression(
            "float( b('B8') / b('B11'))").multiply(1000)\
                .rename(['msi']) 
        
        return img.addBands(msiImg)
    
    
    def agregateBandsIndexGVMI(self, img):
        
        gvmiImg = img.expression(
                        "float ((b('B8')  + 0.1) - (b('B11') + 0.02)) / ((b('B8') + 0.1) + (b('B11') + 0.02))" 
                    ).add(1).multiply(10000).rename(['gvmi'])     
    
        return img.addBands(gvmiImg)
    
    
    def agregateBandsIndexsPRI(self, img):
        
        priImg = img.expression(
                                "float((b('B3') - b('B2')) / (b('B3') + b('B2')))"
                            ).rename(['pri'])   
        spriImg =   priImg.expression(
                                "float((b('pri') + 1) / 2)").multiply(10000).rename(['spri'])  
    
        return img.addBands(spriImg)
    

    def agregateBandsIndexCO2Flux(self, img):
        
        co2FluxImg = img.expression("float(b('ndvi') * b('spri'))"
                                ).add(2).multiply(10000).rename(['co2flux'])   
        
        return img.addBands(co2FluxImg)



    def agregateBandsTexturasGLCM(self, img):
        
        img = img.toInt()                
        textura2 = img.select('B8').glcmTexture(3)  
        contrast = textura2.select('B8_contrast').divide(1000).rename('contrast') 

        return  contrast
        
    
    def agregateBandsgetFractions(self, img):

        # Define endmembers
        endmembers =  [
            [ 119.0,  475.0,  169.0, 6250.0, 2399.0,  675.0], #/*gv*/
            [1514.0, 1597.0, 1421.0, 3053.0, 7707.0, 1975.0], #/*npv*/
            [1799.0, 2479.0, 3158.0, 5437.0, 7707.0, 6646.0], #/*soil*/
            [4031.0, 8714.0, 7900.0, 8989.0, 7002.0, 6607.0], #/*cloud*/
            [   0.0,    0.0,    0.0,    0.0,    0.0,    0.0]  #/*Shade*/
        ]
        # Uminxing data
        fractions = ee.Image(img).select(self.options['bandas'])\
                        .unmix(endmembers= endmembers).float()
        
        fractions = fractions.select([0,1,2,3,4], self.options['bandsFraction'])        
        
        return img.addBands(fractions)


    def agregateBandsIndexNDFIA(self, img):

        # #calculate NDFI
        # ndfi = img.expression(
        #     "float(b('gv') - (b('npv') + b('soil'))) / float( b('gv') + b('npv') + b('soil'))")        
        # ndfi = ndfi.rename('ndfi')        
        
        #calculate NDFIa
        ndfia = img.expression(
            "float(b('gv') - b('soil')) / float( b('gv') + 2 * b('npv') + b('soil'))")        
        ndfia = ndfia.rename('ndfia')
        
        return img.select(['gv','npv','soil']).addBands(ndfi).addBands(ndfia) 

    
    def CalculateIndice(self, imageW):         
        
        geomet = imageW.geometry()
        # imagem em Int16 com valores inteiros ate 10000        
        imageF = self.agregateBandsgetFractions(imageW)
        imageF = self.agregateBandsIndexNDFIA(imageF)
        imageT = self.agregateBandsTexturasGLCM(imageW)        

        imageW = imageW.divide(10000)
        imageW = imageW.set('system:footprint', geomet)

        imageW = self.agregateBandsIndexEVI(imageW)         
        imageW = self.agregateBandsIndexRATIO(imageW) 
        imageW = self.agregateBandsIndexRVI(imageW)               
        imageW = self.agregateBandsIndexNDVI(imageW)
        imageW = self.agregateBandsIndexWater(imageW)
        imageW = self.AutomatedWaterExtractionIndex(imageW)        
        imageW = self.IndiceIndicadorAgua(imageW)
        imageW = self.agregateBandsIndexLAI(imageW) 
        imageW = self.agregateBandsIndexGCVI(imageW) 
        imageW = self.agregateBandsIndexCVI(imageW)               
        imageW = self.agregateBandsIndexOSAVI(imageW)
        imageW = self.agregateBandsIndexSoil(imageW) 
        imageW = self.agregateBandsIndexMSI(imageW)
        imageW = self.agregateBandsIndexwetness(imageW)         
        imageW = self.agregateBandsIndexBrightness(imageW) 

        imageW = self.agregateBandsIndexGVMI(imageW)
        imageW = self.agregateBandsIndexsPRI(imageW)         
        imageW = self.agregateBandsIndexCO2Flux(imageW)
        
        
        return imageW.addBands(imageF).addBands(imageT)


def exportarClassification(imgTransf, nameAl, geomet):
    
    # IdAsset = 'projects/mapbiomas-arida/ALERTAS/alertas-brutos/creados/' + nameAl    
    IdAsset = 'projects/mapbiomas-arida/ALERTAS/alertas-brutos/gerados/' + nameAl
    print(" en id Asset:")
    print("   <> {}".format(IdAsset))
    
    optExp = {
        'image': imgTransf, #.toInt16()
        'description': nameAl, 
        'assetId':IdAsset, 
        'pyramidingPolicy': {".default": "mode"},  
        'region': geomet.getInfo()['coordinates'],
        'scale': 10,
        'maxPixels': 1e13 
    }

    task = ee.batch.Export.image.toAsset(**optExp)    
    task.start()
    print("reporte do status")

    for keys, vals in dict(task.status()).items():
        print ( "  {} : {}".format(keys, vals))
    
    print ("salvando ... ! ")

## https://code.earthengine.google.com/4aa004aae390f0c4dc5708ece511796b
## https://code.earthengine.google.com/f308b42668bed2d6917a03ad362fd1e8
params = {
    "max16bit": 65536,
    "ccobert": 60,
    "start": None,
    "end": None,   
    "mes": None,
    "ano": 2020,
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],        
    "listclassesMB": [1,2,3,4,5,9,10,12], 
    "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/',
    "gradeS2": 'users/solkancengine17/shapes/grade_sentinel_brasil',
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
    'isCaatinga': True,
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

lsIndMin = []
lsIndMax = []

if params['isCaatinga']:
    lsTiles = auxiliar.lsTilesCaat
else:
    lsTiles = auxiliar.lsTilesBa

params['start'] = '2020-01-01'
params['end'] = '2020-12-31'


gradeS2 = ee.FeatureCollection(params['gradeS2'])

datasetSent2 = ee.ImageCollection('COPERNICUS/S2_SR')\
    .filterDate(params['start'], params['end'])\
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert']))\
    .select(params["bandasAll"])

datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
    .filterDate(params['start'], params['end'])

print('Imagem de referencia \n ====> ' + auxiliar.imgRefCaat)
operadorMosaic = ClassCalcIndicesSpectral(auxiliar.imgRefCaat)
operadorMosaic.imgColClouds = datasetCloudS2


for tile in lsTiles[:2]:  

    geomet = gradeS2.filter(ee.Filter.eq('NAME', tile)).geometry() 
    
    newDataset = datasetSent2.filter(ee.Filter.eq('MGRS_TILE', tile))
    numImg = newDataset.size().getInfo()
    print("Para o << {} >> temos # {}  imagens".format(tile, numImg))

    lsIndexImg = newDataset.reduceColumns(ee.Reducer.toList(), ['system:index']).get('list').getInfo()

    for nameId in lsIndexImg:
        print(nameId) 

    ## remoção de Nuvens
    # newDataset = newDataset.map(lambda image: operadorMosaic.maskS2clouds(image))
    # ##  matchiong histogram 
    # newDataset = newDataset.map(lambda image: operadorMosaic.match_Images(image))

    # print(newDataset.first().bandNames().getInfo())
    # ## Clac
    # newDatasetInd = newDataset.map(lambda image: operadorMosaic.CalculateIndice(image))

    # lsBndEsp = newDatasetInd.first().bandNames().getInfo()
    # print(lsBndEsp)

    # ## Reducers Meand
    # imgAnalitic = ee.Image().float()
    # reducer = 'median_'
    
    # for bnd in lsBndEsp:

    #     bandTemp = ee.Image(newDatasetInd.select(bnd).mean()).rename(reducer + bnd)
    #     bandTemp = bandTemp.add(1).multiply(10000).toUint16()
    #     imgAnalitic = imgAnalitic.addBands(bandTemp)

    # ## Reducers Minimum
    # reducer = 'min_'
    # for bnd in lsIndMin:

    #     bandTemp = ee.Image(newDatasetInd.select(bnd).min()).rename(reducer + bnd)
    #     bandTemp = bandTemp.add(1).multiply(10000).toUint16()
    #     imgAnalitic = imgAnalitic.addBands(bandTemp)
    
    # ## Reducers Maximum
    # reducer = 'max_'
    # for bnd in lsIndMax:

    #     bandTemp = ee.Image(newDatasetInd.select(bnd).max()).rename(reducer + bnd)
    #     bandTemp = bandTemp.add(1).multiply(10000).toUint16()
    #     imgAnalitic = imgAnalitic.addBands(bandTemp)
    
    # # set properties
    # imgAnalitic = imgAnalitic.clip(geomet)
    # imgAnalitic = imgAnalitic.set('system:footprint', geomet)
    # imgAnalitic = imgAnalitic.set('year', params['ano'])
    # imgAnalitic = imgAnalitic.set('MGRS_TILE', tile)
    # imgAnalitic = imgAnalitic.set('NUM_IMAGENS', numImg)

    # # save imagens 
    # nameAl = params['ano'] + '_' + tile
    # exportarClassification(imgAnalitic, nameAl, geomet)