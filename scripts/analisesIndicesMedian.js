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
        "float(b('median_nir') - b('median_green')) / (b('median_nir') + b('median_green'))")
        .add(1).multiply(1000)
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
    var fractions = ee.Image(img).select(bandas).unmix(endmembers).float()//
    
    fractions = fractions.select([0,1,2,3,4], self.options['bandsFraction'])        

    //calculate NDFIa
    var ndfia = img.expression(
        "float(b('gv') - b('soil')) / float( b('gv') + 2 * b('npv') + b('soil'))")        
    ndfia = ndfia.add(1).multiply(10000).rename('ndfia')
    fractions =fractions.multiply(10000)

    return img.addBands(fractions).addBands(ndfia)
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
            .rename(['c_median_evi'])     
    
    return img.addBands(eviImg)
}
var agregateBandsIndexWater= function(img){
    
        var ndwiImg = img.expression("float(b('median_nir') - b('median_swir2')) / (b('median_nir') + b('median_swir2'))")
                        .add(1).multiply(10000).rename(['c_median_ndwi'])       
    
        return img.addBands(ndviImg)
}
var agregateBandsIndexBrightness= function(img){

    var tasselledCaprImg = img.expression(
        "float(0.3037 * b('median_blue') + 0.2793 * b('median_green') + 0.4743 * b('median_red')  + 0.5585 * b('median_nir') " +
        "+ 0.5082 * b('median_swir1') +  0.1863 * b('median_swir2'))")
        .multiply(10000).rename(['c_median_brightness']) 
    
    return img.addBands(tasselledCaprImg)
}

var agregateBandsIndexGVMI = function(img){
        
    var gvmiImg = img.expression(
        "float ((b('median_nir')  + 0.1) -(b('median_swir1') + 0.02)) / ((b('median_nir') + 0.1) + (b('median_swir1') + 0.02))") 
        .add(1).multiply(10000).rename(['c_median_gvmi'])     
    
    return img.addBands(gvmiImg)
}

var agregateBandsIndexsPRI = function(img){
        
    var priImg = img.expression(
        "float((b('median_green') - b('median_blue')) / (b('median_green') + b('median_blue')))")
            .rename(['pri'])   
    var spriImg =   priImg.expression(
        "float((b('pri') + 1) / 2)").multiply(10000).rename(['c_median_spri'])  
    
    return img.addBands(spriImg)
}

var agregateBandsIndexMSI= function(img){

    var msiImg = img.expression(
        "float( b('median_nir') / b('median_swir1'))").multiply(1000)
        .rename(['c_median_msi']) 
    
    return img.addBands(msiImg)
}

var agregateBandsIndexwetness= function(img){

    var tasselledCapImg = img.expression(
        "float(0.1509 * b('median_blue') + 0.1973 * b('median_green') + 0.3279 * b('median_red') " +
        " + 0.3406 * b('median_nir') + 0.7112 * b('median_swir1') +  0.4572 * b('median_swir2'))")
        .multiply(10000).rename(['c_median_wetness']) 
    
    return img.addBands(tasselledCapImg)
}

var agregateBandsIndexCVI= function(img){

    var cviImgA = img.expression(
        "float(b('median_nir') * (b('median_red') / (b('median_blue') * b('median_blue'))))")
        .multiply(100).rename(['c_median_cvi'])        
    
    return img.addBands(cviImgA)
}

var agregateBandsIndexLAI= function(img){

    var eviImg = img.expression(
        "float(2.4 * (b('median_nir') - b('median_red')) / (1 + b('median_nir') + b('median_red')))")        
        rename('evi')

    var laiImg = eviImg.expression(
        "(3.618 * float(b('evi') - 0.118))").divide(10).add(1).multiply(1000)
        .rename(['c_median_lai'])     

    return img.addBands(laiImg)
}

var IndiceIndicadorAgua= function(img){

    var iia = img.expression(
            "float((b('median_green') - 4 *  b('median_nir')) / (b('median_green') + 4 *  b('median_nir')))"
    ).add(1).multiply(10000).rename("c_median_iia")
    
    return img.addBands(iia)
}

var AutomatedWaterExtractionIndex= function(img){

    var awei = img.expression(
                        "float(4 * (b('median_blue') - b('median_swir2')) - (0.25 * b('median_nir') + 2.75 * b('median_swir1')))"
                    ).add(5).multiply(10000).rename("c_median_awei")          
    
    return img.addBands(awei)
}

var agregateBandsIndexRVI= function(img){

    var rviImg = img.expression("float(b('median_red') / b('median_nir'))")
                        .multiply(1000).rename(['c_median_rvi'])       

    return img.addBands(rviImg)

}

var agregateBandsIndexRATIO = function(img){
    
    var ratioImg = img.expression("float(b('median_nir') / b('median_red'))")
                    .multiply(1000).rename(['c_median_ratio'])      

    return img.addBands(ratioImg)
}
var agregateBandsTexturasGLCM = function(img){
        
    var img2 = img.toInt()                
    var textura2 = img2.select('median_nir').glcmTexture(3)  
    var contrast = textura2.select('median_nir_contrast').divide(1000).rename('contrast') 

    return  img.addBands(contrast.select('c_median_contrast'))
}  

var agregateBandsIndexCO2Flux = function(img){
        
    var ndviImg = img.expression("float(b('median_nir') - b('median_swir2')) / (b('median_nir') + b('median_swir2'))").rename(['ndvi']) 

    var priImg = img.expression(
                            "float((b('median_green') - b('median_blue')) / (b('median_green') + b('median_blue')))"
                        ).rename(['pri'])   
    var spriImg =   priImg.expression(
                            "float((b('pri') + 1) / 2)").rename(['spri'])

    var co2FluxImg = ndviImg.multiply(spriImg).add(2).multiply(10000)
                            .rename(['c_median_co2flux'])   

    return img.addBands(co2FluxImg)
    //return co2FluxImg
}

// var dictInd = {
//     "median_ndvi":'ndvi',
//     "median_ndwi":'ndwi',
//     "median_gcvi":'gcvi',
//     "median_evi2":'evi2',
//     'meadian_savi':'savi',
//     "median_gv":'gv',
//     "median_npv":'npv',
//     'median_ratio': 'ratio'
    
// };

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

//##########################################################################//
//########### parametros a serem modificados ###############################//
//##########################################################################//

var lsbandNames =  [
    'blue', 'green', 'red', 'nir', 'swir1', 'siwr2', // 0,1,2,3,4,5
    'evi', 'ratio', 'rvi', 'ndvi', 'ndwi', 'awei', 'iia', // 6,7,8,9,10,11,12
    'lai', 'gcvi', 'cvi', 'osavi', 'isoil', 'msi', 'wetness', //13,14,15,16,17,18,19
    'brightness', 'gvmi', 'spri', 'co2flux', 'gv', 'npv', //20,21,22,23,24,25,
    'soil', 'ndfia', 'contrast'   // 26,27,28
];

var numInd = 9;
var indcal = 'median_' + lsbandNames[numInd] ;
var orbNo = '95';
var tile = '23LQC';

var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var pathgradeS2Corr = 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat';

var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);

mS2Caat = mS2Caat.merge(mosaicS2).filter(ee.Filter.and(
                                                    ee.Filter.eq('MGRS_TILE', tile),
                                                    ee.Filter.eq('SENSING_ORBIT_NUMBER', orbNo)
                                                ));
                                                
print("image collections com as bandas do tile ", mS2Caat);

var gradeS2 = ee.FeatureCollection(pathgradeS2Corr).filter(ee.Filter.and(
                                                              ee.Filter.eq('MGRS_TILE', tile),
                                                              ee.Filter.eq('SENSING_ORBIT_NUMBER', parseInt(orbNo))
                                                          )).geometry() 

var MosaicTIni = ee.Image().toUint16();
var newLsBands = [];
lsbandNames.forEach(function(nameBand){
    
    var newNames = 'median_' + nameBand;
    newLsBands.push(newNames);
    // print("filter by band == " + newNames);
    //exportanto os dois pares
    var imgtemp = mS2Caat.filter(ee.Filter.eq('banda', newNames)).mosaic();
    // print(imgtemp)
    MosaicTIni = MosaicTIni.addBands(imgtemp);
    
})
print("lista de bandas", newLsBands);
MosaicTIni = MosaicTIni.select(newLsBands);
// print('imagem formada ', MosaicTIni);

//##########################################################################//
var paletasSelect = paletteVeg;

switch(lsbandNames[numInd]) {
    case 'ndvi':
        print('calculando === ndvi')
        MosaicTIni = agregateBandsIndexNDVI(MosaicTIni) 
        paletasSelect = paletteVeg
        break;
    case 'ndwi':
        print('calculando === ndwi')
        MosaicTIni = agregateBandsIndexWater(MosaicTIni)   
        paletasSelect = paletteWater     
        break;
    case 'gcvi':
        print('calculando === gcvi')
        MosaicTIni = agregateBandsIndexGCVI(MosaicTIni) 
        paletasSelect = paletteVeg       
        break;
    case 'cvi':
        print('calculando === cvi')
        MosaicTIni = agregateBandsIndexCVI(MosaicTIni)  
        paletasSelect = paletteVeg      
        break;
    case 'evi':
        print('calculando === evi')
        MosaicTIni = agregateBandsIndexEVI(MosaicTIni)  
        paletasSelect = paletteVeg      
        break;
    case 'gv':
        print('calculando === gv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)   
        paletasSelect = paletteVeg     
        break;
    case 'npv':
        print('calculando === npv')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni) 
        paletasSelect = paletteVeg       
        break;
    case 'soil':
        print('calculando === soil')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni)    
        paletasSelect = paletteSoil    
        break;
    case 'ndfia':
        print('calculando === ndfia')
        MosaicTIni = agregateBandsgetFractions(MosaicTIni) 
        paletasSelect = paletteVeg       
        break;
    case 'savi':
        print('calculando ===  savi')
        MosaicTIni = agregateBandsIndexOSAVI(MosaicTIni)   
        paletasSelect = paletteVeg     
        break;
    case 'ratio':
        print('calculando ===  ratio')
        MosaicTIni = agregateBandsIndexRATIO(MosaicTIni) 
        paletasSelect = paletteVeg       
        break;
    case 'rvi':
        print('calculando ===  rvi')
        MosaicTIni = agregateBandsIndexRVI(MosaicTIni)   
        paletasSelect = paletteVeg     
        break;
    case 'iia':
        print('calculando ===  iia')
        MosaicTIni = IndiceIndicadorAgua(MosaicTIni)  
        paletasSelect = paletteWater      
        break;
    case 'awei':
        print('calculando ===  awei')
        MosaicTIni = AutomatedWaterExtractionIndex(MosaicTIni)  
        paletasSelect = paletteWater      
        break;
    case 'lai':
        print('calculando ===  lai')
        MosaicTIni = agregateBandsIndexLAI(MosaicTIni) 
        paletasSelect = paletteVeg       
        break;
    case 'isoil':
        print('calculando ===  isoil')
        MosaicTIni = agregateBandsIndexSoil(MosaicTIni)  
        paletasSelect = paletteSoil       
        break;
    case 'wetness':
        print('calculando ===  wetness')
        MosaicTIni = agregateBandsIndexwetness(MosaicTIni)  
        paletasSelect = paletteVeg      
        break;
    case 'brightness':
        print('calculando ===  brightness')
        MosaicTIni = agregateBandsIndexBrightness(MosaicTIni)  
        paletasSelect = paletteSoil       
        break;
    case 'gvmi':
        print('calculando ===  gvmi')
        MosaicTIni = agregateBandsIndexGVMI(MosaicTIni)   
        paletasSelect = paletteVeg     
        break;
    case 'msi':
        print('calculando ===  msi')
        MosaicTIni = agregateBandsIndexMSI(MosaicTIni)  
        paletasSelect = paletteVeg       
        break;
    case 'spri':
        print('calculando ===  spri')
        MosaicTIni = agregateBandsIndexsPRI(MosaicTIni)     
        paletasSelect = paletteVeg   
        break;
    case 'co2flux':
        print('calculando ===  co2flux')
        MosaicTIni = agregateBandsIndexCO2Flux(MosaicTIni)   
        paletasSelect = paletteSoil      
        break;
    case 'contrast':
        print('calculando ===  contrast')
        MosaicTIni = agregateBandsTexturasGLCM(MosaicTIni)  
        paletasSelect = paletteSoil       
        break;    
    default:
        print(" CALCULANDO NINHUM  INDICE ")
} 
print("Bandas selecionadas ", MosaicTIni.bandNames())
var meanDictionary = MosaicTIni.select('c_' + indcal)
                                .reduceRegion({
                                    reducer: ee.Reducer.minMax(),
                                    geometry: gradeS2,
                                    scale: 1000,
                                    maxPixels: 1e9
                                });
  
// The result is a Dictionary.  Print it.
print("resultados de minimo e maximo", meanDictionary);  
var maximo = meanDictionary.get('c_' + indcal + "_max");
maximo = ee.Number(maximo).toInt16()
var minimo = meanDictionary.get('c_' + indcal + "_min");
minimo = ee.Number(minimo).toInt16()

print(minimo)
var visIndex = {
    min: minimo.getInfo(), 
    max: maximo.getInfo(), 
    palette: paletasSelect
  }
  


Map.addLayer(MosaicTIni, param.visMosaic, "Mosc" )
Map.addLayer(MosaicTIni.select(indcal), visIndex, indcal);
Map.addLayer(MosaicTIni.select('c_' + indcal), visIndex, 'calc_' + indcal);



print('bandas ', indcal)
var options = {
    title: indcal,
    fontSize: 20,
    hAxis: {title: 'Values of ' + indcal + ' index'},
    vAxis: {title: 'Quantities pixels of ' + indcal},
    series: {
    0: {color: 'blue'},
    1: {color: 'red'}
    }
};
// Make the histogram, set the options.
var histIndice1= ui.Chart.image.histogram(MosaicTIni.select([indcal, 'c_' + indcal]), gradeS2, 100)
                            .setSeriesNames([indcal])
                            .setOptions(options);

// Display the histogram.
print(histIndice1);

