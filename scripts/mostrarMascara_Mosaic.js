var estilos = {
    style_panel: {
        position: 'top-center',
        // width: '45px',
        height: '45px',
        margin: '0px',
        padding: '0px',
    },
    style_selector:{
        // width: '30px',
        height: '30px',
        padding: '1px',
        fontFamily: 'serif',
        textAlign: 'left'
    },
    tyle_labels : { 
        fontFamily: 'serif',
        fontWeight: 'bold', 
        backgroundColor: '#FFFFFF',
        padding: '1px',
    },
    style_button : {
        position: 'top-center',
        border: '1px solid #000000',
        // width: '200px',
        padding: '3px',
      }

}


var beforeMap = ui.Map({
    style: {
        border: '2px solid black'
    }
});


var dictArqRegCaat ={    
    '9' : [
            '24LYR','24LZR','24MZS','24MZT','24MZU','24MZV','25LBL','25MBM',
            '25MBN','25MBP','24LYP','24LYQ','25MBQ'                
        ],
    '38' : [
            '23LNK','23LNL','23LPL','23MPM','23MPN','23MQN','23MQP','23MPP',
            '23LNJ','23LPJ','23LPK','23LMG','23LNF','23MQQ','23MQR','23MQS',
            '23LNG','23LNH','23LPH','23LMH','23LMJ','23MNM','23MRT'
        ],
    '52' : [
            '24LZR','24MWT','24MWU','24MXA','24MXV','24MYV','24MXS','24MXT',
            '24MZS','24MZT','24MZU','24MZV','24LWR','24LXR','24LYQ','24LYR',
            '24MWS','24MYS','24MYT','24LWP','24LVL','24LVN','24MXU','24MYU',                
            '24LVP','24LWM','24LWN','24LWQ','24LXN','24LXP','24LXQ','24LYP',
            '24LVM','24LWQ','24LVQ','25MBQ'
        ],
    '95' : [
            '23LRL','24LTR','24LTP','24LUN','24MWA','24MWU','24MVT','24MVU',
            '24MTS','24MTT','24MUS','24MUT','24MUU','24MUV','24MVA','24MVB',
            '24MUA','24MUB','24MVS','24MVV','24MWB','24MWS','24MWT','24MWV',             
            '24MXT','24MXU','24MXV','23LQC','23LQD','23LQE','23LRE','23LRF',
            '23LRJ','24LTQ','24LWR','24LTN','24LTQ','24LVQ','24LTM','24MXA',
            '24LVR','24LUR','23LQF','23LRD','23LRG','23LRH','24LTJ','24LTN',
            '24LTK','24LTL','24LUM','24LUJ','24LUK','24LUL','24LVL','24LVM',
            '24LVN','24LWP','24LWQ','24LUP','24LVP','24LUQ','24MUC'  
        ],
    '138' : [
            '23LNK','23MPP','23LPL','23LQL','23MRR','23MQM','23MQN','23MPM',
            '23MQP','23MQQ','23MQR','23MQS','23MRP','23MRM','23MRN','23MRQ',
            '24LTR','24MTS','24MUS','23MRS','24MTA','24MTB','24MTT','24MTU',
            '24MUA','24MUB','24MUT','24MUU','24MUV','24MVB','23KPB','23LMC',
            '23LNC','23LNF','23LNG','23LNH','23LQE','24MTV','23LND','23LNE',
            '23LPD','23LPE','23LPF','23LPG','23LPH','23LPJ','23LPK','23LQG',
            '23LQH','23LQJ','23LQK','23LRH','23LRJ','23LRK','23LRL','24LTM',
            '24LTQ','23LRE','23LPC','23LQC','23LQD','23LQF','23LRF','23LRG',
            '23KNB','23MRT','24MTC','24MUC','23LNJ',
        ]     
}

var visImg = {
    bands: ["median_red","median_green","median_blue"],
    max: 2000,
    min: 200
};

var layeradicionadas = false;
var pathMosaic = 'users/mapbiomascaatinga05/mosaicSentinel2';
var pathMosaicMB = 'projects/mapbiomas-workspace/AMOSTRAS/col5/CAATINGA/MOSAIC/mosaics';
var pathMask = 'users/gleddson1/Mapeamento_Caatinga/Collections/maskCollectionCaatinga';
var pathGrade = 'projects/mapbiomas-arida/ALERTAS/auxiliar/shpGradeSent_IC_Caat'
var mosaicS2 = ee.ImageCollection(pathMosaic);
var mS2Caat = ee.ImageCollection(pathMosaicMB);
var mask = ee.Image(pathMask)
var gradeS2 = ee.FeatureCollection(pathGrade)

// print(mosaicS2);
mS2Caat = mS2Caat.merge(mosaicS2);
// print(mosaicS2);

var Visualize_Map = ui.Map({
    style: {
        border: '2px solid black'
    }
});

var orbActivo = null;
var tileActivo = null;

var funcaoVisualizar = function(){
    
    print("dentro ");
    print('tile ', tileActivo);
    print("orbita ", orbActivo);
    var layerName = orbActivo + '_' + tileActivo

    // var geomet = gradeS2.filter(ee.Filter.and(
    //                             ee.Filter.eq('MGRS_TILE', tileActivo),
    //                             ee.Filter.eq('SENSING_ORBIT_NUMBER', parseInt(orbActivo))
    //                         )).geometry() 
    // print(geomet)
    var mS2CaatBlue = mS2Caat.filter(ee.Filter.eq('banda', 'median_blue'))
                             .filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', orbActivo))
                             .filter(ee.Filter.eq('MGRS_TILE', tileActivo))
                             print(mS2CaatBlue);
    var geomet = mS2CaatBlue.geometry()
    var mS2CaatGreen = mS2Caat.filter(ee.Filter.eq('banda', 'median_green'))
                              .filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', orbActivo))
                              .filter(ee.Filter.eq('MGRS_TILE', tileActivo))
    var mS2CaatRed = mS2Caat.filter(ee.Filter.eq('banda', 'median_red'))
                            .filter(ee.Filter.eq('SENSING_ORBIT_NUMBER', orbActivo))
                            .filter(ee.Filter.eq('MGRS_TILE', tileActivo))
    var mS2CaatRGB = mS2CaatBlue.mosaic().addBands(mS2CaatGreen.mosaic()).addBands(mS2CaatRed.mosaic())

    var mascaraVeg = mask.clip(geomet)
    mascaraVeg = mascaraVeg.eq(1)
    
    if (layeradicionadas === true){
        Visualize_Map.clear();
    }
    Visualize_Map.addLayer(mS2CaatRGB, visImg, layerName)
    Visualize_Map.addLayer(mascaraVeg.updateMask(mascaraVeg), {min: 0, max: 1, palette: ['grey', 'green']}, "CaatingaMask")
    Visualize_Map.centerObject(geomet, 12)
    layeradicionadas = true
}

var imageTile = null;



var titlePainel = ui.Label(" 🔰 Painel de Analises Mascara Vegetação Nativa 🔰  ");
var orbitaLabel = ui.Label("Select Orbit 📡");
orbitaLabel.setStyle = estilos.tyle_labels;
var orbita_select = ui.Select({
    items: Object.keys(dictArqRegCaat),
    onChange: function (key) {
        print("chave selecionada ", key);
        orbActivo = key;
        tiles_select.items().reset(dictArqRegCaat[key]);
        tiles_select.setValue(tiles_select.items().get(0));
        return dictArqRegCaat[key];         
    }
});
var tilesLabel = ui.Label("Select Tile 📡");
tilesLabel.setStyle = estilos.tyle_labels;
var tiles_select = ui.Select({
    items: dictArqRegCaat[orbActivo],
    onChange: function (valor) {
      print("tile selecionado ", valor)
        tileActivo = valor;
        return tileActivo;         
    }
})
var visualizador_button = ui.Button('SHOW');
visualizador_button.onClick(funcaoVisualizar)

var panelTile_Select = ui.Panel(
        [titlePainel, orbitaLabel, orbita_select,tilesLabel, tiles_select, visualizador_button],
        ui.Panel.Layout.Flow('horizontal', true)
    );
panelTile_Select.setStyle = estilos.style_panel;



var panelGeral = ui.Panel(
    [panelTile_Select ,Visualize_Map],
    ui.Panel.Layout.Flow('vertical'), {
      width: '100%',
      height: '100%',
    });
// panelGeral.se
ui.root.widgets().reset([panelGeral]);
ui.root.setLayout(ui.Panel.Layout.Flow('vertical'));
