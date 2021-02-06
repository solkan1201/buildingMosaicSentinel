var visImg = {
    bands: ["median_red","median_green","median_blue"],
    max: 2000,
    min: 200
};


var orb = '138';  // 52,138, 138
var tile = "23LRK";  //"24LVM","23LQJ", "23LRK"
var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);
print(mosaicS2);
mS2Caat = mS2Caat.merge(mosaicS2);
print(mS2Caat.limit(10));

var imgColtile = mS2Caat.filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', orb))
                     .filter(ee.Filter.eq('MGRS_TILE', tile))
                        
print(imgColtile)

var geomet = imgColtile.geometry()//.union()
print(geomet)
var mS2CaatBlue = imgColtile.filter(ee.Filter.eq('banda', 'median_blue'))
var mS2CaatGreen = imgColtile.filter(ee.Filter.eq('banda', 'median_green'))
var mS2CaatRed = imgColtile.filter(ee.Filter.eq('banda', 'median_red'))
var mS2CaatRGB = mS2CaatBlue.mosaic().addBands(mS2CaatGreen.mosaic()).addBands(mS2CaatRed.mosaic())
// Map.addLayer(mS2CaatRGB, visImg, 'mos')



Map.addLayer(mS2CaatRGB, visImg, 'mos')


var pathMB = "projects/mapbiomas-workspace/public/collection5/mapbiomas_collection50_integration_v1"

var imgClass = ee.Image(pathMB).select("classification_2019")  
imgClass = imgClass.eq(33) // classe de agua com pixels = 1 o resto = 0
imgClass = imgClass//.clip(geomet)
// selecionando uam borda maior do espelho de agua 
imgClass = imgClass.focal_max(3,'square')//.focal_min(1, 'square')


Map.addLayer(imgClass, {min:0 , max: 1}, "MaskWater") 
Map.addLayer(imgClass.eq(0), {min:0 , max: 1}, "NotWater") 