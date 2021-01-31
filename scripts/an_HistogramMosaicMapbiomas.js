
var agregateBandsIndexGCVI = function(img){
        
    var gcviImgA = img.expression(
                    "float(b('median_nir')) / (b('median_green')) - 1")
                    .divide(10).add(1).multiply(1000)
                    .rename(['c_median_gcvi'])        
    
    return img.addBands(gcviImgA)
}
var agregateBandsIndexOSAVI = function(img){

    var osaviImg = img.expression(
        "float(b('median_nir') - b('median_red')) / (0.16 + b('median_nir') + b('median_red'))")
            .divide(10).add(1).multiply(1000)
            .rename(['c_median_savi'])        
    
    return img.addBands(osaviImg)
}
var agregateBandsIndexSoil = function(img){
    
    var soilImg = img.expression(
        "float(b('median_nir') - b('median_green')) / (b('median_nir') + b('median_green'))").add(1).multiply(1000)
            .rename(['c_median_isoil'])       
    
    return img.addBands(soilImg)    
}
var agregateBandsgetFractions = function(img){
    
    var bandas = ['median_blue','median_green','median_red','median_nir','median_swir1','median_swir2']  
    var bandsFraction = ['c_median_gv','c_median_npv','c_median_soil','c_median_cloud', 'c_median_shade']
    // Define endmembers
    var endmembers =  [
            [ 119.0,  475.0,  169.0, 6250.0, 2399.0,  675.0], //*gv*/
            [1514.0, 1597.0, 1421.0, 3053.0, 7707.0, 1975.0], //*npv*/
            [1799.0, 2479.0, 3158.0, 5437.0, 7707.0, 6646.0], //*soil*/
            [4031.0, 8714.0, 7900.0, 8989.0, 7002.0, 6607.0], //*cloud*/
            [   0.0,    0.0,    0.0,    0.0,    0.0,    0.0]  //*Shade*/
        ]
    //# Uminxing data
    var fractions = ee.Image(img).select(bandas).unmix(endmembers).float().multiply(10000)
    
    fractions = fractions.select([0,1,2,3,4], self.options['bandsFraction'])        
    
    return img.addBands(fractions)
}
var agregateBandsIndexNDVI= function(img){
    
        var ndviImg = img.expression("float(b('median_nir') - b('median_red')) / (b('median_nir') + b('median_red'))")
                        .add(1).multiply(10000).rename(['c_median_ndvi'])       
    
        return img.addBands(ndviImg)
}
var agregateBandsIndexEVI = function(img){
        
    var eviImg = img.expression(
        "float(2.4 * (b('median_nir') - b('median_red')) / (1 + b('median_nir') + b('median_red')))")
            .divide(10).add(1).multiply(10000)
            .rename(['c_median_evi2'])     
    
    return img.addBands(eviImg)
}
var agregateBandsIndexWater= function(img){
    
        var ndwiImg = img.expression("float(b('median_nir') - b('median_swir2')) / (b('median_nir') + b('median_swir2'))")
                        .add(1).multiply(10000).rename(['c_median_ndwi'])       
    
        return img.addBands(ndviImg)
}


var dictInd = {
    "median_ndvi":'ndvi',
    "median_ndwi":'ndwi',
    "median_gcvi":'gcvi',
    "median_evi2":'evi2',
    'meadian_savi':'savi',
    "median_gv":'gv',
    "median_npv":'npv',
    'median_ratio': 'ratio'
    
};

//print(class4)
var palettesMapBiomas = require('users/mapbiomas/modules:Palettes.js');
var pal = palettesMapBiomas.get('classification2');
var palettes = require('users/gena/packages:palettes');
var paletteVeg = palettes.cmocean.Speed[7];  
var paletteSoil = palettes.crameri.lajolla[25]; 
var paletteWater = palettes.colorbrewer.Blues[5];  

var param = { 
    visclass2: {
            "min": 0, 
            "max": 34,
            "palette":  pal,
            "format": "png"
    },
    visMosaic: {
        min: 0,
        max: 2000,
        bands: ['median_red', 'median_green', 'median_blue']
    },
    visVeg:  {
        min: 10148, 
        max: 12700,
        palette: paletteVeg
    },
    visSoil: {
        min: 12345, 
        max: 17760,
        palette: paletteSoil
    },
    visWater: {
        min: 12839, 
        max: 18000,
        palette: paletteWater
    }

};

var orbNo = '95';
var tile = '23LQC';

var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);

mS2Caat = mS2Caat.merge(mosaicS2).filter(ee.Filter.and(
                                                    ee.Filter.eq('MGRS_TILE', tile),
                                                    ee.Filter.eq('SENSING_ORBIT_NUMBER', orbNo)
                                                ));
print("image collections com as bandas do tile ", mS2Caat);
var lsbandNames =  [
            'blue', 'green', 'red', 'nir', 'swir1', 'siwr2', // 0,1,2,3,4,5
            'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', // 6,7,8,9,10,11,12
            'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', //13,14,15,16,17,18,19
            'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', //20,21,22,23,24,25,
            'soil', 'ndfia', 'contrast'   // 26,27,28
        ];
var indcal = lsbandNames[9];

var MosaicTIni = ee.Image().toUint16();
var newLsBands = [];
lsbandNames.forEach(function(nameBand){
    
    var newNames = 'median_' + nameBand;
    newLsBands.push(newNames);
    print("filter by band == " + newNames);
    //exportanto os dois pares
    var imgtemp = mS2Caat.filter(ee.Filter.eq('banda', newNames)).mosaic();
    // print(imgtemp)
    MosaicTIni = MosaicTIni.addBands(imgtemp);
    
})
print("lista de bandas", newLsBands);
MosaicTIni = MosaicTIni.select(newLsBands);
print('imagem formada ', MosaicTIni);



switch(indcal) {
    case 'ndvi':
        print('ndvi')
        MosaicTIni = agregateBandsIndexNDVI(MosaicTIni)
        
        break;
    case 'ndwi':
        print('ndwi')
        MosaicTIni = agregateBandsIndexWater(MosaicTIni)
        
        break;
    case 'gcvi':
        print('gcvi')
        MosaicTIni = agregateBandsIndexGCVI(MosaicTIni)
        
        break;
    case 'evi2':
        print('evi2')
        MosaicTIni = agregateBandsIndexEVI(MosaicTIni)
        
        break;
    case 'gv':
        print('gv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)
        
        break;
    case 'npv':
        print('npv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)
        
        break;
    case 'savi':
        print('savi')
        MosaicTIni = agregateBandsIndexOSAVI(MosaicTIni)
        
        break;
    default:
        print(" CALCULANDO NINHUM  INDICE ")
} 


Map.addLayer(MosaicTIni, param.visMosaic, "Mosc" )
Map.addLayer(MosaicTIni.select(indcal), {min: 0, max: 200, palette: paletteVeg}, indcal);
Map.addLayer(MosaicTIni.select('c' + indcal), {min: 0, max: 200, palette: paletteVeg}, 'c' + indcal);



// var options = {
//     title: indcal + " para todo o ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'blue'}
//     }
// };
// // Make the histogram, set the options.
// var histIndice1= ui.Chart.image.histogram(MosaicTIni.select(indice1), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice1);

// options = {
//     title: indcal + " do periodo seco do ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'blue'}
//     }
// };
// // Make the histogram, set the options.
// var histIndice2 = ui.Chart.image.histogram(MosaicTIni.select(indice2), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice2);

// options = {
//     title: indcal + "do periodo chuvos o ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'blue'}
//     }
// };
// // Make the histogram, set the options.
// var histIndice3 = ui.Chart.image.histogram(MosaicTIni.select(indice3), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice3);


// Map.addLayer(MosaicTIni.select('c_' + indice1), {min: 9500, max: 11500, palette: paletteVeg}, 'calc_' + indice1);
// Map.addLayer(MosaicTIni.select('c_' + indice2), {min: 9500, max: 11500, palette: paletteVeg},'calc_' + indice2);
// Map.addLayer(MosaicTIni.select('c_' + indice3), {min: 9500, max: 11500, palette: paletteVeg}, 'calc_' + indice3);


// options = {
//     title: indcal + " CALCULADO para todo o ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'red'}
//     }
// };
// print('c_' + indice1)
// // Make the histogram, set the options.
// var histIndice4= ui.Chart.image.histogram(MosaicTIni.select('c_' + indice1), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice4);

// options = {
//     title: indcal + " CALCULADO do periodo seco do ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'red'}
//     }
// };
// print('c_' + indice2)
// // Make the histogram, set the options.
// var histIndice5 = ui.Chart.image.histogram(MosaicTIni.select('c_' + indice2), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice5);

// options = {
//     title: indcal + "CALCULADO do periodo chuvos o ano " + yearini.toString(),
//     fontSize: 20,
//     hAxis: {title: 'DN'},
//     vAxis: {title: 'count of DN'},
//     series: {
//     0: {color: 'red'}
//     }
// };
// print('c_' + indice3)
// // Make the histogram, set the options.
// var histIndice6 = ui.Chart.image.histogram(MosaicTIni.select('c_' + indice3), geomLimit, 100)
//                             .setSeriesNames(['NDVI'])
//                             .setOptions(options);

// // Display the histogram.
// print(histIndice6);