# -*- coding: utf-8 -*-


import numpy as np
import math

# bierzemy prostokat


def dane_wejsciowe(tab,k):
    
    szerokosc_k=64
    
    max1=int(max(tab[0]))
    max2=int(max(tab[1]))

    kwadrat = np.zeros([max1,max2])
    
    # tab_k gdzie się prosokąt zaczyna, a tab gdzie się kończy
    tab_k=tab-np.array(k).transpose()
    tab=tab.astype(np.int)
    tab_k=tab_k.astype(np.int)

    for i in range(len(k)):                
        kwadrat[tab_k[0][i]:tab[0][i],tab_k[1][i]:tab[1][i]]=1
        
    kwadrat2=np.zeros([szerokosc_k,szerokosc_k])
    kwadrat2pomocniczy=np.zeros([szerokosc_k,szerokosc_k])
    
    #pszekształcamy kwadrat na 64x64
    
    #Jak mamy kwadrat mniejszy niz 64x64
    if max1<=szerokosc_k and max2<=szerokosc_k:
        for i in range(szerokosc_k):
            for j in range(szerokosc_k):            
                wsp11=math.floor(i*max1/szerokosc_k)
                wsp22=math.floor(j*max2/szerokosc_k)

                kwadrat2[i,j]=kwadrat[wsp11,wsp22]
                
    elif max1==szerokosc_k and max2==szerokosc_k:
        kwadrat2=kwadrat
    
    #jak mamy kwadrat wiekszy niz 64x64
    elif max1>szerokosc_k and max2>szerokosc_k:
        
        for i in range(max1):
            for j in range(max2):
                
                wsp11=math.floor(i*szerokosc_k/max1)
                wsp22=math.floor(j*szerokosc_k/max2)
                            

                
                kwadrat2[wsp11,wsp22]=kwadrat2[wsp11,wsp22]+kwadrat[i,j]
                kwadrat2pomocniczy[wsp11,wsp22]+=1
                            
        kwadrat2pomocniczy[kwadrat2pomocniczy==0]=1
        kwadrat2=kwadrat2/kwadrat2pomocniczy
    
    elif max1>szerokosc_k and max2<=szerokosc_k:
        #print(max1,max2,szerokosc_k)
        for i in range(max1):
            for j in range(szerokosc_k):
                    wsp11=math.floor(i*szerokosc_k/max1)
                    
                    #wsp22=math.floor(j*max2/szerokosc_k)
                    
                    jj=math.floor(j*max2/szerokosc_k)
                    
                    kwadrat2[wsp11,j]=kwadrat2[wsp11,j]+kwadrat[i,jj]
                    kwadrat2pomocniczy[wsp11,j]+=1
                        
        kwadrat2pomocniczy[kwadrat2pomocniczy==0]=1
        kwadrat2=kwadrat2/kwadrat2pomocniczy
                
    elif max1<=szerokosc_k and max2>szerokosc_k:

        for i in range(szerokosc_k):
            for j in range(max2):
                    
                    wsp22=math.floor(j*szerokosc_k/max2)
                    
                    ii=math.floor(i*max1/szerokosc_k)
                    
                    kwadrat2[i,wsp22]=kwadrat2[i,wsp22]+kwadrat[ii,j]
                    kwadrat2pomocniczy[i,wsp22]+=1
                        
        kwadrat2pomocniczy[kwadrat2pomocniczy==0]=1
        kwadrat2=kwadrat2/kwadrat2pomocniczy

    return kwadrat2
