var idAssetBA = 'users/CartasSol/shapes/SUB_BA1'
var idAssetCaat = 'users/CartasSol/shapes/nCaatingaBff3000'


var limCaat = ee.FeatureCollection(idAssetCaat)
var grade =ee.FeatureCollection('users/solkancengine17/shapes/grade_sentinel_brasil')
                        .filterBounds(limCaat)
print("grade Sentinel 2", grade)

var empty = ee.Image().byte();

// Paint all the polygon edges with the same number and width, display.
var paint_grade = ee.Image().byte().paint({
  featureCollection: grade,
  color: 1,
  width: 3
});
Map.addLayer(paint_grade, {palette: 'FF0000'}, 'grade');


// visualiza a região de estudo
var paint_Region = ee.Image().byte().paint({
  featureCollection: limCaat,
  color: 1,
  width: 3
});
Map.addLayer(paint_Region, {palette: '0000FF'}, 'grade');
// Map.addLayer(limCaat)

var lsgrade = grade.reduceColumns(ee.Reducer.toList(), ['NAME']).get('list')
print(lsgrade)
