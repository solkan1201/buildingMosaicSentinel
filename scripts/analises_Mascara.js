var visImg = {
    bands: ["B4","B3","B2"],
    max: 2000,
    min: 200
};

var band = ['B2', 'B3', 'B4', 'B8', 'B11', 'B12']
var datasetCloudS2 = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
                        .filterDate('2020-01-01', '2020-12-31')
var newDataset = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(
                                '2020-01-01', '2020-12-31').filter(
                                        ee.Filter.eq('SENSING_ORBIT_NUMBER', 52)).filter(
                                            ee.Filter.eq('MGRS_TILE', "24LVM")).filter(
                                                ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 40)).sort(                                                
                                                    'CLOUDY_PIXEL_PERCENTAGE')//;.select(params["bandasAll"])
                                                    .limit(5)
print(newDataset)

var lsId = newDataset.reduceColumns(ee.Reducer.toList(), ['system:index']).get('list').getInfo()

var imglist = ee.List([])

lsId.forEach(function(idIm){
    
    var imgTemp = newDataset.filter(ee.Filter.eq('system:index', idIm))
                            .first().select(band)
                            
    var imgMask = datasetCloudS2.filter(ee.Filter.eq('system:index', idIm)).first()
    
    imgMask = imgMask.lt(20).focal_min(1.5).rename('mask')
    
    imgTemp = imgTemp.updateMask(imgMask).addBands(imgMask)  
    
    print("imagem ==> " + idIm + ': ', imgTemp)
    
    Map.addLayer(imgTemp, visImg, idIm, false)
    
    Map.addLayer(imgMask, {min: 0, max: 1}, idIm, false)
    
    imglist = imglist.add(imgTemp)
    
})

imglist = ee.ImageCollection(imglist)
var imgMosaic = imglist.median()

Map.addLayer(imgMosaic, visImg, 'Mosaic')