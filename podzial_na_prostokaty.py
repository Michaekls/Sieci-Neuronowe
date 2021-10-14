# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:21:59 2021

@author: m_war
"""
import random as rn
import numpy as np

def mnoznik(yy):
    return yy[0]*yy[1]

def podzial_na_dwa(k_wymiary,l,p,k):
    losowa_i=rn.randint(0,l-1)
    losowa_j=rn.randint(0,p-1)
    losowa_gora_dol = rn.randint(0,1)

    j=-1

    while True:
        j+=1

        if losowa_i>k_wymiary[j][0] and losowa_i<k_wymiary[j][1] and losowa_j>k_wymiary[j][2] and losowa_j<k_wymiary[j][3]:
            k_dzielimy=j
            break
        elif losowa_i==k_wymiary[j][0] or losowa_i==k_wymiary[j][1]:
            if losowa_j>k_wymiary[j][2] and losowa_j<k_wymiary[j][3]:   #na rogach prostokątu
                #losowa_gora_dol=0
                if (losowa_i == k_wymiary[j][1] and losowa_gora_dol==1) or (losowa_i == k_wymiary[j][0] and losowa_gora_dol==1):
                    losowa_gora_dol=0

                k_dzielimy=j
                break

        elif losowa_j==k_wymiary[j][2] or losowa_j == k_wymiary[j][3]:
            if losowa_i>k_wymiary[j][0] and losowa_i<k_wymiary[j][1]:
                
                #losowa_gora_dol=1
                if (losowa_j==k_wymiary[j][3] and losowa_gora_dol==0) or (losowa_j==k_wymiary[j][2] and losowa_gora_dol==0):
                    losowa_gora_dol=1

                k_dzielimy=j
                break

        if j==len(k_wymiary)-1:
            j = -1
            losowa_i=rn.randint(0,l-1)
            losowa_j=rn.randint(0,p-1)
            losowa_gora_dol = rn.randint(0,1)

    return k_dzielimy,losowa_gora_dol,losowa_i,losowa_j

def podzial_prostokaty(n,l,p):
    k=[]
    k_wymiary=[]
    prostokat=np.zeros([l,p])
    prostokat[0,:]=1
    prostokat[l-1,:]=1
    prostokat[:,0]=1
    prostokat[:,p-1]=1
    k.append((l,p))
    k_wymiary.append((0,l-1,0,p-1))
    for i in range(n-1):
        
        k_dzielimy, losowa_gora_dol,losowa_i,losowa_j = podzial_na_dwa(k_wymiary,l,p,k)                    

        dol=k_wymiary[k_dzielimy][0]
        gora = k_wymiary[k_dzielimy][1]
        lewo = k_wymiary[k_dzielimy][2]
        prawo = k_wymiary[k_dzielimy][3]

        if losowa_gora_dol==0:
            prostokat[k_wymiary[k_dzielimy][0]:k_wymiary[k_dzielimy][1],losowa_j]=1
            prostokat[k_wymiary[k_dzielimy][0]:k_wymiary[k_dzielimy][1],losowa_j+1]=1
            del k_wymiary[k_dzielimy]
            k_wymiary.append((dol,gora,lewo,losowa_j))
            k_wymiary.append((dol,gora,losowa_j+1,prawo))
            
        else:
            prostokat[losowa_i,k_wymiary[k_dzielimy][2]:k_wymiary[k_dzielimy][3]]=1
            prostokat[losowa_i+1,k_wymiary[k_dzielimy][2]:k_wymiary[k_dzielimy][3]]=1
            del k_wymiary[k_dzielimy]
            k_wymiary.append((dol,losowa_i,lewo,prawo))
            k_wymiary.append((losowa_i+1,gora,lewo,prawo))
        ############################################

    k=[]
    for prostokat2 in k_wymiary:
        k.append([prostokat2[1]-prostokat2[0]+1,prostokat2[3]-prostokat2[2]+1])

    k=sorted(k,key=mnoznik,reverse=True)
    # print(prostokat)
    return k


################przyklad użycia
# k = podzial_prostokaty(150,50,50)
# print(k)
# suma=0
# for i in k:
#     suma+=i[0]*i[1]
# print(suma)
