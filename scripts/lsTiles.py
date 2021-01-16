lsTilesCaat = [
    '23KNB','23KPB','23LMC','23LMG','23LMH','23LMJ','23LNC','23LND',
    '23LNE','23LNF','23LNG','23LNH','23LNJ','23LNK','23LNL','23LPC',
    '23LPD','23LPE','23LPF','23LPG','23LPH','23LPJ','23LPK','23LPL',
    '23LQC','23LQD','23LQE','23LQF','23LQG','23LQH','23LQJ','23LQK',
    '23LQL','23LRD','23LRE','23LRF','23LRG','23LRH','23LRJ','23LRK',
    '23LRL','23MNM','23MPM','23MPN','23MQM','23MQN','23MQP','23MRM',
    '23MRN','23MRP','23MRQ','23MRR','23MRS','23MRT','24LTJ','24LTK',
    '24LTL','24LTM','24LTN','24LTP','24LTQ','24LTR','24LUJ','24LUK',
    '24LUL','24LUM','24LUN','24LUP','24LUQ','24LUR','24LVL','24LVM',
    '24LVN','24LVP','24LVQ','24LVR','24LWM','24LWN','24LWP','24LWQ',
    '24LWR','24LXN','24LXP','24LXQ','24LXR','24LYP','24LYQ','24LYR',
    '24LZR','24MTA','24MTB','24MTC','24MTS','24MTT','24MTU','24MTV',
    '24MUA','24MUB','24MUC','24MUS','24MUT','24MUU','24MUV','24MVA',
    '24MVB','24MVS','24MVT','24MVU','24MVV','24MWA','24MWB','24MWS',
    '24MWT','24MWU','24MWV','24MXA','24MXS','24MXT','24MXU','24MXV',
    '24MYS','24MYT','24MYU','24MYV','24MZS','24MZT','24MZU','24MZV',
    '25LBL','25MBM','25MBN','25MBP','25MBQ'
]

imgRefCaat = 'COPERNICUS/S2_SR/20200809T131249_20200809T131246_T23MQP'


bandasInd = ['osavi',]


dictStd_IndBND = {
    'median': [
                'blue','green','red','nir','swir1','swir2', 
                'evi2','ndvi','ndwi', 'savi', 'gcvi',"awei","iia",
                'gvmi','spri','co2flux','gv','soil','msi','wetness',
                'brightness','cvi','lai','rvi','ratio','contrast',
                'npv', 'soil', 'ndfi','ndfia'                
    ],
    'stdDev':[
                'evi2','ndvi','ndwi', 'savi', 'gcvi',"awei","iia",
                'gvmi','spri','co2flux','gv','soil','msi','wetness',
                'brightness','cvi','lai','rvi','ratio'
                'npv', 'soil', 'ndfi','ndfia'
    ],   
    'dry': [
                'blue','green','red','nir','swir1','swir2', 
                'evi2','ndvi','ndwi', 'savi', 'gcvi',"awei","iia",
                'gvmi','spri','co2flux','gv','soil','msi','wetness',
                'brightness','cvi','lai','rvi','ratio'
                'npv', 'soil', 'ndfi','ndfia'
    ],
    'wet': [
                'blue','green','red','nir','swir1','swir2', 
                'evi2','ndvi','ndwi', 'savi', 'gcvi',"awei","iia",
                'gvmi','spri','co2flux','gv','soil','msi','wetness',
                'brightness','cvi','lai','rvi','ratio'
                'npv', 'soil', 'ndfi','ndfia' 
    ],

}





lsBandas = [
    'blue_median','blue_median_wet','blue_median_dry','blue_min','blue_stdDev','green_median',
    'green_median_dry','green_median_wet','green_median_texture','green_min','green_stdDev',
    'red_median','red_median_dry','red_min','red_median_wet','red_stdDev','nir_median',
    'nir_median_dry','nir_median_wet','nir_min','nir_stdDev','swir1_median','swir1_median_dry',
    'swir1_median_wet','swir1_min','swir1_stdDev','swir2_median','swir2_median_wet','evi2_amp',
    'swir2_min','swir2_stdDev','ndvi_median_dry','ndvi_median_wet','ndvi_median','ndvi_amp',
    'ndvi_stdDev','ndwi_median','ndwi_median_dry','ndwi_median_wet','ndwi_amp','ndwi_stdDev',
    'evi2_median','evi2_median_dry','swir2_median_dry','evi2_median_wet','evi2_stdDev',
    'savi_median_dry','savi_median_wet','savi_median','savi_stdDev','pri_median_dry','pri_median',
    'pri_median_wet','gcvi_median','gcvi_median_dry','gcvi_median_wet','gcvi_stdDev','hallcover_median',
    'hallcover_stdDev','cai_median','cai_median_dry','cai_stdDev','gv_median','gv_amp','gv_stdDev',
    'gvs_median','gvs_median_dry','gvs_median_wet','gvs_stdDev','npv_median','soil_median','soil_amp',
    'soil_stdDev','cloud_median','cloud_stdDev','shade_median','shade_stdDev','ndfi_median','ndfi_amp',
    'ndfi_median_dry','ndfi_median_wet','ndfi_stdDev','sefi_median','sefi_stdDev','sefi_median_dry',
    'wefi_median','wefi_median_wet','wefi_amp','wefi_stdDev','fns_median','fns_median_dry','fns_stdDev'
    'slope'
]


mydict = {
    'median': [],
    'stdDev': [],
    'min': [],
    'max': [],
    'amp': []
}

for bnd in lsBandas:    
    # print(bnd)
    if 'dry' not in bnd and 'wet' not in bnd:

        if 'median' in bnd:
            lsTemp = mydict['median']
            lsTemp.append(bnd)
            mydict['median'] = lsTemp
        
        elif 'stdDev' in bnd:
            lsTemp = mydict['stdDev']
            lsTemp.append(bnd)
            mydict['stdDev'] = lsTemp
        
        elif 'min' in bnd:
            lsTemp = mydict['min']
            lsTemp.append(bnd)
            mydict['min'] = lsTemp
        
        elif 'max' in bnd:
            lsTemp = mydict['max']
            lsTemp.append(bnd)
            mydict['max'] = lsTemp
        
        elif 'amp' in bnd:
            lsTemp = mydict['amp']
            lsTemp.append(bnd)
            mydict['amp'] = lsTemp


for kk, lsBND in mydict.items():

    print( "= estadistico Σ ➳ ⚡ " + kk)

    for band in lsBND:

        print(band)


mydict_dry = {
    'median': [],
    'stdDev': [],
    'min': [],
    'max': [],
    'amp': []
}

for bnd in lsBandas:    
    # print(bnd)
    if 'dry' in bnd:

        if 'median' in bnd:
            lsTemp = mydict_dry['median']
            lsTemp.append(bnd)
            mydict_dry['median'] = lsTemp
        
        elif 'stdDev' in bnd:
            lsTemp = mydict_dry['stdDev']
            lsTemp.append(bnd)
            mydict_dry['stdDev'] = lsTemp
        
        elif 'min' in bnd:
            lsTemp = mydict_dry['min']
            lsTemp.append(bnd)
            mydict_dry['min'] = lsTemp
        
        elif 'max' in bnd:
            lsTemp = mydict_dry['max']
            lsTemp.append(bnd)
            mydict_dry['max'] = lsTemp
        
        elif 'amp' in bnd:
            lsTemp = mydict_dry['amp']
            lsTemp.append(bnd)
            mydict_dry['amp'] = lsTemp
print("")
print("############ print periodo SECO ##################")

for kk, lsBND in mydict_dry.items():

    print( "= estadistico Σ ➳ ⚡  " + kk)

    for band in lsBND:

        print(band)

mydict_wet = {
    'median': [],
    'stdDev': [],
    'min': [],
    'max': [],
    'amp': []
}


for bnd in lsBandas:    
    # print(bnd)
    if 'wet' in bnd:

        if 'median' in bnd:
            lsTemp = mydict_wet['median']
            lsTemp.append(bnd)
            mydict_wet['median'] = lsTemp
        
        elif 'stdDev' in bnd:
            lsTemp = mydict_wet['stdDev']
            lsTemp.append(bnd)
            mydict_wet['stdDev'] = lsTemp
        
        elif 'min' in bnd:
            lsTemp = mydict_wet['min']
            lsTemp.append(bnd)
            mydict_wet['min'] = lsTemp
        
        elif 'max' in bnd:
            lsTemp = mydict_wet['max']
            lsTemp.append(bnd)
            mydict_wet['max'] = lsTemp
        
        elif 'amp' in bnd:
            lsTemp = mydict_wet['amp']
            lsTemp.append(bnd)
            mydict_wet['amp'] = lsTemp

print("")
print("############ print periodo chuvoso ##################")
for kk, lsBND in mydict_wet.items():

    print( "= estadistico Σ ➳ ⚡ " + kk)

    for band in lsBND:

        print(band)

keyss = []
dictBND = {}
for bnd in lsBandas:    
    # print(bnd)
    lsNom = bnd.split('_')
    banda = lsNom[0]
    
    if banda not in keyss:
        keyss.append(banda)
        lsT = []
        for nbnd in lsNom[1:]:
            lsT.append(nbnd)
        
        dictBND[banda] = lsT

    else:

        lsT = dictBND[banda]
        addiciono = False
        for nbnd in lsNom[1:]:
            if nbnd not in lsT:
                lsT.append(nbnd)
                addiciono = True

        if addiciono == True:
            dictBND[banda] = lsT


for bnd, lsStd in dictBND.items():
    print("banda == ➳ ⚡ " + bnd)

    for std in lsStd:
        print(std)


print(keyss)