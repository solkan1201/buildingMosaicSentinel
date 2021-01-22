//https://code.earthengine.google.com/f12dd28f16d07524273b3db8d2e1ee85
//https://code.earthengine.google.com/4aabc8ca6fb058f8bb677fb17e2edf23

// var palettes = require('users/gena/packages:palettes');
// var paletteVeg = palettes.cmocean.Speed[7];  
// var paletteSoil = palettes.crameri.lajolla[25]; 
// var paletteWater = palettes.colorbrewer.Blues[5];  

var visImg = {
    bands: ["median_red","median_green","median_blue"],
    max: 2000,
    min: 200
};

var visImgSwir = {
    bands: ["median_swir1","median_nir","median_red"],
    max: 4500,
    min: 80
};


var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);
// print(mosaicS2);
mS2Caat = mS2Caat.merge(mosaicS2);
print(mosaicS2);

var mS2CaatBlue = mS2Caat.filter(ee.Filter.eq('banda', 'median_blue'))
var mS2CaatGreen = mS2Caat.filter(ee.Filter.eq('banda', 'median_green'))
var mS2CaatRed = mS2Caat.filter(ee.Filter.eq('banda', 'median_red'))
var mS2CaatNir = mS2Caat.filter(ee.Filter.eq('banda', 'median_nir'))
var mS2CaatSwir = mS2Caat.filter(ee.Filter.eq('banda', 'median_swir1'))

var mS2CaatRGB = mS2CaatBlue.mosaic().addBands(mS2CaatGreen.mosaic())
                            .addBands(mS2CaatRed.mosaic())
                            .addBands(mS2CaatSwir.mosaic())
                            .addBands(mS2CaatNir.mosaic())
print(mS2CaatRGB)
Map.addLayer(mS2CaatRGB, visImg, 'mos')
Map.addLayer(mS2CaatRGB, visImgSwir, 'mos2')

var gradeS2 = ee.FeatureCollection(
            'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat')
            .filterBounds(geometry)
print(gradeS2)

var reduce = gradeS2.reduceColumns(ee.Reducer.toList(2), ['SENSING_ORBIT_NUMBER', 'MGRS_TILE'] ).get('list')
print("Grades para serem eliminados", reduce)

Map.addLayer(gradeS2, {color: 'blue'}, 'grade')

var gradeS2Other = ee.FeatureCollection(
            'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat')
            .filterBounds(geometry2)
// print(gradeS2)
var reduceOther = gradeS2Other.reduceColumns(ee.Reducer.toList(2), ['SENSING_ORBIT_NUMBER', 'MGRS_TILE'] ).get('list')
print("grades para serem tratados com outra metodologia ", reduceOther)

Map.addLayer(gradeS2Other, {color: 'red'}, 'gradeOther')





