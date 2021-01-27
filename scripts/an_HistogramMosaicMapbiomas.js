var lisBND = {
    '0':"amp_evi2",
    '1':"amp_gv",
    '2':"amp_ndfi",
    '3':"amp_ndvi", 
    '4':"amp_ndwi", 
    '5':"amp_npv",
    '6':"amp_sefi", 
    '7':"amp_soil", 
    '8':"amp_wefi", 
    '9':"median_blue", 
    '10':"median_blue_dry",
    '11':"median_blue_wet", 
    '12':"median_cai",
    '13':"median_cai_dry", 
    '14':"median_cai_wet",
    '15':"median_cloud", 
    '16':"median_evi2", 
    '17':"median_evi2_dry", 
    '18':"median_evi2_wet",
    '19':"median_fns", 
    '20':"median_fns_dry", 
    '21':"median_fns_wet", 
    '22':"median_gcvi",
    '23':"median_gcvi_dry",
    '24':"median_gcvi_wet", 
    '25':"median_green",
    '26':"median_green_dry",
    '27':"median_green_wet", 
    '28':"median_gv",
    '29':"median_gvs",
    '30':"median_gvs_dry",
    '31':"median_gvs_wet",
    '32':"median_hallcover",
    '33':"median_ndfi", 
    '34':"median_ndfi_dry", 
    '35':"median_ndfi_wet",
    '36':"median_ndvi",
    '37':"median_ndvi_dry",
    '38':"median_ndvi_wet",
    '39':"median_ndwi",
    '40':"median_ndwi_dry",
    '41':"median_ndwi_wet",
    '42':"median_nir",
    '43':"median_nir_dry",
    '44':"median_nir_wet",
    '45':"median_npv",
    '46':"median_pri",
    '47':"median_pri_dry",
    '48':"median_pri_wet",
    '49':"median_red",
    '50':"median_red_dry",
    '51':"median_red_wet",
    '52':"median_savi",
    '53':"median_savi_dry",
    '54':"median_savi_wet",
    '55':"median_sefi",
    '56':"median_sefi_dry",
    '57':"median_sefi_wet", 
    '58':"median_shade",
    '59':"median_soil", 
    '60':"median_swir1",
    '61':"median_swir1_dry",
    '62':"median_swir1_wet",
    '63':"median_swir2",
    '64':"median_swir2_dry",
    '65':"median_swir2_wet",
    '66':"median_temp",
    '67':"median_wefi",
    '68':"median_wefi_dry",
    '69':"median_wefi_wet",
    '70':"min_blue",
    '71':"min_green",
    '72':"min_nir",
    '73':"min_red",
    '74':"min_swir1",
    '75':"min_swir2",
    '76':"min_temp",
    '77':"stdDev_blue",
    '78':"stdDev_cai",
    '79':"stdDev_cloud",
    '80':"stdDev_evi2",
    '81':"stdDev_fns",
    '82':"stdDev_gcvi",
    '83':"stdDev_green",
    '84':"stdDev_gv",
    '85':"stdDev_gvs",
    '86':"stdDev_hallcover",
    '87':"stdDev_ndfi", 
    '88':"stdDev_ndvi",
    '89':"stdDev_ndwi",
    '90':"stdDev_nir",
    '91':"stdDev_npv",
    '92':"stdDev_pri",
    '93':"stdDev_red",
    '94':"stdDev_savi",
    '95':"stdDev_sefi",  
    '96':"stdDev_shade",
    '97':"stdDev_soil", 
    '98':"stdDev_swir1",
    '99':"stdDev_swir2",
    '100':"stdDev_temp",
    '101':"stdDev_wefi"
}
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
var agregateBandsIndexGCVI_dry = function(img){
        
    var gcviImgA = img.expression(
            "float(b('median_nir_dry')) / (b('median_green_dry')) - 1")
            .divide(10).add(1).multiply(1000)
            .rename(['c_median_gcvi_dry'])        
    
    return img.addBands(gcviImgA)
}
var agregateBandsIndexOSAVI_dry = function(img){

    var osaviImg = img.expression(
        "float(b('median_nir_dry') - b('median_red_dry')) / (0.16 + b('median_nir_dry') + b('median_red_dry'))")
            .divide(10).add(1).multiply(10000)
            .rename(['c_median_savi_dry'])        
    
    return img.addBands(osaviImg)
}
var agregateBandsIndexSoil_dry = function(img){
    
    var soilImg = img.expression(
        "float(b('median_nir_dry') - b('median_green_dry')) / (b('median_nir_dry') + b('median_green_dry'))")
            .rename(['c_median_isoil_dry'])       
    
    return img.addBands(soilImg)    
}
var agregateBandsgetFractions_dry = function(img){
    
    var bandas = ['median_blue_dry','median_green_dry','median_red_dry','median_nir_dry','median_swir1_dry','median_swir2_dry']  
    var bandsFraction = ['c_median_gv_dry','c_median_npv_dry','c_median_soil_dry','c_median_cloud_dry', 'c_median_shade_dry']
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
var agregateBandsIndexNDVI_dry= function(img){
    
        var ndviImg = img.expression("float(b('median_nir_dry') - b('median_red_dry')) / (b('median_nir_dry') + b('median_red_dry'))")
                        .add(1).multiply(10000).rename(['c_median_ndvi_dry'])       
    
        return img.addBands(ndviImg)
}
var agregateBandsIndexEVI_dry = function(img){
        
    var eviImg = img.expression(
            "float(2.4 * (b('median_nir_dry') - b('median_red_dry')) / (1 + b('median_nir_dry') + b('median_red_dry')))")
            .divide(10).add(1).multiply(10000)
            .rename(['c_median_evi2_dry'])     
    
    return img.addBands(eviImg)
}
var agregateBandsIndexWater_dry = function(img){
    
        var ndwiImg = img.expression("float(b('median_nir_dry') - b('median_swir2_dry')) / (b('median_nir_dry') + b('median_swir2_dry'))")
                        .add(1).multiply(10000).rename(['c_median_ndwi_dry'])       
    
        return img.addBands(ndviImg)
}
var agregateBandsIndexGCVI_wet = function(img){
        
    var gcviImgA = img.expression(
        "float(b('median_nir_wet')) / (b('median_green_wet')) - 1")
            .divide(10).add(1).multiply(1000)
            .rename(['c_median_gcvi_wet'])        
    
    return img.addBands(gcviImgA)
}
var agregateBandsIndexOSAVI_wet = function(img){

    var osaviImg = img.expression(
        "float(b('median_nir_wet') - b('median_red_wet')) / (0.16 + b('median_nir_wet') + b('median_red_wet'))")
            .divide(10).add(1).multiply(1000)
            .rename(['c_median_savi_wet'])        
    
    return img.addBands(osaviImg)
}
var agregateBandsIndexSoil_wet = function(img){
    
    var soilImg = img.expression(
        "float(b('median_nir_wet') - b('median_green_wet')) / (b('median_nir_wet') + b('median_green_wet'))").add(1).multiply(1000)
            .rename(['c_median_isoil_wet'])       
    
    return img.addBands(soilImg)    
}
var agregateBandsgetFractions_wet = function(img){
    
    var bandas = ['median_blue_wet','median_green_wet','median_red_wet','median_nir_wet','median_swir1_wet','median_swir2_wet']  
    var bandsFraction = ['c_median_gv_wet','c_median_npv_wet','c_median_soil_wet','c_median_cloud_wet', 'c_median_shade_wet']
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
    
    fractions = fractions.select([0,1,2,3,4], bandsFraction)        
    
    return img.addBands(fractions)
}
var agregateBandsIndexNDVI_wet = function(img){
    
        var ndviImg = img.expression("float(b('median_nir_wet') - b('median_red_wet')) / (b('median_nir_wet') + b('median_red_wet'))")
                        .add(1).multiply(10000).rename(['c_median_ndvi_wet'])       
    
        return img.addBands(ndviImg)
}
var agregateBandsIndexEVI_wet = function(img){
        
    var eviImg = img.expression(
        "float(2.4 * (b('median_nir_wet') - b('median_red_wet')) / (1 + b('median_nir_wet') + b('median_red_wet')))")
            .divide(10).add(1).multiply(10000)
            .rename(['c_median_evi2_wet'])     
    
    return img.addBands(eviImg)
}
var agregateBandsIndexWater_wet = function(img){
    
        var ndwiImg = img.expression("float(b('median_nir_wet') - b('median_swir2_wet')) / (b('median_nir_wet') + b('median_swir2_wet'))")
                        .add(1).multiply(10000).rename(['c_median_ndwi_wet'])       
    
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
}

//print(class4)
var palettesMapBiomas = require('users/mapbiomas/modules:Palettes.js');
var pal = palettesMapBiomas.get('classification2');
var palettes = require('users/gena/packages:palettes');
var paletteVeg = palettes.cmocean.Speed[7];  
var paletteSoil = palettes.crameri.lajolla[25]; 
var paletteWater = palettes.colorbrewer.Blues[5];  

var param = { 
    assetMapB4: 'projects/mapbiomas-workspace/public/collection4_1/mapbiomas_collection41_integration_v1',
    assetMapB5_1: 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/classificacoes/classesV5',
    assetCol5Final : "projects/mapbiomas-workspace/public/collection5/mapbiomas_collection50_integration_v1",
    assetMapB5_v11: 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/classificacoes/classesV7_filter/CA_col5_v7_5055',
    assetBacia: "users/nerivaldogeo/bacias_caatinga_f",
    assetMosaic: 'projects/mapbiomas-workspace/MOSAICOS/workspace-c3',   
    classMapB: [3, 4, 5, 9,12,13,15,18,19,20,21,22,23,24,25,26,29,30,31,32,33],
    classNew: [3, 4, 3, 3,12,12,21,21,21,21,21,22,22,22,22,33,29,22,33,12,33],
    anos: ['1985','1986','1987','1988','1989','1990','1991','1992','1993','1994',
            '1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
            '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014',
            '2015','2016','2017','2018','2019'],
    bandas: ['median_red', 'median_green', 'median_blue'],
    //'743','732','747',
    listaNameBacias: [
            '741','742','744', '745','746','749','751','752','753', '754',
            '755','756','757','758','759','76111','76116','7612','7613',
            '7614','7615','7616', '7617','7618','7619','762','763','764','765',
            '766','767','771','772','773', '774', '775','776','777','778'
    ],
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

}
var lsIdImg = [
    '20200809T131249_20200809T131246_T23MQP',
    '20200814T131251_20200814T131249_T23KNB',
    '20201015T130249_20201015T130251_T24LVR'
    ]

var img =ee.Image('COPERNICUS/S2_SR/' + lsIdImg[2])
                    .select(['B2', 'B3', 'B4', 'B8', 'B11', 'B12'])
                    //.divide(10000)
var geomLimit = img.geometry()                    
var yearini = 2005
var indice1 = lisBND[16]
var indice2 = lisBND[17]
var indice3 = lisBND[18]
var indcal = dictInd[indice1]

// var yearfin = 2013
var FeatColbacia = ee.FeatureCollection('users/CartasSol/shapes/nCaatingaBff3000').geometry();
var Mosaicos = ee.ImageCollection(param.assetMosaic).filter(
                                        ee.Filter.or(
                                            ee.Filter.eq("biome", 'CAATINGA'),
                                            ee.Filter.eq("biome", 'CERRADO'),
                                            ee.Filter.eq("biome", 'MATAATLANTICA')
                                        ))
                                        .filterBounds(FeatColbacia)//.select(param.bandas);

print(Mosaicos.first())
var MosaicTIni = Mosaicos.filter(ee.Filter.eq('year', yearini)).mosaic().clip(geomLimit)
// var MosaicTFin = Mosaicos.filter(ee.Filter.eq('year', yearfin)).mosaic().clip(geomLimit)

switch(indcal) {
    case 'ndvi':
        print('ndvi')
        MosaicTIni = agregateBandsIndexNDVI(MosaicTIni)
        MosaicTIni = agregateBandsIndexNDVI_dry(MosaicTIni)
        MosaicTIni = agregateBandsIndexNDVI_wet(MosaicTIni)
        break;
    case 'ndwi':
        print('ndwi')
        MosaicTIni = agregateBandsIndexWater(MosaicTIni)
        MosaicTIni = agregateBandsIndexWater_dry(MosaicTIni)
        MosaicTIni = agregateBandsIndexWater_wet(MosaicTIni)
        break;
    case 'gcvi':
        print('gcvi')
        MosaicTIni = agregateBandsIndexGCVI(MosaicTIni)
        MosaicTIni = agregateBandsIndexGCVI_dry(MosaicTIni)
        MosaicTIni = agregateBandsIndexGCVI_wet(MosaicTIni)
        break;
    case 'evi2':
        print('evi2')
        MosaicTIni = agregateBandsIndexEVI(MosaicTIni)
        MosaicTIni = agregateBandsIndexEVI_dry(MosaicTIni)
        MosaicTIni = agregateBandsIndexEVI_wet(MosaicTIni)
        break;
    case 'gv':
        print('gv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)
        MosaicTIni = agregateBandsgetFractions_dry(MosaicTIni)
        MosaicTIni = agregateBandsgetFractions_wet(MosaicTIni)
        break;
    case 'npv':
        print('npv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)
        MosaicTIni = agregateBandsgetFractions_dry(MosaicTIni)
        MosaicTIni = agregateBandsgetFractions_wet(MosaicTIni)
        break;
    case 'savi':
        print('savi')
        MosaicTIni = agregateBandsIndexOSAVI(MosaicTIni)
        MosaicTIni = agregateBandsIndexOSAVI_dry(MosaicTIni)
        MosaicTIni = agregateBandsIndexOSAVI_wet(MosaicTIni)
        break;
    default:
        print(" CALCULANDO NINHUM  INDICE ")
} 


Map.addLayer(MosaicTIni, param.visMosaic, "Mosc" + yearini.toString())
Map.addLayer(MosaicTIni.select(indice1), {min: 0, max: 200, palette: paletteVeg}, indice1);
Map.addLayer(MosaicTIni.select(indice2), {min: 0, max: 200, palette: paletteVeg}, indice2);
Map.addLayer(MosaicTIni.select(indice3), {min: 0, max: 200, palette: paletteVeg}, indice3);


var options = {
    title: indcal + " para todo o ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'blue'}
    }
};
// Make the histogram, set the options.
var histIndice1= ui.Chart.image.histogram(MosaicTIni.select(indice1), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice1);

options = {
    title: indcal + " do periodo seco do ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'blue'}
    }
};
// Make the histogram, set the options.
var histIndice2 = ui.Chart.image.histogram(MosaicTIni.select(indice2), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice2);

options = {
    title: indcal + "do periodo chuvos o ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'blue'}
    }
};
// Make the histogram, set the options.
var histIndice3 = ui.Chart.image.histogram(MosaicTIni.select(indice3), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice3);


Map.addLayer(MosaicTIni.select('c_' + indice1), {min: 9500, max: 11500, palette: paletteVeg}, 'calc_' + indice1);
Map.addLayer(MosaicTIni.select('c_' + indice2), {min: 9500, max: 11500, palette: paletteVeg},'calc_' + indice2);
Map.addLayer(MosaicTIni.select('c_' + indice3), {min: 9500, max: 11500, palette: paletteVeg}, 'calc_' + indice3);


options = {
    title: indcal + " CALCULADO para todo o ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'red'}
    }
};
print('c_' + indice1)
// Make the histogram, set the options.
var histIndice4= ui.Chart.image.histogram(MosaicTIni.select('c_' + indice1), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice4);

options = {
    title: indcal + " CALCULADO do periodo seco do ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'red'}
    }
};
print('c_' + indice2)
// Make the histogram, set the options.
var histIndice5 = ui.Chart.image.histogram(MosaicTIni.select('c_' + indice2), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice5);

options = {
    title: indcal + "CALCULADO do periodo chuvos o ano " + yearini.toString(),
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'red'}
    }
};
print('c_' + indice3)
// Make the histogram, set the options.
var histIndice6 = ui.Chart.image.histogram(MosaicTIni.select('c_' + indice3), geomLimit, 100)
                            .setSeriesNames(['NDVI'])
                            .setOptions(options);

// Display the histogram.
print(histIndice6);