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
        # '52': ["24MXA","24MXV","24MYV","24MZV"],  # ,"24MXA","24LVM","24MXS","24LXQ","24MYU"
        # '95': ["24LUN","24MVB","24MVS","24MWA","24MXA"],  
#         # "24LTJ","24LUK","24LUL","24LUN","24LVL","24MVB","24MWA","24MXA",
#         #          "23LRD","24LTJ","24LUJ","24LVM","24MWU",
              
        '138': ["24MTV","23LQE"] #"24MTA",
#         #      "23MPM","23MQM","23MQN","23MRN","23MRQ","23MRR","23MRS",
#         #     "23KPB","23LND","23LNE","23LNF","23LNG","23LNH","23MPN",
#         #     "23LPG","23LPH","24MTA","24MTT","24MTU","24MTV","23LNC"
       
}

dictArqRegOther = {    
        '52': ["24MXT"],            
                # "24MWT","24MXV","24MYS","24MYV","24MZS","24MZV",
                # "24LWQ","24LWR"
                
        '95': ["24LTQ","24LVR"],
                # "24LWR","24MUA","24MUB","24MVB","24MWA","24MWB",
                # "24MXA"  
        '138': [ "24MTB",
                # "23LRK","23MRS","24LTQ","24MUA","24MUB","23LQJ","23LQK"
                ]
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


# dictArqRegCaat ={
    
#     '9' : [
#             '24LYR',
#         #     '24LZR','24MZS','24MZT','24MZU','24MZV','25LBL','25MBM',
#         #     '25MBN','25MBP','24LYP','24LYQ','25MBQ'                
#         ],
#     '38' : [
#             '23LNK','23LNL',
#         #     '23LPL','23MPM','23MPN','23MQN','23MQP',
#         #         '23MPP',
#         #         '23MQQ','23MQR','23MQS',
#         #     '23LNJ','23LPJ','23LPK','23LMG','23LNF',
#         #     '23LNG','23LNH',
#         #         '23LPH',
#         #         '23LMH','23LMJ','23MNM',
#         #         '23MRT'
#         ],
#     '52' : [
#             '24LZR','24MWT',
#         #     '24MWU','24MXA','24MXV','24MYV',
#         #     '24MZS','24MZT','24MZU','24MZV','24LWR','24LXR','24LYQ','24LYR',
#         #     '24MWS','24MYS','24MYT','24LWP','24LVL','24LVN',
#         #         '24MXS','24MXT','24MXU','24MYU',
#         #     '24LVP','24LWM','24LWN','24LWQ','24LXN','24LXP','24LXQ','24LYP',
#         #     '24LVM','24LWQ','24LVQ',
#         #         '25MBQ'
#         ],
#     '95' : [
#             '23LRL','24LTR'
#         #     ,'24MTS','24MTT','24MUS','24MUT','24MUU','24MUV',
#         #     '24MUA','24MUB','24MVA','24MVB',
#         #         '24MVS', '24MVT','24MVU',
#         #         '24LTP','24LUN','24MWA','24MWU',
#         #     '24MVV','24MWB','24MWS','24MWT','24MWV','24MXA',
#         #     '24MXT','24MXU','24MXV','23LQC','23LQD','23LQE','23LRE','23LRF',
#         #     '23LRJ','24LTQ','24LWR','24LTN','24LTQ','24LVQ','24LTM',
#         #     '24LVR','24LUR','23LQF','23LRD','23LRG','23LRH','24LTJ','24LTN',
#         #     '24LTK','24LTL','24LUM','24LUJ','24LUK','24LUL','24LVL','24LVM',
#         #     '24LVN','24LWP','24LWQ','24LUP','24LVP','24LUQ','24MUC'      
#         ],
#     '138' : [
#             '23LNK','23MPP',
#         #     '23LPL','23LQL','23MRR',
#         #     '23MQM','23MQN','23MPM',
#         #     '23MQP','23MQQ','23MQR','23MQS','23MRP',
#         #     '23MRM','23MRN','23MRQ',
#         #     '24LTR','24MTS','24MUS',
#         #     '23MRS','24MTA','24MTB','24MTT','24MTU','24MTV',
#         #     '24MUA','24MUB','24MUT','24MUU','24MUV','24MVB','23KPB','23LMC',
#         #     '23LNC','23LNF','23LNG','23LNH','23LQE',
#         #     '23LND','23LNE','23LNJ',
#         #     '23LPD','23LPE','23LPF','23LPG','23LPH','23LPJ','23LPK','23LQG',
#         #     '23LQH','23LQJ','23LQK','23LRH','23LRJ','23LRK','23LRL','24LTM',
#         #     '24LTQ','23LRE','23LPC','23LQC','23LQD','23LQF','23LRF','23LRG',
#         # '23KNB','23MRT','24MTC','24MUC'
#         ]     
# }

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
