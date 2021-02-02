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

    geomet = None
    footprint = None 

    imgColClouds = None

    def __init__(self, colClouds):

        print("inicializando o objeto")
        self.imgColClouds = colClouds
       

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

    def strecht_Images(self, image):   

        image = self.maskS2clouds(image)
        image = image.clip(self.geomet)     

        matching = ee.Image().uint16()  

        for band in self.options['bandas']:

            imgTemp = self.NomalizeImg(image, band, self.geomet)

            imgTemp = imgTemp.rename(band)        

            matching = matching.addBands(imgTemp)

        matching = ee.Image.cat(matching.select(self.options['bandas'])) 
        matching = matching.set('system:footprint', self.footprint)
        # matching = matching.set()       

        return matching

    
    ######################################################################################
    ## // Function to calculate illumination condition (IC). Function by Patrick Burns ###
    ## // (pb463@nau.edu) and Matt Macander                                            ###
    ## // (mmacander@abrinc.com)                                                       ###
    ######################################################################################
    

    def agregateBandsIndexRATIO(self, img):
    
        ratioImg = img.expression("float(b('B8') / b('B4'))")\
                                .multiply(1000).rename(['ratio'])      

        # return img.addBands(ratioImg)
        return ratioImg

    def agregateBandsIndexRVI(self, img):
    
        rviImg = img.expression("float(b('B4') / b('B8'))")\
                                .multiply(1000).rename(['rvi'])       

        # return img.addBands(rviImg)
        return rviImg

    
    def agregateBandsIndexNDVI(self, img):
    
        ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")\
                                .add(1).multiply(10000).rename(['ndvi'])       

        # return img.addBands(ndviImg)
        return ndviImg

    
    def agregateBandsIndexWater(self, img):
    
        ndwiImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")\
                                .add(1).multiply(10000).rename(['ndwi'])       

        return img.addBands(ndwiImg)
    
    
    def AutomatedWaterExtractionIndex(self, img):
    
        awei = img.expression(
                            "float(4 * (b('B3') - b('B12')) - (0.25 * b('B8') + 2.75 * b('B11')))"
                        ).add(5).multiply(10000).rename("awei")          
        
        # return img.addBands(awei)
        return awei


    def IndiceIndicadorAgua(self, img):
    
        iiaImg = img.expression(
                            "float((b('B3') - 4 *  b('B8')) / (b('B3') + 4 *  b('B8')))"
                        ).add(1).multiply(10000).rename("iia")
        
        # return img.addBands(iiaImg)
        return iiaImg


    def agregateBandsIndexEVI(self, img):
            
        eviImg = img.expression(
            "float(2.4 * (b('B8') - b('B4')) / (1 + b('B8') + b('B4')))").divide(10)\
                .add(1).multiply(10000).rename(['evi'])     
        
        return img.addBands(eviImg)
    
    
    def agregateBandsIndexLAI(self, img):
    
        laiImg = img.expression(
            "(3.618 * float(b('evi') - 0.118))").divide(10)\
                .add(1).multiply(1000).rename(['lai'])     
    
        # return img.addBands(laiImg)
        return laiImg
    

    def agregateBandsIndexGCVI(self, img):
    
        gcviImgA = img.expression(
            "float(b('B8')) / (b('B3')) - 1")\
                .add(1).multiply(10000).rename(['gcvi'])        
        
        # return img.addBands(gcviImgA)
        return gcviImgA
    

    # Chlorophyll vegetation index
    def agregateBandsIndexCVI(self, img):
    
        cviImgA = img.expression(
            "float(b('B8') * (b('B3') / (b('B2') * b('B2'))))").multiply(100)\
                .rename(['cvi'])        
        
        # return img.addBands(cviImgA)
        return cviImgA
    
    
    def agregateBandsIndexOSAVI(self,img):
    
        osaviImg = img.expression(
            "float(b('B8') - b('B4')) / (0.16 + b('B8') + b('B4'))")\
                .add(1).multiply(10000).rename(['osavi'])        
        
        # return img.addBands(osaviImg)
        return osaviImg
    
    
    def agregateBandsIndexSoil(self, img):
        
        soilImg = img.expression(
            "float(b('B8') - b('B3')) / (b('B8') + b('B3'))")\
                .add(1).multiply(10000).rename(['isoil'])       
        
        # return img.addBands(soilImg)    
        return soilImg 
    
    def agregateBandsIndexBAI(self, img):
    
        baiImg = img.expression(
            "float(1) / ((0.1 - b('B4'))**2 + (0.06 - b('B8'))**2)")\
                .rename(['bai']) 
        
        # return img.addBands(baiImg)
        return baiImg
    
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
        
        # return img.addBands(tasselledCapImg)
        return tasselledCapImg
    
    # Tasselled Cap - wetness 
    def agregateBandsIndexwetness(self, img):
    
        tasselledCapImg = img.expression(
            "float(0.1509 * b('B2') + 0.1973 * b('B3') + 0.3279 * b('B4')  + 0.3406 * b('B8') + 0.7112 * b('B11') +  0.4572 * b('B12'))")\
                .multiply(10000).rename(['wetness']) 
        
        # return img.addBands(tasselledCapImg)
        return tasselledCapImg
    
    # Moisture Stress Index (MSI)
    def agregateBandsIndexMSI(self, img):
    
        msiImg = img.expression(
            "float( b('B8') / b('B11'))").multiply(1000)\
                .rename(['msi']) 
        
        # return img.addBands(msiImg)
        return msiImg
    
    
    def agregateBandsIndexGVMI(self, img):
        
        gvmiImg = img.expression(
                        "float ((b('B8')  + 0.1) - (b('B11') + 0.02)) / ((b('B8') + 0.1) + (b('B11') + 0.02))" 
                    ).add(1).multiply(10000).rename(['gvmi'])     
    
        # return img.addBands(gvmiImg)
        return gvmiImg
    
    
    def agregateBandsIndexsPRI(self, img):
        
        priImg = img.expression(
                                "float((b('B3') - b('B2')) / (b('B3') + b('B2')))"
                            ).rename(['pri'])   
        spriImg =   priImg.expression(
                                "float((b('pri') + 1) / 2)").multiply(10000).rename(['spri'])  
    
        # return img.addBands(spriImg)
        return spriImg
    

    def agregateBandsIndexCO2Flux(self, img):
        
        co2FluxImg = img.expression("float(b('ndvi') * b('spri'))"
                                ).add(2).multiply(10000).rename(['co2flux'])   
        
        # return img.addBands(co2FluxImg)
        return co2FluxImg



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

        #calculate NDFIa
        ndfia = img.expression(
            "float(b('gv') - b('soil')) / float( b('gv') + 2 * b('npv') + b('soil'))")        
        ndfia = ndfia.add(1).rename('ndfia')
        
        return img.select(['gv','npv','soil']).addBands(ndfia) #.addBands(ndfi)

    
    def CalculateIndice(self, imageW, indice ):         
        
        # imageW = self.maskS2clouds(imageW)

        # imageW = self.strecht_Images(imageW, geomet)
        # imageW = imageW.set('system:footprint', geomet)

        # por causa do bucket  a imagem sai com [0, 10.000]
        # imageW = self.match_Images(imageW)        
        
        if indice in ['gv', 'npv', 'soil', 'ndfia']:
            # imagem em Int16 com valores inteiros ate 10000        
            imageF = self.agregateBandsgetFractions(imageW)
            if  indice == 'ndfia':
                imageF = self.agregateBandsIndexNDFIA(imageF)
            
            return imageF.multiply(10000).select(indice)
        
        # capturando textura  
        elif  indice == 'contrast':
            imageT = self.agregateBandsTexturasGLCM(imageW)    

            return imageT.select(indice)

        imageW = imageW.divide(10000)
        imageW = imageW.set('system:footprint', self.geomet)
        
        
        if indice == 'evi':
            imageW = self.agregateBandsIndexEVI(imageW)    
        elif  indice == 'ratio':
            imageW = self.agregateBandsIndexRATIO(imageW) 
        elif  indice == 'rvi':
            imageW = self.agregateBandsIndexRVI(imageW)  
        elif  indice == 'ndvi':             
            imageW = self.agregateBandsIndexNDVI(imageW)
        elif  indice == 'ndwi':
            imageW = self.agregateBandsIndexWater(imageW)
        elif  indice == 'awei':
            imageW = self.AutomatedWaterExtractionIndex(imageW)        
        elif  indice == 'iia':
            imageW = self.IndiceIndicadorAgua(imageW)
        elif  indice == 'lai':
            imageW = self.agregateBandsIndexEVI(imageW)
            imageW = self.agregateBandsIndexLAI(imageW) 
        elif  indice == 'gcvi':
            imageW = self.agregateBandsIndexGCVI(imageW) 
        elif  indice == 'cvi':
            imageW = self.agregateBandsIndexCVI(imageW)               
        elif  indice == 'osavi':
            imageW = self.agregateBandsIndexOSAVI(imageW)
        elif  indice == 'isoil':
            imageW = self.agregateBandsIndexSoil(imageW) 
        elif  indice == 'msi':
            imageW = self.agregateBandsIndexMSI(imageW)
        elif  indice == 'wetness':
            imageW = self.agregateBandsIndexwetness(imageW)         
        elif  indice == 'brightness':
            imageW = self.agregateBandsIndexBrightness(imageW) 
        elif  indice == 'gvmi':
            imageW = self.agregateBandsIndexGVMI(imageW)
        elif  indice == 'spri':
            imageW = self.agregateBandsIndexsPRI(imageW)         
        elif  indice == 'co2flux':
            imageW = self.agregateBandsIndexCO2Flux(imageW)        
        
        return imageW #.addBands(imageF).addBands(imageT)


def exportarClassification(imgTransf, nameAl, geomet):
    
    # IdAsset = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics/' + nameAl 
    # IdAsset = 'users/mapbiomascaatinga05/mosaicSentinel2/' + nameAl
    IdAsset = 'users/mapbiomascaatinga05/mosaicTestS2/'  + nameAl 
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
    "year": 2020,
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],     
    "assetLimBra": 'users/CartasSol/shapes/Brasil_Buffer3km',  
    "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/', 
    "gradeS2Corr": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat',  
    "gradeS2Div": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeNordeC',    
    'pathHome': "/home/superusuario/Dados/projAlertas/tabFeitas/",
    'path_TF': "/tabFeitas/",    
    'isCaatinga': True,
    'periodo': 'year',    # 'dry', 'wet'
    'imgRef': {
        'year': 'COPERNICUS/S2_SR/20200702T130251_20200702T130252_T24MVS',
        'dry': 'COPERNICUS/S2_SR/20200930T130251_20200930T130253_T24MVS'
    },
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
grades_Solape = [
            '25LBL','25MBM','25MBN','25MBP','24KTG','24LTH','24LTJ','24LTK',
            '24LTL','24LTM','24LTN','24LTP','24LTQ','24LTR','24MTA','24MTB',
            '24MTS','24MTT','24MTU','24MTV','23KKB','23LKC','23LKD','23LKE',
            '23LKF','23LKG','23LKH','23LKJ','23LKK','23LKL','23MKM','23MKN',
            '23MKP','23MKQ','23MKR','23MKS','23MKT','23MKU'
        ]
listException = ['52_24MXA']
bandasInd = [
            'blue', 'green', 'red', 'nir', 'swir1', 'siwr2' 
            # 'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
            # 'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
            # 'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
            # 'soil', 'ndfia', 'contrast'
        ]

lsBND_ind = [
            'B2', 'B3', 'B4', 'B8', 'B11', 'B12'
            # 'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
            # 'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
            # 'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
            # 'soil', 'ndfia', 'contrast'
        ]
lsIndMin = []
lsIndMax = []

# if params['isCaatinga']:
#     lsTiles = auxiliar.lsTilesCaat
# else:
#     lsTiles = auxiliar.lsTilesBa

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


datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
    .filterDate(params['start'], params['end'])


operadorMosaic = ClassCalcIndicesSpectral(datasetCloudS2)
# operadorMosaic.imgColClouds = datasetCloudS2


reducer = '_median'
# lsMedian = [ibnd + reducer for ibnd in bandasInd]
limiteImg = 15

for orbNo, lsTiles in tiles_Orb.dictArqReg.items():

    for tile in lsTiles:  

        item = str(orbNo) + '_' + tile

        print("Processando imagens de orbita  📡 {} >>  e tile 📡 {} >> ".format(orbNo, tile))

        geomet = gradeS2.filter(ee.Filter.And(
                                            ee.Filter.eq('MGRS_TILE', tile),
                                            ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))
                                        )).geometry() 
        
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

        print("numero de imagens {}".format(newDataset.size().getInfo()))
        
        for lado in ['A', 'B']:

            geometDiv = gradeDiv.filter(ee.Filter.eq('label', tile + '_' + lado)).geometry()
            gradeInGeo = geomet.intersection(geometDiv)            
            gradeInter = ee.Geometry(gradeInGeo.intersection(limiteCaat))
            del gradeInGeo
            areaInt = gradeInter.area(1).getInfo()
            print("area #### {} ####".format(areaInt))           
            
            # print(gradeInter.getInfo())
            if (tile in grades_Solape and lado == 'B') or areaInt < 1000:
                print("###############################################################")
                print(" 🔰 lado B 🔰 da orbita __{}__ e tile __{}__ NÃO SERÁ PROCESSADO".format(orbNo, tile))
                print("###############################################################")
                continue           
            
            else:
                print("ntro")
                footprint = gradeInter.getInfo()['coordinates']
                print("footprint com {} pontos para o poligon \n".format( len(footprint[0])))
                
                try:
                    # newDatsetDiv = newDataset.map(lambda image: image.clip(gradeInter))
                    # newDatsetDiv = newDataset.map(lambda image: image.set('system:footprint', footprint)) 
                    print("====> enviandos a geometria limite e a lista de pontos limites #####")
                    numImg = newDataset.size()#.getInfo()                       
                    operadorMosaic.geomet = gradeInter
                    operadorMosaic.footprint = footprint        
                    ## remoção de Nuvens        
                    #  matchiong histogram 
                    newDatsetDiv = newDataset.map(lambda image: operadorMosaic.strecht_Images(image))
                    # print(newDataset.first().bandNames().getInfo())
                    ## Clac
                    print("reduzindo a mediana")
                    imgAnalitic = newDatsetDiv.median()     
                    print(imgAnalitic.bandNames().getInfo())
                    imgAnalitic = imgAnalitic.select(lsBND_ind)
                    imgAnalitic = imgAnalitic.rename(bandasInd)
                    
                    print('Set properties to imagesss')
                    # set properties
                    # imgAnalitic = imgAnalitic.addBands(std_imgAnalitic)
                    # imgAnalitic = imgAnalitic.clip(gradeInter)
                    imgAnalitic = imgAnalitic.set('system:footprint', footprint)
                    imgAnalitic = imgAnalitic.set('year', params['year'])
                    imgAnalitic = imgAnalitic.set('MGRS_TILE', tile)
                    imgAnalitic = imgAnalitic.set('SENSING_ORBIT_NUMBER', orbNo)
                    imgAnalitic = imgAnalitic.set('NUM_IMAGENS', numImg)
                    # imgAnalitic = imgAnalitic.set('banda', bndMedian)
                    imgAnalitic = imgAnalitic.set('periodo', params['periodo'])  
                    imgAnalitic = imgAnalitic.set('lado', lado)          

                    # save imagens 
                    nameAl = str(params['year']) + '_' + str(orbNo)  + '_' + tile + '_' + lado + '_' + params['periodo']  
                    exportarClassification(imgAnalitic, nameAl, geomet)

                except:

                    print("#############🔰 ALGO DEU ERRO NO PROCESSO    🔰######################")