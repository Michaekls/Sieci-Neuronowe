# -*- coding: utf-8 -*-

#Sposoby układania prostokątów

import copy

def pole(tab,m,SPnaj,nowa,najlepsza,k,obrot,nowe_k):
    
    max1=max(tab[0])
    max2=max(tab[1])
    if max1+max2<m:
        m=max1+max2
        najlepsza=tab
        nowa=copy.deepcopy(SPnaj)
        nowe_k=obrot
    return nowa,najlepsza,m,nowe_k

def PoPw(tab,m,SPnaj,nowa,najlepsza,k,obrot,nowe_k):
    max1=max(tab[0])
    max2=max(tab[1])
    Polek=0
    for i in k:
        Polek += i[0]*i[1]
    if max1*max2/Polek<m:
        m=max1*max2-Polek
        najlepsza=tab
        nowa=copy.deepcopy(SPnaj)
        nowe_k=obrot
    return nowa,najlepsza,m,nowe_k

def PoPk(tab,m,SPnaj,nowa,najlepsza,k):
    max1=max(tab[0])
    max2=max(tab[1])
    Polek=0

    for i in k:
        Polek += i[0]*i[1]
    if max1*max2-Polek<m:
        m=max1*max2-Polek
        najlepsza=tab
        nowa=copy.deepcopy(SPnaj)
    return nowa,najlepsza,m

def pole_prawidlowe(tab,m,SPnaj,nowa,najlepsza,k,obrot,nowe_k):
    
    max1=max(tab[0])
    max2=max(tab[1])
    if max1*max2<m:
        m=max1*max2
        najlepsza=tab
        nowa=copy.deepcopy(SPnaj)
        nowe_k=obrot
    return nowa,najlepsza,m,nowe_k