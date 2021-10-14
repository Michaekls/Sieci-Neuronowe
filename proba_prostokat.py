import numpy as np
import matplotlib.pyplot as plt
import random as rn
from tabelka_prostokat import *
from ukladanie import*
from dane_wejsciowe import*
import copy
import csv


shape=64

# Wysowanie ułożenie prostokątów
def rysuj(wsp,wsp2):
    for i in range(len(k)):
        
        #wyznaczamy 4 linie prostokątu i srodek
        
        x1=(wsp[0][i],wsp2[0][i])
        y1=(wsp[1][i],wsp[1][i])
        
        x2=(wsp[0][i],wsp[0][i])
        y2=(wsp[1][i],wsp2[1][i])
        
        x3=(wsp2[0][i],wsp2[0][i])
        y3=(wsp[1][i],wsp2[1][i])
        
        x4=(wsp[0][i],wsp2[0][i])
        y4=(wsp2[1][i],wsp2[1][i])
        
        x5=(wsp[0][i]+wsp2[0][i])/2-0.2
        y5=(wsp[1][i]+wsp2[1][i])/2-0.2

        plt.plot(x1,y1,'b')
        plt.plot(x2,y2,'b')
        plt.plot(x3,y3,'b')
        plt.plot(x4,y4,'b')
        numer=i+1
        plt.text(x5,y5,numer, fontsize=13)
        
    plt.xlim(0)
    plt.ylim(0)
    plt.grid()
    #plt.show()



#k=[[18,18],[15,15],[14,14],[10,10],[9,9],[8,8],[7,7],[4,4],[1,1]]        
k=[[11,8],[12,4],[10,6],[8,5],[6,4],[5,4],[4,1],[1,2]]
#k=k.sort(reverse=True)

m=1000
def SP_dla_ostatniego(SPnaj,k,tab_i,Pole_od_i):
    wyjscie_sieci=[]   # 0 lub 1
    kwadrat_wyjsciowe=[]
    SPnaj2=SPnaj

    for ii in range(1,len(SPnaj)+1):

        if ii<len(SPnaj2):
            SP_bez_ostatniego=SPnaj2[-ii-1]
        else:
            SP_bez_ostatniego=[[],[]]  #jak będziemy pierwszy kwadrat ukadać
            
        SPnaj=SP_bez_ostatniego

        i=len(SP_bez_ostatniego[0])+1
        
        for j in range(i):
            
            SPnaj[0].insert(i-j-1,i)   
            for jj in range(i):
                SPnaj[1].insert(i-jj-1,i)
                
                for obrot in range(2):
                    if obrot==0:
                        k2=np.array(k[0:i])
                    else:
                        k2=np.array(k[0:i])
                        k2[-1][0],k2[-1][1] = k2[-1][1],k2[-1][0]
                    

                    tab=tabelka_prostokat(k2,SPnaj)+np.array(k2).transpose()
                    
                    ostatni_z_sp=[tab[0][-1],tab[1][-1]] #ostatni z uciętej tej tabeli

                    tab_ii=[tab_i[-ii][0][-1],tab_i[-ii][1][-1]] # odpowiedni z prawidlowej tabeli
                    
                    #wyjscie sieci na podstawie Pola##########################3
                    max11=max(tab[0])
                    max22=max(tab[1])
                    Polek=0
                    for w_k in k2:
                        Polek += w_k[0]*w_k[1]
                  
                    #Pole_do_porownania = abs(max11*max22/Polek)
                    Pole_do_porownania = max11*max22
                    
                    #########################################################
                                        
                    # porównojemy oby dwa i jesli jest w tym samym miejscu to wyjscie_sieci =1
                    # porównujemy gdzie jest umieszczony prawy górny róg prostokątu a nie lewy dolny,
                    # więc jest załotwione odwracanie prostokąta

                    #if Pole_do_porownania == Pole_od_i[-ii]:
                    if tab_ii==ostatni_z_sp:    #pol
                        wyjscie_sieci.append(1)
                    else:
                        wyjscie_sieci.append(0 )
                    
                    
                    #tworzymy dane_wejsciowe
                    kwadrat_wyjsciowe_pom=dane_wejsciowe(tab,k2)
                    
                    #aby kwadrat był do zapisania w jednej linii
                    kwadrat_wyjsciowe_pom=np.reshape(kwadrat_wyjsciowe_pom,(1,shape*shape))
                    kwadrat_wyjsciowe.append(kwadrat_wyjsciowe_pom)
                    
                    #jakby był kwadrat   to tylko raz
                    if  k2[-1][0]==k2[-1][1]:
                        continue
                SPnaj[1].remove(i)
            SPnaj[0].remove(i)
        #print(ii)
    wyjscie_sieci = np.reshape(wyjscie_sieci,(1,len(wyjscie_sieci)))
    return wyjscie_sieci,kwadrat_wyjsciowe

def dokladanieSP(k):
    
    SPnaj=[[],[]]       #aby operowac na SP (dodawac, przekladac)
    nowa=[[],[]]
    najlepsza=[[],[]]    #najlepsze ułożenie tabelka
    SP_i=[]             # najlepsze SP dla danego i
    tab_i=[]            #najlepsze ulozenie dla danego i
    global m
    Pole_od_i=[]        # Najlepsze pole SP dla nadego i
    for i in range(1,len(k)+1):
        m=1000000  # zmienna #Pole
        nowe_k=0   # czy zmieniamy kwadrat z poziomu w pion
        
        SPnaj=copy.deepcopy(nowa)
        #SPnaj=nowa[:,:]
        
        for j in range(i):
            SPnaj[0].insert(i-j-1,i)
            for jj in range(i):
                
                SPnaj[1].insert(i-jj-1,i)
                for obrot in range(2):
                    if obrot==0:
                        k2=np.array(k[0:i])

                    else:
                        #odwracamy prostokąt do porownania
                        k[i-1][0],k[i-1][1] = k[i-1][1],k[i-1][0]
                        k2=np.array(k[0:i])
                    
                    
                    tab=tabelka_prostokat(k2,SPnaj)+(np.array(k2)).transpose()
    ######################### wybór w jaki sposób układa ######################    
                   #nowe_k -> czy prostokąt jest odwrocony czy w normalnej formie
                    
                    #nowa,najlepsza,m,nowe_k=pole(tab,m,SPnaj,nowa,najlepsza,k2,obrot,nowe_k)
                    
                    #nowa,najlepsza,m,nowe_k=PoPw(tab,m,SPnaj,nowa,najlepsza,k2,obrot,nowe_k)
                    
                    #nowa,najlepsza,m=PoPk(tab,m,SPnaj,nowa,najlepsza,k2)
                    
                    nowa,najlepsza,m,nowe_k=pole_prawidlowe(tab,m,SPnaj,nowa,najlepsza,k2,obrot,nowe_k)
                                        
                    
                    #wracamy po porownaniu do normalnej formy
                    if obrot==1:
                         k[i-1][0],k[i-1][1] = k[i-1][1],k[i-1][0]
                         
                SPnaj[1].remove(i)
            SPnaj[0].remove(i)
            
        SP_i.append(nowa)
        tab_i.append(najlepsza)
        Pole_od_i.append(m)
        #jesli w najlepszym jest prostokat odwrocony to go odwracamy
        if nowe_k==1:
            k[i-1][0],k[i-1][1] = k[i-1][1],k[i-1][0]
                   

    [wyjscie_sieci, kwadrat_wyjsciowe] = SP_dla_ostatniego(SP_i,k,tab_i,Pole_od_i)
    wejscie_sieci=kwadrat_wyjsciowe
    

    return wyjscie_sieci, wejscie_sieci
   

print("koniec")
######################aby narysować przykład ze strzałkami ########################
###################### Rysunek wykorzystany w pracy        #########################
def rysuj_strzalki(wsp,wsp2):  
    plt.annotate('', xy=((wsp[0][0]+wsp2[0][0])/2,(wsp[1][0]+wsp2[1][0])/2+0.3), 
                  xytext=((wsp[0][1]+wsp2[0][1])/2,(wsp[1][1]+wsp2[1][1])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][1]+wsp2[0][1])/2,(wsp[1][1]+wsp2[1][1])/2+0.3), 
              xytext=((wsp[0][4]+wsp2[0][4])/2,(wsp[1][4]+wsp2[1][4])/2-0.2),
           arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
          )
    plt.annotate('', xy=((wsp[0][1]+wsp2[0][1])/2,(wsp[1][1]+wsp2[1][1])/2+0.3), 
                  xytext=((wsp[0][5]+wsp2[0][5])/2,(wsp[1][5]+wsp2[1][5])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.3), 
                  xytext=((wsp[0][1]+wsp2[0][1])/2,(wsp[1][1]+wsp2[1][1])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.3), 
                  xytext=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )  
    plt.annotate('', xy=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.3), 
                  xytext=((wsp[0][6]+wsp2[0][6])/2,(wsp[1][6]+wsp2[1][6])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][6]+wsp2[0][6])/2,(wsp[1][6]+wsp2[1][6])/2+0.3), 
                  xytext=((wsp[0][7]+wsp2[0][7])/2,(wsp[1][7]+wsp2[1][7])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=1),
              )
    # plt.annotate('', xy=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.3), 
    #               xytext=((wsp[0][5]+wsp2[0][5])/2,(wsp[1][5]+wsp2[1][5])/2-0.2),
    #            arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
    #           )
    plt.annotate('', xy=((wsp[0][0]+wsp2[0][0])/2,(wsp[1][0]+wsp2[1][0])/2+0.3), 
                  xytext=((wsp[0][7]+wsp2[0][7])/2,(wsp[1][7]+wsp2[1][7])/2-0.2),
               arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=1),
              )
    
def rysuj_strzalki2(wsp,wsp2):  
    
    
    plt.annotate('', xy=((wsp[0][0]+wsp2[0][0])/2,(wsp[1][0]+wsp2[1][0])/2+0.15), 
                  xytext=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][4]+wsp2[0][4])/2,(wsp[1][4]+wsp2[1][4])/2+0.15), 
                  xytext=((wsp[0][5]+wsp2[0][5])/2,(wsp[1][5]+wsp2[1][5])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][5]+wsp2[0][5])/2,(wsp[1][5]+wsp2[1][5])/2+0.15), 
                  xytext=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][1]+wsp2[0][1])/2,(wsp[1][1]+wsp2[1][1])/2+0.15), 
                  xytext=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][0]+wsp2[0][0])/2,(wsp[1][0]+wsp2[1][0])/2+0.15), 
                  xytext=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2+0.15), 
                  xytext=((wsp[0][7]+wsp2[0][7])/2,(wsp[1][7]+wsp2[1][7])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][2]+wsp2[0][2])/2,(wsp[1][2]+wsp2[1][2])/2+0.15), 
                  xytext=((wsp[0][6]+wsp2[0][6])/2,(wsp[1][6]+wsp2[1][6])/2+0.1),
              arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
              )
    plt.annotate('', xy=((wsp[0][4]+wsp2[0][4])/2,(wsp[1][4]+wsp2[1][4])/2+0.15), 
              xytext=((wsp[0][3]+wsp2[0][3])/2,(wsp[1][3]+wsp2[1][3])/2+0.1),
          arrowprops=dict(arrowstyle="<-", shrinkB=5,shrinkA=5),
          )
    
    plt.show()
#rysuj_strzalki(najlepsza-k2.transpose(),najlepsza)
#rysuj_strzalki2(najlepsza-k2.transpose(),najlepsza)