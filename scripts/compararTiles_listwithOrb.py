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
dictArqReg = {    
        # '9': ["25MBP","25LBL","25MBM","25MBN"],   # 
        # '52': ["24MWT","24MZS"],  
        #"24MYS","24MXA","24MXS","24LXQ","24MZV","24MYV","24MXV","24MYU","24MYV",
        # "24MZS","24LWQ","24LVM",
        '95': ['24MWT'],  # "24MUA","24MUB"
        # "24LTJ", "24MUB","24MWB","24MXA"
          # "24MVB",,"24MXA""24MVS","24MWA","24LUN","24MVB","24MUA","24MXA","24MWA"
#         # "24LTJ","24LUK","24LUL","24LUN","24LVL","24MVB","24MWA","24MXA",
#         #          "23LRD","24LTJ","24LUJ","24LVM","24MWU",
              
        # '138': ["24MUA","23LNH"]  
        #"23KNB","23LMH","23LNH","23LMC","23MRS", 
        # ["23LNC","23LNH","23LPH","24MTA","24MTB","24MTT","24MTV","23LQE"
        #         "24MUA","24MUB","23LNC"] #"24MTV",        
#         #      "23MPM","23MQM","23MQN","23MRN","23MRQ","23MRR","23MRS",
#         #     "23KPB","23LND","23LNE","23LNF","23LNG","23LNH","23MPN",
#         #     "23LPG","23LPH","24MTA","24MTT","24MTU","23LNC"
       
}

dictArqRegOther = {    
        '52': ["24LVM"],            
                # "24MWT","24MXV","24MYS","24MYV","24MZS","24MZV",
                # "24LWQ",,"24MXT","24LWR"
                
        '95': ["23LRJ","24LTP"],
        #         # "24LWR","24MUA","24MUB","24MVB","24MWA","24MWB",
        #         # "24MXA"  ,"24LVR""24MWU","24LTQ","24LWR","24MWT"
        # '138': ["23LQJ","23LRJ","23LRK"]
                # "23MRS","24MUA","24MUB","24MTB","23LQJ",
                # ]"24LTQ","23LQK"
}

dictArqRegPan = {    
        '24': [
                '21KVR','21KWA','21KWR','21KWS','21KWT','21KWU',
                '21KWV','21KXA','21KXB','21KXR','21KXS','21KXT',
                '21KXU','21KXV','21KYA','21KYB','21KYS','21KYT',
                '21KYU','21KYV','21KZA','21KZB','21KZU','21KZV',
                '21LXC','21LXD','21LXE','21LYC','21LYD','21LYE',
                '21LZC','22KBD','22KBE','22KBF','22KBG','22LBH'
        ],
        '67' : [
                '21KUA','21KUB','21KUR','21KUS','21KUT','21KUU',
                '21KVA','21KVB','21KVR','21KVS','21KVT','21KVU',
                '21KVV','21KWA','21KWB','21KWR','21KWS','21KWT',
                '21KWU','21KWV','21KXA','21KXB','21KXU','21KXV',
                '21LUC','21LUD','21LVC','21LVD','21LVE','21LWC',
                '21LWD','21LWE','21LXC','21LXD','21LXE','21LYD',
                '21LYE'
        ],    
        '110': [
                '20KRG','20LRH','21KTB','21KUA','21KUB','21KVB',
                '21LTC','21LTD','21LUC','21LUD','21LUE','21LVC',
                '21LVD','21LVE'
        ],
        '124' : [
                '21KZA','21KZU','21KZV','22KBD','22KBE','22KBF'
        ]
}

dictArqRegMAtla = {
        
        '52': [
               '23KQQ',
               '23KQR','23KRQ','23KRR','23KRS','23KRT','23KRU','24KTA',
               '24KTB','24KTC','24KTD','24KTE','24KTF','24KTV','24KUB',
               '24KUC','24KUD','24KUE','24KUF','24KUG','24KVD','24KVE',
               '24KVF','24KVG','24KWF','24LUH','24LUJ','24LVH','24LVJ',
               '24LVK','24LWH','24LWJ','24LWK','24LWL','24LXM','24LYN',
               '24LZQ','25MBP','23KRV',
        ],
        '124' : [
                '21JXH','21JXJ','21JXK','21JYH','21JYJ','21JYK','21JYL',
                '21JYM','21JYN','21JZM','21JZN','21KXP','21KYP','21KYQ',
                '21KYR','21KYS','21KZP','21KZQ','21KZR','21KZS','22JBN',
                '22JBP','22JBQ','22JBR','22JBS','22JBT','22JCQ','22JCR',
                '22JCS','22JCT','22KBA','22KBU','22KBV','22KCA','22KCB',
                '22KCU','22KCV','22KDA','22KDB','22KDC','22KDD','22KDE',
                '22KDV','22KEE','22KDU',

        ],
        '138': [
                '22JGP','22JGQ','22JHT','22KHA','22KHU','22KHV','23JKN',
                '23JLN','23KKP','23KKQ','23KKR','23KLP','23KLQ','23KLR',
                '23KLS','23KLT','23KMP','23KMQ','23KMR','23KMS','23KMT',
                '23KMU','23KNQ','23KNR','23KNS','23KNT','23KNU','23KPA',
                '23KPR','23KPS','23KPT','23KPU','23KPV','23KQA',

        ],
        '9' : [
               '24LZQ','25LBK','25MCM','25MCN','24LZP',
        ],
       '95' : [
                '23KNQ','23KNR','23KNS','23KNT','23KPA','23KPQ','23KPR',
                '23KPS','23KPT','23KPU','23KPV','23KQA','23KQB','23KQQ',
                '23KQR','23KQS','23KQT','23KQU','23KQV','23KRA','23KRB',
                '23KRQ','23KRR','23KRS','23KRT','23KRU','23KRV','23LRC',
                '24KTA','24KTB','24KTC','24KTD','24KTE','24KTF','24KTG',
                '24KTV','24KUD','24KUE','24KUF','24KUG','24LTH','24LUH',
                '24LVJ','24LVK',
        ],
       '24' : [
                '21KXP','21KXQ','21KYP','21KYQ','21KYR','21KZR','21KZS',

        ],
       '38' : [
                '22JDM','22JDN','22JDP','22JDQ','22JEM','22JEN','22JEP',
                '22JEQ','22JER','22JES','22JET','22JFN','22JFP','22JFQ',
                '22JFR','22JFS','22JFT','22JGP','22JGQ','22JGR','22JGS',
                '22JGT','22JHT','22KEU','22KFA','22KFB','22KFC','22KFU',
                '22KFV','22KGA','22KGB','22KGC','22KGD','22KGE','22KGU',
                '22KGV','22KHA','22KHB','22KHC','22KHD','22KHU','22KHV',
                '23JKN','23KKP','23KKQ','23KKR','23KKS','23KKT','23KKU',
                '23KLP','23KLQ','23KLR','23KLS','23KLT',

        ],
       '81' : [
                '21JYH','21JZM','22JBM','22JBN','22JBP','22JBQ','22JBR',
                '22JBS','22JCM','22JCN','22JCP','22JCQ','22JCR','22JCS',
                '22JCT','22JDM','22JDN','22JDP','22JDQ','22JDR','22JDS',
                '22JDT','22JEN','22JEP','22JEQ','22JER','22JES','22JET',
                '22JFS','22JFT','22KCA','22KCB','22KCU','22KCV','22KDA',
                '22KDB','22KDC','22KDD','22KDE','22KDU','22KDV','22KEA',
                '22KEB','22KEC','22KED','22KEE','22KEU','22KEV','22KFA',
                '22KFB','22KFC','22KFD','22KFE','22KFF','22KFU','22KFV',
                '22KGA','22KGB','22KGC','22KGD','22KGE','22KGF','22JEM',

        ]
       
}

dictArqRegPampa = {
        '124': [
               '21HYE','21JWF','21JWG','21JWH','21JWJ','21JXF','21JXG',
               '21JXH','21JXJ','21JXK','21JYF','21JYG','21JYH','21JYJ',
               '21JYK','22HBK','22JBL','22JBM','22JBN','22JBP','22JBQ',

        ],
        '24' : [
               '21JVG','21JVH','21JWG','21JWH','21JWJ','21JXH','21JXJ',

        ],
        '38': [
               '22JDM','22JDN','22JEL','22JEM','22JEN','22HCJ','22HCK',
               '22HDK','22JCL','22JDL',

        ],
        '81' : [
               '21HYE','21JYF','21JYG','21JYH','22HBH','22HBJ','22HBK',
               '22HCH','22HCJ','22HCK','22HDK','22JBL','22JBM','22JBN',
               '22JBP','22JBQ','22JCL','22JCM','22JCN','22JCP','22JCQ',
               '22JDL','22JDM','22JDN',
 
        ]
       
}


dictArqRegCaat ={    
    '9' : [
        #     '24LYR','24LZR','24MZS','24MZT','24MZU','24MZV','25LBL','25MBM',
        #     '25MBN','25MBP','24LYP','24LYQ',
            '25MBQ'                
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
            '23KNB','23MRT','24MTC','24MUC','23LNJ'
        ]     
}

# dictArqReg = {
#     '95': ['24MVS', '24LUL', '24MXU'],   #, 
#     # '52': ['24LXR','24MXU'],  #
#     # '38': ['23LNJ']
# }

imgRefCaat = 'COPERNICUS/S2_SR/20200809T131249_20200809T131246_T23MQP'

imgRefPan = ''

imgRefMatAtl = ''

imgRefPampa = ''


# lsAllTiles = []
# for ltile in lsTilesCaat:
#     encontrado = False
#     for orb, lsTiles in dictArqReg.items():        
#         # print("orbita {} ".format(orb))
#         # print(lsTiles)        
#         if ltile in lsTiles:
#             encontrado = True
    
#     if encontrado == False:
#         lsAllTiles.append(ltile)
#         print(" não encontado  === {}  === ".format(ltile))


# print("lista dos alertas sem orbi")

# print(lsAllTiles )


dictArqRegbandas = {
    
    '9' : {
            '24LYR': ["median_brightness"],
            '24LZR': [],
            '24MZS': [],
            '24MZT': [],
            '24MZU': [],
            '24MZV': [],
            '25LBL': [],
            '25MBM': [],
            '25MBN': [],
            '25MBP': ['median_blue'],
            '24LYP': [],
            '24LYQ': [],
            '25MBQ': []                
    },
    '38' : {
            '23LNK': [],
            '23LNL': [],
            '23LPL': [],
            '23MPM': [],
            '23MPN': [],
            '23MQN': [],
            '23MQP': [  'median_red','median_nir','median_swir1','median_swir2',
                        'median_evi','median_ratio','median_rvi','median_ndvi',
                        'median_ndwi'],
            '23MPP': [],
            '23MQQ': [],
            '23MQR': [],
            '23MQS': [],
            '23LNJ': [],
            '23LPJ': [],
            '23LPK': [],
            '23LMG': [],
            '23LNF': [],
            '23LNG': [],
            '23LNH': [],
            '23LPH': [],
            '23LMH': [],
            '23LMJ': [],
            '23MNM': [],
            '23MRT': []
    },
    '52' : {
            '24LZR': [],
            '24MWT': [],
            '24MWU': [],
            '24MXA': [],
            '24MXU': [],
            '24MXV': [],
            '24MYU': [],
            '24MYV': [],
            '24MZS': [],
            '24MZT': [],
            '24MZU': [],
            '24MZV': [],
            '24LWR': [],
            '24LXR': [],
            '24LYQ': [],
            '24LYR': [],
            '24MWS': [],
            '24MXS': [],
            '24MXT': [],
            '24MYS': [],
            '24MYT': [],
            '24LWP': [],
            '24LVL': [],
            '24LVN': [],
            '24LVP': [],
            '24LWM': [],
            '24LWN': [],
            '24LWQ': [],
            '24LXN': [],
            '24LXP': [],
            '24LXQ': [],
            '24LYP': ["median_wetness","median_brightness"],
            '24LVM': [],
            '24LWQ': [],
            '24LVQ': [],
            '25MBQ': []
    },
    '95' : {
            '23LRL': ["median_co2flux"],
            '24LTR': ["median_co2flux"],
            '24MTS': ["median_co2flux"],
            '24MTT': ["median_co2flux"],
            '24MUS': ["median_co2flux"],
            '24MUT': ["median_co2flux"],
            '24MUU': ["median_co2flux"],
            '24MUV': ["median_co2flux"],
            '24MUU': [],
            '24MUV': [],
            '24MUU': [],
            '24MUV': [],
            '24MUA': [],
            '24MUB': [],
            '24MVA': [],
            '24MVB': [],
            '24MVS': [],
            '24MVT': [],
            '24MVU': [],
            '24LTP': [  'median_blue','median_green','median_red',
                        'median_gv','median_npv','median_soil',
                        'median_ndfia','median_contrast'],
            '24MVV': [],
            '24MWA': [],
            '24MWB': [],
            '24MWS': [],
            '24MWT': [],
            '24MWU': [],
            '24MWV': [],
            '24MXA': [],
            '24MXT': [],
            '24MXU': [],
            '24MXV': [],
            '23LQC': [],
            '23LQD': [],
            '23LQE': [],
            '23LRE': [],
            '23LRF': [],
            '23LRJ': [],
            '24LTQ': [],
            '24LWR': [],
            '24LTN': [],
            '24LUN': [],
            '24LTQ': [],
            '24LVQ': [],
            '24LTM': [],
            '24LVR': [],
            '24LUR': [],
            '23LQF': [],
            '23LRD': [],
            '23LRG': [],
            '23LRH': [],
            '24LTJ': [],
            '24LTN': [],
            '24LTK': [],
            '24LTL': [],
            '24LUM': [],
            '24LUJ': [],
            '24LUK': [],
            '24LUL': [],
            '24LVL': [],
            '24LVM': [],
            '24LVN': [],
            '24LWP': [],
            '24LWQ': [],
            '24LUP': [],
            '24LVP': [],
            '24LUQ': [],
            '24MUC': []      
    },
    '138' : {
            '23LNK': [],
            '23MPP': [],
            '23LPL': [],
            '23LQL': [],
            '23MQM': [],
            '23MQN': [],
            '23MPM': [],
            '23MRR': [],
            '23MQP': [],
            '23MQQ': [],
            '23MQR': [],
            '23MQS': [],
            '23MRP': [],
            '23MRM': [],
            '23MRN': [],
            '23MRQ': [],
            '24LTR': [],
            '24MTS': [],
            '24MUS': [],
            '23MRS': [],
            '24MTA': [],
            '24MTB': [],
            '24MTT': [],
            '24MTU': [],
            '24MTV': [],
            '24MUA': [],
            '24MUB': [],
            '24MUT': [],
            '24MUU': [],
            '24MUV': [],
            '24MVB': [],
            '23KPB': [],
            '23LMC': [],
            '23LNC': [],
            '23LND': [],
            '23LNE': [],
            '23LNF': [],
            '23LNG': [],
            '23LNH': [],
            '23LNJ': [],
            '23LPD': [],
            '23LPE': [],
            '23LPF': [],
            '23LPG': [],
            '23LPH': [],
            '23LPJ': [],
            '23LPK': [],
            '23LQG': [],
            '23LQH': [],
            '23LQJ': [],
            '23LQK': [],
            '23LRH': [],
            '23LRJ': [],
            '23LRK': [],
            '23LRL': [],
            '24LTM': [],
            '24LTQ': [],
            '23LQE': [],
            '23LRE': [],
            '23LPC': [],
            '23LQC': [],
            '23LQD': [],
            '23LQF': [],
            '23LRF': [],
            '23LRG': [],
            '23KNB': [],
            '23MRT': [],
            '24MTC': [],
            '24MUC': []
    }     
}

lsICsizeZero = [
        "9_24LYR","9_24LZR","9_24MZS","9_24MZT","9_24MZU","9_24MZV","9_25LBL","9_25MBM",
        "9_25MBN","9_25MBP","9_24LYP","9_24LYQ","9_25MBQ","38_23LNK","38_23LNL","38_23LPL",
        "38_23MPM","38_23MPN","38_23MQN","38_23MQP","38_23MPP","38_23LNJ","38_23LPJ","38_23LPK",
        "38_23LMG","38_23LNF","38_23MQQ","38_23MQR","38_23MQS","38_23LNG","38_23LNH","38_23LPH",
        "38_23LMH","38_23LMJ","38_23MNM","38_23MRT","52_24LZR","52_24MWT","52_24MWU","52_24MXA",
        "52_24MXV","52_24MYV","52_24MXS","52_24MXT","52_24MZS","52_24MZT","52_24MZU","52_24MZV",
        "52_24LWR","52_24LXR","52_24LYQ","52_24LYR","52_24MWS","52_24MYS","52_24MYT","52_24LWP",
        "52_24LVL","52_24LVN","52_24MXU","52_24MYU","52_24LVP","52_24LWM","52_24LWN","52_24LWQ",
        "52_24LXN","52_24LXP","52_24LXQ","52_24LYP","52_24LVM","52_24LWQ","52_24LVQ","52_25MBQ",
        "95_23LRL","95_24LTR","95_24LTP","95_24LUN","95_24MWA","95_24MWU","95_24MVT","95_24MVU",
        "95_24MTS","95_24MTT","95_24MUS","95_24MUT","95_24MUU","95_24MUV","95_24MVA","95_24MVB",
        "95_24MUA","95_24MUB","95_24MVS","95_24MVV","95_24MWB","95_24MWS","95_24MWT","95_24MWV",
        "95_24MXT","95_24MXU","95_24MXV","95_23LQC","95_23LQD","95_23LQE","95_23LRE","95_23LRF",
        "95_23LRJ","95_24LTQ","95_24LWR","95_24LTN","95_24LTQ","95_24LVQ","95_24LTM","95_24MXA",
        "95_24LVR","95_24LUR","95_23LQF","95_23LRD","95_23LRG","95_23LRH","95_24LTJ","95_24LTN",
        "95_24LTK","95_24LTL","95_24LUM","95_24LUJ","95_24LUK","95_24LUL","95_24LVL","95_24LVM",
        "95_24LVN","95_24LWP","95_24LWQ","95_24LUP","95_24LVP","95_24LUQ","95_24MUC","138_23LNK",
        "138_23MPP","138_23LPL","138_23LQL","138_23MRR","138_23MQM","138_23MQN","138_23MPM",
        "138_23MQP","138_23MQQ","138_23MQR","138_23MQS","138_23MRP","138_23MRM","138_23MRN",
        "138_23MRQ","138_24LTR","138_24MTS","138_24MUS","138_23MRS","138_24MTA","138_24MTB",
        "138_24MTT","138_24MTU","138_24MUA","138_24MUB","138_24MUT","138_24MUU","138_24MUV",
        "138_24MVB","138_23KPB","138_23LMC","138_23LNC","138_23LNF","138_23LNG","138_23LNH",
        "138_23LQE","138_24MTV","138_23LND","138_23LNE","138_23LPD","138_23LPE","138_23LPF",
        "138_23LPG","138_23LPH","138_23LPJ","138_23LPK","138_23LQG","138_23LQH","138_23LQJ",
        "138_23LQK","138_23LRH","138_23LRJ","138_23LRK","138_23LRL","138_24LTM","138_24LTQ",
        "138_23LRE","138_23LPC","138_23LQC","138_23LQD","138_23LQF","138_23LRF","138_23LRG",
        "138_23KNB","138_23MRT","138_24MTC","138_24MUC","138_23LNJ"
]