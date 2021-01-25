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
        # '9': ["25LBL","25MBM","25MBN"],
        '52': ["24MYU"],  # ,"24MXA","24LVM","24MXS","24LXQ"
        '95': ["24LUN","24MWU","24MVS"],
        # "24LTJ","24LUK","24LUL","24LUN","24LVL","24MVB","24MWA","24MXA",
        #          "23LRD","24LTJ","24LUJ","24LVM"
              
        '138': ["24MTA","24MTT","24MTU","24MTV","23LNC","23LQE"]                            
        #      "23MPM","23MQM","23MQN","23MRN","23MRQ","23MRR","23MRS",
        #     "23KPB","23LND","23LNE","23LNF","23LNG","23LNH","23MPN",
        #     "23LPG","23LPH",
       
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


# dictArqReg ={
    
#     # '9' : [
#             # '24LYR','24LZR','24MZS','24MZT','24MZU','24MZV','25LBL','25MBM',
#             # '25MBN','25MBP','24LYP','24LYQ','25MBQ'                
#         # ],
# #     '38' : [
# # #             '23LNK','23LNL','23LPL','23MPM','23MPN','23MQN','23MQP',
# #                 '23MPP',
# #                 '23MQQ','23MQR','23MQS',
# #             # '23LNJ','23LPJ','23LPK','23LMG','23LNF',
# #             # '23LNG','23LNH',
# #                 '23LPH',
# #                 # '23LMH','23LMJ','23MNM',
# #                 '23MRT'
# #         ],
#     # '52' : [
# # #             '24LZR','24MWT','24MWU','24MXA','24MXV','24MYV',
# #             # '24MZS','24MZT','24MZU','24MZV','24LWR','24LXR','24LYQ','24LYR',
# #             # '24MWS','24MYS','24MYT','24LWP','24LVL','24LVN',
#                 # '24MXS','24MXT','24MXU','24MYU',
# #             # '24LVP','24LWM','24LWN','24LWQ','24LXN','24LXP','24LXQ','24LYP',
# #     #         '24LVM','24LWQ','24LVQ',
# #                 '25MBQ'
#         # ],
#     '95' : [
# #             # '23LRL','24LTR','24MTS','24MTT','24MUS','24MUT','24MUU','24MUV',
# #             # '24MUA','24MUB','24MVA','24MVB',
#                 '24MVS', #'24MVT','24MVU',
#                 # '24LTP','24LUN','24MWA','24MWU',
# #             # '24MVV','24MWB','24MWS','24MWT','24MWV','24MXA',
# #             # '24MXT','24MXU','24MXV','23LQC','23LQD','23LQE','23LRE','23LRF',
# #             # '23LRJ','24LTQ','24LWR','24LTN','24LTQ','24LVQ','24LTM',
# #             # '24LVR','24LUR','23LQF','23LRD','23LRG','23LRH','24LTJ','24LTN',
# #             # '24LTK','24LTL','24LUM','24LUJ','24LUK','24LUL','24LVL','24LVM',
# #             # '24LVN','24LWP','24LWQ','24LUP','24LVP','24LUQ','24MUC'      
#         ],
#     '138' : [
#         #     '23LNK','23MPP',
#             # '23LPL','23LQL','23MRR',
#             '23MQM','23MQN','23MPM',
#         #     '23MQP','23MQQ','23MQR','23MQS','23MRP',
#             # '23MRM','23MRN','23MRQ',
#             # '24LTR','24MTS','24MUS',
#             # '23MRS','24MTA','24MTB','24MTT','24MTU','24MTV',
#             # '24MUA','24MUB','24MUT','24MUU','24MUV','24MVB','23KPB','23LMC',
#             # '23LNC','23LNF','23LNG','23LNH','23LQE',
#             # '23LND','23LNE','23LNJ',
#             # '23LPD','23LPE','23LPF','23LPG','23LPH','23LPJ','23LPK','23LQG',
#             # '23LQH','23LQJ','23LQK','23LRH','23LRJ','23LRK','23LRL','24LTM',
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
