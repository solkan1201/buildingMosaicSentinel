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
var agregateBandsIndexNDVI= function(img){
    
        var ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
                        .add(1).multiply(10000).rename(['ndvi_n'])       
    
        return img.addBands(ndviImg)
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
var yearfin = 2013
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
var MosaicTFin = Mosaicos.filter(ee.Filter.eq('year', yearfin)).mosaic().clip(geomLimit)

var indice1 = lisBND[16]
var indice2 = lisBND[17]


Map.addLayer(MosaicTIni, param.visMosaic, "Mosc" + yearini.toString())
Map.addLayer(MosaicTIni.select(indice1), {min: 0, max: 200, palette: paletteVeg}, "EVI");
Map.addLayer(MosaicTIni.select(indice2), {min: 0, max: 200, palette: paletteVeg}, "NDFI");





var options = {
    title: 'NDVI',
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
    0: {color: 'blue'}
    }
};

// Make the histogram, set the options.
var histNDVI= ui.Chart.image.histogram(MosaicTIni.select(["median_evi2"]), img.geometry(), 100)
    .setSeriesNames(['NDVI'])
    .setOptions(options);

// Display the histogram.
print(histNDVI);





Map.addLayer(MosaicTFin, param.visMosaic, "Mosc" + yearfin.toString())
Map.addLayer(MosaicTFin.select(indice1), {min: 0, max: 200, palette: paletteVeg}, "GCVI");
