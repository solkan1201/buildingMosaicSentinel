var palettes = require('users/gena/packages:palettes');
var paletteVeg = palettes.cmocean.Speed[7];  
var paletteSoil = palettes.crameri.lajolla[25]; 
var paletteWater = palettes.colorbrewer.Blues[5]; 

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
 
var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);
print(mosaicS2);
mS2Caat = mS2Caat.merge(mosaicS2);
print(mosaicS2);