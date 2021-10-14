
import csv
import numpy as np

def odczyt_z_pliku(nr,_k,_shape=64,dane=[],wyjscie=[]):

    path=r'D:\\0pm michal\\pol\\dane_k'+_k+'_PoPr\\dane_wejsciowe'+nr+'.csv'
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
            
    path=r'D:\\0pm michal\\pol\\dane_k'+_k+'_PoPr\\dane_wyjsciowe'+nr+'.csv'
    with open(path, 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)
        for wiersz in csvreader:
            for kolumna in wiersz:
                wyjscie.append(float(kolumna))
    return dane,wyjscie



def odczyt_z_pliku2(nr,_k,_shape,dane,wyjscie):

    path=r'D:\\0pm michal\\pol\\dane_k'+_k+'_PoPr_sprawdzenie\\dane_wejsciowe'+nr+'.csv'
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
            
    path=r'D:\\0pm michal\\pol\\dane_k'+_k+'_PoPr_sprawdzenie\\dane_wyjsciowe'+nr+'.csv'
    with open(path, 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)
        for wiersz in csvreader:
            for kolumna in wiersz:
                wyjscie.append(float(kolumna))
    return dane,wyjscie