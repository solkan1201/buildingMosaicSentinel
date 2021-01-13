
  // Get a palette: a list of hex strings
  var palettes = require('users/gena/packages:palettes');
  var palette = palettes.cmocean.Speed[7];
  
  
  var agregateBandsIndexNDVI= function(img){
  
      var ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
                      .add(1).multiply(10000).rename(['ndvi_n'])       
  
      return img.addBands(ndviImg)
  
  }
  
  var BandsIndexNDVI= function(img){
  
      var ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
                        .multiply(100).byte().rename(['ndvi_s'])       
  
      return img.addBands(ndviImg)
  
  }
  
  var IndexNDVI= function(img){
  
      var ndviImg = img.expression("float(b('B8') - b('B12')) / (b('B8') + b('B12'))")
                        .rename(['ndvi'])       
  
      return img.addBands(ndviImg)
  
  }
  
  var lsIdImg = [
      '20200809T131249_20200809T131246_T23MQP',
      '20200814T131251_20200814T131249_T23KNB',
      '20201015T130249_20201015T130251_T24LVR'
      
    ]
  
  
  
  var img =ee.Image('COPERNICUS/S2_SR/' + lsIdImg[0])
                    .select(['B2', 'B3', 'B4', 'B8', 'B11', 'B12'])
                    .divide(10000)
  
  img = IndexNDVI(img)
  img = agregateBandsIndexNDVI(img)
  img = BandsIndexNDVI(img)
  
  file:///home/superusuario/Downloads/remotesensing-11-00632.pdf
  /// https://code.earthengine.google.com/3a121cbd7a98d811b4b8c5638cf356bb  //
  ///  https://code.earthengine.google.com/289b9a794016ff658bea9ce3e920e6e3 //
  var visImg = {
    bands: ["B4","B3","B2"],
    gamma: 1,
    max: 0.3500,
    min: 0.045
  }
  var visInd = {
    min: -0.1053,
    max: 0.6863513588905334,
    palette: palette
  }
  var visIndByte = {
    min: 0,
    max: 62,
    palette: palette
  }
  var visIndNor = {
    min: 8300,
    max: 16034,
    palette: palette
  }
  
  Map.addLayer(img, visImg, "img")
  // Map.centerObject(img, 12)
  
  Map.addLayer(img.select('ndvi'), visInd, 'NDVI')
  Map.addLayer(img.select('ndvi_s'), visIndByte, 'NDVItoByte')
  Map.addLayer(img.select('ndvi_n'), visIndNor, 'NDVInorm')
  
  // Pre-define some customization options.
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
  var histNDVI= ui.Chart.image.histogram(img.select(["ndvi"]), img.geometry(), 100)
      .setSeriesNames(['NDVI'])
      .setOptions(options);
  
  // Display the histogram.
  print(histNDVI);
  
  var options = {
    title: 'NDVI_toByte',
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
      0: {color: 'blue'},
      1: {color: 'magenta'},
      2: {color: 'red'}
    }
  };
  
  // Make the histogram, set the options.
  var histNDVIsin = ui.Chart.image.histogram(img.select(["ndvi_s"]), img.geometry(), 100)
      .setSeriesNames(['NDVI_byte'])
      .setOptions(options);
  
  // Display the histogram.
  print(histNDVIsin);
  
  
  var options = {
    title: 'NDVI_Norm',
    fontSize: 20,
    hAxis: {title: 'DN'},
    vAxis: {title: 'count of DN'},
    series: {
      0: {color: 'blue'},
      1: {color: 'magenta'},
      2: {color: 'red'}
    }
  };
  
  // Make the histogram, set the options.
  var histNDVINorm = ui.Chart.image.histogram(img.select(["ndvi_n"]), img.geometry(), 100)
      .setSeriesNames(['NDVI_norm'])
      .setOptions(options);
  
  // Display the histogram.
  print(histNDVINorm);
  
  
  
  
  