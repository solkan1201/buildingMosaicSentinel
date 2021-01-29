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
        "Feature" :['evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
                    'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
                    'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
                    'soil', 'ndfia', 'contrast'], 
        'bandsFraction': ['gv','npv','soil','cloud', 'shade'], 
        'scale': 300,
        'toaOrSR' : 'SR',
        'degree2radian' : 0.01745
    }  

    dictClassifRef = {}

    geomet = None
    geomet = None
    footprint = None   


    def __init__(self, idRef):

        self.imgRef_ = ee.Image(idRef)
        
        geomRef = self.imgRef_.geometry()

        self.imgRef_  = self.imgRef_.select(self.options['bandas'])              
    
        # self.imgRef_  = self.strecht_Images(self.imgRef_, geomRef)

        # salvando em um diccionario as propiedades dde Classify da ref
        self.equalizeRef(geomRef)

        self.dem = ee.Image("USGS/SRTMGL1_003")


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

        image = self.maskS2clouds(image)
        # image = self.strecht_Images(image, self.geomet)

        matching = ee.Image().uint16()    
        
        for band in self.options['bandas']:

            imgTemp = self.equalize(image.clip(self.geomet), band, self.geomet)
            
            imgTemp = imgTemp.toUint16()#.clip(self.geomet)

            matching = matching.addBands(imgTemp)

        matching = ee.Image.cat(matching.select(self.options['bandas']))
        matching = matching.set('system:footprint', self.geomet)
        
        return matching
    
    ######################################################################################
    ## // Function to calculate illumination condition (IC). Function by Patrick Burns ###
    ## // (pb463@nau.edu) and Matt Macander                                            ###
    ## // (mmacander@abrinc.com)                                                       ###
    ######################################################################################
    def illuminationCondition(self, img):

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
    def illuminationCorrection(self, img):

        props = img.toDictionary()
        st = img.get('system:time_start')

        img_plus_ic = img
        mask1 = img_plus_ic.select('nir').gt(-0.1)
        mask2 = img_plus_ic.select('slope').gte(5).And(
                            img_plus_ic.select('IC').gte(0)).And(
                            img_plus_ic.select('nir').gt(-0.1))
        

        img_plus_ic_mask2 = ee.Image(img_plus_ic.updateMask(mask2))

        ### Specify Bands to topographically correct ###
        bandList = ['blue','green','red','nir','swir1','swir2']
        bandList = ['B2','B3','B4','B8','B11','B12']
        compositeBands = img.bandNames()
        nonCorrectBands = img.select(compositeBands.removeAll(bandList))

        geom = ee.Geometry(img.get('system:footprint')).bounds().buffer(10000)


        def apply_SCSccorr(band):

            method = 'SCSc'
            pmtroRed = {
                'reducer': ee.Reducer.linearRegression(2,1), 
                'geometry': ee.Geometry(img.geometry()), 
                'scale': scale, 
                'bestEffort': True,
                'maxPixels': 1e10
            }
            
            out =  ee.Image(1).addBands(img_plus_ic_mask2.select('IC', band))\
                            .reduceRegion(pmtroRed)

            fit = out.combine({"coefficients": ee.Array([[1],[1]])}, false)
            
            out_a = (ee.Array(fit.get('coefficients')).get([0,0]))
            out_b = (ee.Array(fit.get('coefficients')).get([1,0]))
            out_c = out_a.divide(out_b)

            expression = "(( b('" + band + "')* (b('cosS') * b('cosZ') + b('outC'))) / (b('IC') + b('outC')))"

            SCSc_output = img_plus_ic_mask2.addBands(ee.Image(out_c).rename('outC')).expression(expression)

            return SCSc_output
        
        imgList = ee.Image().float()

        for bnd in bandList:
            tempIm = apply_SCSccorr(bnd)
            imgList = imgList.addBands(ee.Image(tempIm))
        
        img_SCSccorr = imgList.select(bandList).addBands(img_plus_ic.select('IC'))
        bandList_IC = ee.List(bandList).add('IC')
        img_SCSccorr = img_SCSccorr.unmask(img_plus_ic.select(bandList_IC)).select(bandList)
        
        return img_SCSccorr.addBands(nonCorrectBands).set('system:time_start', st)


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
    
    
    def AutomatedWaterExtractionIndex(self, img):
    
        awei = img.expression(
                            "float(4 * (b('B3') - b('B12')) - (0.25 * b('B8') + 2.75 * b('B11')))"
                        ).add(5).multiply(10000).rename("awei")          
        
        return img.addBands(awei)

    def IndiceIndicadorAgua(self, img):
    
        iiaImg = img.expression("float((b('B3') - 4 *  b('B8')) / (b('B3') + 4 *  b('B8')))"
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
            "float(b('B8') * (b('B3') / (b('B2') * b('B2'))))").multiply(100)\
                .rename(['cvi'])        
        
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
        # return spriImg
    

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

        #calculate NDFIa
        ndfia = img.expression(
            "float(b('gv') - b('soil')) / float( b('gv') + 2 * b('npv') + b('soil'))")        
        ndfia = ndfia.add(1).rename('ndfia')
        
        return img.select(['gv','npv','soil']).addBands(ndfia) #.addBands(ndfi)

    
    def CalculateIndice(self, imageW):         
        
        # imageW = self.maskS2clouds(imageW)
        # imageW = self.strecht_Images(imageW, geomet)
        # imageW = imageW.set('system:footprint', geomet)
        # por causa do bucket  a imagem sai com [0, 10.000]
        # imageW = self.match_Images(imageW)        
        
        # imagem em Int16 com valores inteiros ate 10000        
        imageF = self.agregateBandsgetFractions(imageW)        
        imageF = self.agregateBandsIndexNDFIA(imageF)
        imageF = imageF.multiply(10000)
        # capturando textura          
        imageT = self.agregateBandsTexturasGLCM(imageW)        

        imageWd = imageW.divide(10000)
        imageWd = imageWd.set('system:footprint', self.geomet)        
        
        imageWd = self.agregateBandsIndexEVI(imageWd)         
        imageWd = self.agregateBandsIndexRATIO(imageWd)        
        imageWd = self.agregateBandsIndexRVI(imageWd)  
        imageWd = self.agregateBandsIndexNDVI(imageWd)        
        imageWd = self.agregateBandsIndexWater(imageWd)        
        imageWd = self.AutomatedWaterExtractionIndex(imageWd)         
        imageWd = self.IndiceIndicadorAgua(imageWd)              
        imageWd = self.agregateBandsIndexLAI(imageWd)       
        imageWd = self.agregateBandsIndexGCVI(imageWd)        
        imageWd = self.agregateBandsIndexCVI(imageWd)               
        imageWd = self.agregateBandsIndexOSAVI(imageWd)        
        imageWd = self.agregateBandsIndexSoil(imageWd)        
        imageWd = self.agregateBandsIndexMSI(imageWd)        
        imageWd = self.agregateBandsIndexwetness(imageWd)            
        imageWd = self.agregateBandsIndexBrightness(imageWd)         
        imageWd = self.agregateBandsIndexGVMI(imageWd)        
        imageWd = self.agregateBandsIndexsPRI(imageWd)          
        imageWd = self.agregateBandsIndexCO2Flux(imageWd)    

        imageWd = imageWd.select(self.options['Feature'])    
        
        return imageW.addBands(imageWd).addBands(imageF).addBands(imageT)


def exportarClassification(imgTransf, nameAl, geomet):
    
    IdAsset = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics/' + nameAl    
    # IdAsset = 'users/mapbiomascaatinga05/mosaicSentinel2/' + nameAl
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
    "ccobert": 50,
    "start": None,
    "end": None,   
    "mes": None,
    "ano": 2020,
    "bandasAll": ['B2','B3', 'B4', 'B8', 'B11', 'B12'],     
    "assetLimBra": 'users/CartasSol/shapes/Brasil_Manual', 
    # "idassetOut": 'users/Tarefa01_MAPBIOMAS/teste_alerta_caatinga/ver1/', 
    "idassetOut": 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC',
    "gradeS2Corr": 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat',       
    'pathHome': "/home/superusuario/Dados/projAlertas/tabFeitas/",
    'path_TF': "/tabFeitas/",
    'numeroTask': 0,
    'numeroLimit': 85,
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
            '23MKP','23MKQ','23MKR','23MKS','23MKT','23MKU'  #,'24MXU'
        ]

bandasInd = [
            'blue', 'green', 'red', 'nir', 'swir1', 'siwr2', 
            'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
            'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
            'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
            'soil', 'ndfia', 'contrast'
        ]

lsBND_ind = [
            'B2', 'B3', 'B4', 'B8', 'B11', 'B12', 
            'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
            'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
            'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
            'soil', 'ndfia', 'contrast'
        ]
lsIndMin = []
lsIndMax = []

# if params['isCaatinga']:
#     lsTiles = auxiliar.lsTilesCaat
# else:
#     lsTiles = auxiliar.lsTilesBa
# suf = ''
imgRefCaat = params['imgRef']['year']


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

datasetSent2 = ee.ImageCollection('COPERNICUS/S2_SR')\
    .filterDate(params['start'], params['end'])\
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', params['ccobert']))\
    .select(params["bandasAll"])

datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
    .filterDate(params['start'], params['end'])

print('Imagem de referencia \n ====> ' + tiles_Orb.imgRefCaat)
operadorMosaic = ClassCalcIndicesSpectral(tiles_Orb.imgRefCaat)
operadorMosaic.imgColClouds = datasetCloudS2


reducer = '_median'
lsMedian = [ibnd + reducer for ibnd in bandasInd]

for orbNo, lsTiles in tiles_Orb.dictArqReg.items():

    for tile in lsTiles:  

        geomet = gradeS2.filter(ee.Filter.And(
                                            ee.Filter.eq('MGRS_TILE', tile),
                                            ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo))
                                        )).geometry() 
        
        operadorMosaic.geomet = geomet        
        newDataset = datasetSent2.filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', int(orbNo)))\
                                .filter(ee.Filter.eq('MGRS_TILE', tile))
        
        
        numImg = newDataset.size()#.getInfo()        
        print("Processando imagens de orbita  📡 {} >>  e tile 📡 {} >> ".format(orbNo, tile))
        # print(numImg)
        # lsIndexImg = newDataset.reduceColumns(ee.Reducer.toList(), ['system:index']).get('list').getInfo()

        # for nameId in lsIndexImg:
        #     print(nameId) 

        ##  remoção de Nuvens        
        ##  matchiong histogram 
        newDataset = newDataset.map(lambda image: operadorMosaic.match_Images(image))
        # print("bandas ", newDataset.first().bandNames().getInfo())
        # print(newDataset.filter(ee.Filter.eq(
        #             "system:index", '20200111T125301_20200111T125302_T24LXR')).first().bandNames().getInfo())
        ## Clac
       
        newDatasetInd = newDataset.map(lambda image: operadorMosaic.CalculateIndice(image))
        # print("All bandas ", newDatasetInd.first().bandNames().getInfo())
        ##########################################
        ########  Reducers Median cc  ############ 
        # print(bandasInd[cc])
        # reducer = 'median_'         
        # bndMedian =  reducer + bandasInd[cc]
        
        imgAnalitic = newDatasetInd.median().toUint16()        
        imgAnalitic = imgAnalitic.select(lsBND_ind, lsMedian)
        # print("bandas do mosaico ", imgAnalitic.bandNames().getInfo())
        imgAnalitic = imgAnalitic.clip(geomet)

        #print("bandas seleccionadas {}".format(imgAnalitic.bandNames().getInfo()))

        # imgAnalitic = imgAnalitic.rename(bndMedian)
        # print(imgAnalitic.bandNames().getInfo())

        ########################################
        ####### Reducers Desvio Padrão   #######
        # reducer = 'stdDev_'       
        # lsstdDev = [reducer + ibnd for ibnd in bandasInd]
        # std_imgAnalitic = newDatasetInd.reduce(
        #                         reducer= ee.Reducer.stdDev(), 
        #                         parallelScale= 2).toUint16()

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
        
        # set properties
        # imgAnalitic = imgAnalitic.addBands(std_imgAnalitic)
        imgAnalitic = imgAnalitic.clip(geomet)
        imgAnalitic = imgAnalitic.set('system:footprint', geomet)
        imgAnalitic = imgAnalitic.set('year', params['ano'])
        imgAnalitic = imgAnalitic.set('MGRS_TILE', tile)
        imgAnalitic = imgAnalitic.set('SENSING_ORBIT_NUMBER', orbNo)
        imgAnalitic = imgAnalitic.set('NUM_IMAGENS', numImg)
        # imgAnalitic = imgAnalitic.set('banda', bndMedian)
        imgAnalitic = imgAnalitic.set('periodo', params['periodo'])

        # save imagens 
        nameAl = str(params['ano']) + '_' + str(orbNo)  + '_' + tile  + '_' + params['periodo']
        exportarClassification(imgAnalitic, nameAl, geomet)