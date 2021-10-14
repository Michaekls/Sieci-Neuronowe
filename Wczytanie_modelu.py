# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:26:45 2021

@author: m_war
"""
import csv
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy
 
model = tf.keras.models.load_model("pol_model_k6_PoPr_alexnet.h5",compile=False)

#model.compile()

_shape=64

dane=[]
wyjscie=[]    
def odczyt_z_pliku(nr):
    ilosc_1=0
    path=r'D:\\0pm michal\\pol\\dane_k6_PoPr_wczytanie\\dane_wejsciowe'+nr+'.csv'
    with open(path, 'r') as csvfile:
        # inicjujemy *zapisywacz*
        csvreader = csv.reader(csvfile)
        for wiersz in csvreader:
            w=[]
            for kolumna in wiersz:
                w.append(float(kolumna))
            w=np.array(w)
            w=w.reshape(_shape,_shape,1)
            dane.append(w)
        
            
    path=r'D:\\0pm michal\\pol\\dane_k6_PoPr_wczytanie\\dane_wyjsciowe'+nr+'.csv'
    with open(path, 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)
        for wiersz in csvreader:
            for kolumna in wiersz:
                wyjscie.append(float(kolumna))
            if float(kolumna)==1:
                ilosc_1 +=1
    return dane,wyjscie,ilosc_1




####
#### Zobaczenie która instancja prostokątów zwróci 1 przy daniu jej do sieci 
#### Podgląd dla mnie do sprawdzenia jak się mniej więcej pokrywa z rzeczywistocią
#### to znaczy z danymi zapisanymi w excelu


ilosc_11=0
for i in range(1):
    dane,wyjscie,ilosc_1=odczyt_z_pliku(str(i))
    ilosc_11 +=ilosc_1

dane=np.array(dane)
ynew2 = model.predict(dane)
print(ynew2)
counter=0
gdzie=0
l=[]
for i in range(1*770): #182  770   5740
    if gdzie ==5740:
        gdzie=0
    gdzie+=1

    ynew = model.predict(np.reshape(dane[i],(1,_shape,_shape,1)))
    
    print(ynew) 
    if ynew[0][0]>0.5:
        print(1)

    if ynew[0][1]>0.5:
        counter +=1
        print(gdzie,"")
        l.append(gdzie)
        print('Zgadza się')

    if i % 100 ==0:
        print(i)

