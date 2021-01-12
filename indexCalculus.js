
var agregateBandsIndexGCVI = function(img){
    
    var gcviImgA = img.expression(
        "float(b('B8')) / (b('B3')) - 1")
            .rename(['gcvi'])        
    
    return img.addBands(gcviImgA)
}
var agregateBandsIndexOSAVI = function(img){

    var osaviImg = img.expression(
        "float(b('B8') - b('B4')) / (0.16 + b('B8') + b('B4'))")
            .rename(['osavi'])        
    
    return img.addBands(osaviImg)
}

var agregateBandsIndexRATIO = function(img){
    
    var ratioImg = img.expression("float(b('B8') / b('B4'))").rename(['ratio'])      

    return img.addBands(ratioImg)
}
var agregateBandsIndexRVI= function(img){

    var rviImg = img.expression("float(b('B4') / b('B8'))").rename(['rvi'])       

    return img.addBands(rviImg)

}
var agregateBandsIndexNDVI= function(img){

    var ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
        .rename(['ndvi'])       

    return img.addBands(ndviImg)

}
var agregateBandsIndexWater= function(img){

    var ndwiImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
        .rename(['ndwi'])       

    return img.addBands(ndwiImg)

}
var AutomatedWaterExtractionIndex= function(img){

    var awei = img.expression(
                        "float(4 * (b('B2') - b('B12')) - (0.25 * b('B8') + 2.75 * b('B11')))"
                    ).rename("awei")          
    
    return img.addBands(awei)
}

var IndiceIndicadorAgua= function(img){

    var iia = img.expression(
            "float((b('B3') - 4 *  b('B8')) / (b('B3') + 4 *  b('B8')))"
    ).rename("iia")
    
    return img.addBands(iia)
}

var agregateBandsIndexEVI = function(img){
        
    var eviImg = img.expression(
        "float(2.4 * (b('B8') - b('B4')) / (1 + b('B8') + b('B4')))").rename(['evi'])     
    
    return img.addBands(eviImg)
}

var agregateBandsIndexLAI= function(img){

    var laiImg = img.expression(
        "(3.618 * float(b('evi') - 0.118))").rename(['lai'])     

    return img.addBands(laiImg)
}
// Chlorophyll vegetation index
var agregateBandsIndexCVI= function(img){

    var cviImgA = img.expression(
        "float(b('B8') * (b('B4') / (b('B2') * b('B2'))))").rename(['cvi'])        
    
    return img.addBands(cviImgA)
}

var agregateBandsIndexBAI= function(img){

    var baiImg = img.expression(
        "float(1) / ((0.1 - b('B4'))**2 + (0.06 - b('B8'))**2)").rename(['bai']) 
    
    return img.addBands(baiImg)
}
// Normalized Difference NIR/SWIR Normalized Burn Ratio 
var agregateBandsIndexNBR= function(img){

    var nbrImg = img.expression(
        "float((b('B8') - b('B11')) / (b('B8') + b('B11')))").rename(['nbr']) 
    
    return img.addBands(nbrImg)
}
//# Tasselled Cap - brightness 
var agregateBandsIndexBrightness= function(img){

    var tasselledCapImg = img.expression(
        "float(0.3037 * b('B2') + 0.2793 * b('B3') + 0.4743 * b('B4')  + 0.5585 * b('B8') + 0.5082 * b('B11') +  0.1863 * b('B12'))")
            .rename(['brightness']) 
    
    return img.addBands(tasselledCapImg)
}
//# Tasselled Cap - wetness 
var agregateBandsIndexwetness= function(img){

    var tasselledCapImg = img.expression(
        "float(0.1509 * b('B2') + 0.1973 * b('B3') + 0.3279 * b('B4')  + 0.3406 * b('B8') + 0.7112 * b('B11') +  0.4572 * b('B12'))")
            .rename(['wetness']) 
    
    return img.addBands(tasselledCapImg)
}
//# Moisture Stress Index (MSI)
var agregateBandsIndexMSI= function(img){

    var msiImg = img.expression(
        "float( b('B8') / b('B11'))").rename(['msi']) 
    
    return img.addBands(msiImg)
}

var agregateBandsIndexSoil = function(img){
    
    var soilImg = img.expression(
        "float(b('B8') - b('B3')) / (b('B8') + b('B3'))")
            .rename(['isoil'])       
    
    return img.addBands(soilImg)    
}
var agregateBandsIndexEVI = function(img){
        
    var eviImg = img.expression(
        "float(2.4 * (b('B8') - b('B4')) / (1 + b('B8') + b('B4')))")
            .rename(['evi'])     
    
    return img.addBands(eviImg)
}

var agregateBandsIndexGVMI = function(img){
        
    var gvmiImg = img.expression(
        "float ((b('B8')  + 0.1) -(b('B11') + 0.02)) / ((b('B8') + 0.1) + (b('B11') + 0.02))") 
            .rename(['gvmi'])     
    
    return img.addBands(gvmiImg)
}

var agregateBandsIndexSAVI = function(img){
        
    var saviImg = img.expression(
        "float(1.5 * (b('B8') - b('B3'))) / (b('B8') + b('B3') + 0.5)")
            .rename(['savi'])     
    
    return img.addBands(saviImg)
}

var agregateBandsIndexsPRI = function(img){
        
    var priImg = img.expression(
        "float((b('B3') - b('B2')) / (b('B3') + b('B2')))")
            .rename(['pri'])   
    var spriImg =   priImg.expression(
        "float((b('pri') + 1) / 2)").rename(['spri'])  
    
    return img.addBands(spriImg)
}

var agregateBandsIndexCO2Flux = function(img){
        
    var co2FluxImg = img.expression(
        "float(b('ndvi') * b('spri'))").rename(['co2flux'])   
        
    return img.addBands(co2FluxImg)
}


// PRI Índice de reflectância fotoquímica
//https://code.earthengine.google.com/e073ae3b060131cfd3b2278bbdda068c

var bandasInd = ['evi','gcvi','osavi','soil','msi','wetness','brightness',
                 'nbr','cvi','lai',"iia","awei",'ndwi','ndvi','rvi','ratio']

var lsIdImg = [
    '20200809T131249_20200809T131246_T23MQP',
    '20200814T131251_20200814T131249_T23KNB'
    
  ]



var img =ee.Image('COPERNICUS/S2_SR/' + lsIdImg[1])
                  .select(['B2', 'B3', 'B4', 'B8', 'B11', 'B12'])
                  .divide(10000)
var visImg = {
  bands: ["B4","B3","B2"],
  gamma: 1,
  max: 0.3500,
  min: 0.045
}
// Map.addLayer(img, visImg, "img")
// Map.centerObject(img, 12)

img = agregateBandsIndexEVI(img)
img = agregateBandsIndexGCVI(img)
img = agregateBandsIndexOSAVI(img)

img = agregateBandsIndexGVMI(img)
img = agregateBandsIndexSAVI(img)
img = agregateBandsIndexsPRI(img)

img = agregateBandsIndexRATIO(img)
img = agregateBandsIndexSoil(img)
img = AutomatedWaterExtractionIndex(img)
img = IndiceIndicadorAgua(img)
img = agregateBandsIndexNDVI(img)
img = agregateBandsIndexWater(img)
img = agregateBandsIndexNBR(img)
img = agregateBandsIndexMSI(img)
img = agregateBandsIndexRVI(img)

img = agregateBandsIndexOSAVI(img)

img = agregateBandsIndexCVI(img)
img = agregateBandsIndexLAI(img)
img = agregateBandsIndexwetness(img)
img = agregateBandsIndexBrightness(img)
img = agregateBandsIndexCO2Flux(img)



// Reduce the region. The region parameter is the Feature geometry.
var meanDictionary = img.select(bandasInd).reduceRegion({
  reducer: ee.Reducer.minMax(),
  geometry: img.geometry(),
  scale: 100,
  maxPixels: 1e9
});

// The result is a Dictionary.  Print it.
print(meanDictionary);