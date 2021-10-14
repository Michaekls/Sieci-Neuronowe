# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:07:57 2021

@author: m_war
"""


from podzial_na_prostokaty import *
from proba_prostokat import *
import random as rnd
import csv
import sys

def zapisz_do_pliku(kwadrat_wyjsciowe,wyjscie_sieci,nr):
    path=r'D:\0pm michal\pol\dane_k10_PoPr_wczytanie\dane_wejsciowe'+nr+'.csv'
    with open(path, 'w', encoding='utf-8',newline='') as csvfile:

        csvwriter = csv.writer(csvfile)
        for wiersz in kwadrat_wyjsciowe:
            for kolumna in wiersz:
                csvwriter.writerow(kolumna)
    path2=r'D:\0pm michal\pol\dane_k10_PoPr_wczytanie\dane_wyjsciowe'+nr+'.csv'    
    with open(path2, 'w', encoding='utf-8',newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\n')
        for wiersz in wyjscie_sieci:
                csvwriter.writerow(wiersz)
               

            

for i in range(2):
    print(i)
    k = podzial_prostokaty(rnd.randint(6,15),rnd.randint(20,40),rnd.randint(20,40))
    #k = podzial_prostokaty(10,20,20)
    
    wyjscie_sieci, wejscie_sieci= dokladanieSP(k)

    zapisz_do_pliku(wejscie_sieci, wyjscie_sieci,str(i))
    
    
    
    
    
    
    

