#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
#SCRIPT DE CLASSIFICACAO POR BACIA
#Produzido por Geodatin - Dados e Geoinformacao
#DISTRIBUIDO COM GPLv2
'''

import ee 
import gee
import sys


try:
  ee.Initialize()
  print('The Earth Engine package initialized successfully!')
except ee.EEException as e:
  print('The Earth Engine package failed to initialize!')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
sys.setrecursionlimit(1000000000)

relatorios = open("registros/relatorioTaskXContas.txt", 'a+')

param = {
    'unicaconta': True,
    'numeroTask': 280,
    'numeroLimit': 12,
    'conta' : {
        '0': 'caatinga01',
        '1': 'caatinga02',
        '2': 'caatinga03',
        '3': 'caatinga04',
        '4': 'caatinga05',        
        '5': 'solkan1201',
        '6': 'diegoGmail',
        '7': 'rodrigo',
        '8': 'Rafael',
        '9': 'solkanCengine',
        '10': 'Nerivaldo',
        '11': 'diegoUEFS',
        # '12': 'simao',
        # '13': 'ellen',
        # '14': 'vinicius',
        # '15': 'bruna',
        '16': 'superconta'
    }
}


def gerenciador(cont):    
    #=====================================
    # gerenciador de contas para controlar 
    # processos task no gee   
    #=====================================
    numberofChange = [kk for kk in param['conta'].keys()]
    print(cont)
    print(numberofChange)
    if str(cont) in numberofChange:
        
        gee.switch_user(param['conta'][str(cont)])
        gee.init()
        relatorios.write("Conta de: " + param['conta'][str(cont)] + '\n')

        tarefas = gee.tasks(
            n= param['numeroTask'],
            return_list= True)
        
        for lin in tarefas:            
            relatorios.write(str(lin) + '\n')
    
    elif cont > param['numeroLimit']:
        cont = 0
    
    cont += 1    
    return cont

if param['unicaconta'] == True:

    cont = 16
    cont = gerenciador(cont)
else:
    cont = 0
    for ii in range(0,15):        
        cont = gerenciador(cont)