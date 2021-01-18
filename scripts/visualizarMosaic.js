
var palettes = require('users/gena/packages:palettes');
var paletteVeg = palettes.cmocean.Speed[7];  
var paletteSoil = palettes.crameri.lajolla[25]; 
var paletteWater = palettes.colorbrewer.Blues[5];  

var visImg = {
    bands: ["median_red","median_green","median_blue"],
    max: 2000,
    min: 200
}
var visVeg = {
    min: 10148, 
    max: 12700,
    palette: paletteVeg
}
var visSoil = {
    min: 12345, 
    max: 17760,
    palette: paletteSoil
}
var visWater = {
    min: 12839, 
    max: 18000,
    palette: paletteWater
}

var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2'
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics'
var mosaicS2 = ee.ImageCollection(pathMosaic)
var mS2Caat = ee.ImageCollection(pathMosaicMB)
print(mosaicS2)
mS2Caat = mS2Caat.merge(mosaicS2)
print(mosaicS2)
// // var lsBands = mosaicS2.filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', '38'))
// //                       .filter(ee.Filter.eq('MGRS_TILE', '23LNJ'))
// //                       .filter(ee.Filter.eq('year', 2020))
// // print(lsBands)
// // var nameBands 
// var lsbandNames = lsBands.reduceColumns(ee.Reducer.toList(), ['banda']).get('list')
// lsbandNames = ee.List(lsbandNames).distinct().getInfo()

var lsbandNames = [
    'median_blue','median_evi','median_green','median_nir','median_ratio',
    'median_red','median_rvi','median_siwr2','median_swir1'
]


print(lsbandNames)
var img1 = ee.Image().toUint16()
lsbandNames.forEach(function(nameBand){
    // print(nameBand)
    var imgtemp = mS2Caat.filter(ee.Filter.eq('banda', nameBand)).mosaic()
    // print(imgtemp)
    img1 = img1.addBands(imgtemp)
    
})
img1 = img1.select(lsbandNames)
print('imagem formada ', img1)


Map.addLayer(img1, visImg, "img");
Map.addLayer(img1.select("median_evi"), {min: 9951, max: 10600, palette: paletteVeg}, "EVI");
Map.addLayer(img1.select("median_rvi"), {min: 60, max: 2000, palette: paletteVeg}, "RVI");
Map.addLayer(img1.select("median_ratio"), {min: 400, max: 15000, palette: paletteVeg}, "RATIO");
// Map.addLayer(img1.select("evi_median"), visVeg, "EVI");
// Map.addLayer(img1.select("ndwi_median"), visWater, "NDWI");