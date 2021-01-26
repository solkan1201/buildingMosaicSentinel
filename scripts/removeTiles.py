import ee
import sys
try:
    ee.Initialize()
    print('The Earth Engine package initialized successfully!')
except ee.EEException as e:
    print('The Earth Engine package failed to initialize!')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


bandasInd = [
            'blue', 'green', 'red', 'nir', 'swir1', 'siwr2', 
            'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', 
            'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', 
            'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', 
            'soil', 'ndfia', 'contrast'
        ]

# dictArqReg = {    
    # '52': ["24MXA"],
    # '95': ["24LTJ","24LUK","24LUL","24LUN","24LVL","24MVB","24MWA","24MXA",],  
    # '95': ["23LRD","24LTJ","24LUJ","24LVM"],  
    # '138': ["23MPM","23MQM","23MQN","23MRN","23MRQ","23MRR","23MRS","24MTA",
    #         "24MTT","24MTV","23KPB","23LND","23LNE","23LNF","23LNG","23LNH",
    #         "23LPG","23LPH","23LQE"]
# }

dictArqRegOther = {    
    '52': [
            "24LVM",
            "24MWT","24MXT","24MXV","24MYS","24MYV","24MZS","24MZV",
            "24LWQ","24LWR"
            ],
    '95': ["24LTQ","24LVR","24LWR","24MUA","24MUB","24MVB","24MWA","24MWB",
            "24MXA"],  
    '138': ["23MRS","24LTQ","24MTB","24MUA","24MUB","23LQJ","23LQK","23LRK"]
}

pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2'
pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics'
mosaicS2 = ee.ImageCollection(pathMosaic)
mS2Caat = ee.ImageCollection(pathMosaicMB)
mS2Caat = mS2Caat.merge(mosaicS2)
print("Numero de imagens carregadas {} no mosaic".format(mosaicS2.size().getInfo()))

# cont = 0
# for orb, lstile in dictArqReg.items():

#     for tile in lstile:

#         for bnd in bandasInd:

#             for lado in ['A', 'B']:

#                 nomeImg = '2020_' + orb + "_" + tile + "_" + lado + "_median" + "_" + bnd + '_year'
#                 idAssetImg = pathMosaicMB + '/' + nomeImg

#                 try:
#                     ee.data.deleteAsset(idAssetImg)
#                     print("eliminando ❌ ... item 📍 " + nomeImg)
#                     cont += 1
#                 except:
#                     print("no existe " + nomeImg)

# print("quantidade de imagens removidas {} ".format(cont))

cont = 0
for orb, lstile in dictArqRegOther.items():

    for tile in lstile:

        for bnd in bandasInd:

            for lado in ['A', 'B']:

                nomeImg = '2020_' + orb + "_" + tile + "_" + lado + "_median" + "_" + bnd + '_year'
                idAssetImg = pathMosaicMB + '/' + nomeImg

                try:
                    ee.data.deleteAsset(idAssetImg)
                    print("eliminando ❌ ... item 📍 " + nomeImg)
                    cont += 1
                
                except:
                    print("no existe " + nomeImg)

print("quantidade de imagens removidas novas {} ".format(cont))