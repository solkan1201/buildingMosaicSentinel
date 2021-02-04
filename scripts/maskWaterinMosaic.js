

var visImg = {
    bands: ["median_red","median_green","median_blue"],
    max: 2000,
    min: 200
};
var visVeg = {
    min: 10148, 
    max: 12700,
    palette: paletteVeg
};
var visSoil = {
    min: 12345, 
    max: 17760,
    palette: paletteSoil
};
var visWater = {
    min: 12839, 
    max: 18000,
    palette: paletteWater
};


var orb = 52;  // 138, 138
var tile = "24LVM";  //"23LQJ", "23LRK"
var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);
print(mosaicS2);
mS2Caat = mS2Caat.merge(mosaicS2);
print(mosaicS2);

var mS2CaatBlue = mS2Caat.filter(ee.Filter.eq('banda', 'median_blue'))
var mS2CaatGreen = mS2Caat.filter(ee.Filter.eq('banda', 'median_green'))
var mS2CaatRed = mS2Caat.filter(ee.Filter.eq('banda', 'median_red'))
var mS2CaatRGB = mS2CaatBlue.mosaic().addBands(mS2CaatGreen.mosaic()).addBands(mS2CaatRed.mosaic())
Map.addLayer(mS2CaatRGB, visImg, 'mos')

var gradeS2 = ee.FeatureCollection(
            'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat')
            .filterBounds(geometry)


print(gradeS2)