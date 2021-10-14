
import numpy as np


# k=[[40,30],[20,20],[20,10],[20,20],[20,20],[20,20]]
# SP=[[1,3,2,4,5,6],
#     [1,2,3,5,4,6]]

# Stworzenie tabeli w celu ustalenia najdłuższego wspólnego podciągu

def tabelka_prostokat(k,SP):
    tabela=np.zeros([len(k),len(k)])
    wsp=np.zeros([2,len(k)])
    for i in range(len(k)):
        dalej=0;
        zapamietaj=0;
        for j in range(len(k)):
            if i==0:
                if SP[0][i]==SP[1][j]:
                    dalej=1
                    zapamietaj=j;
                if dalej==0:
                    tabela[i][j]=tabela[i][j]
                else:
                    tabela[i][j]=tabela[i][j]+k[SP[0][i]-1][0]     
            else:
                if SP[0][i]==SP[1][j]:
                    dalej=1
                    zapamietaj=j;
                    tabela[i][j]=tabela[i-1][j]+k[SP[0][i]-1][0]  
                if dalej==0:
                    tabela[i][j]=tabela[i-1][j]
                else:
                    if tabela[i][j]<tabela[i][j-1]:
                        tabela[i][j]=tabela[i][j-1] 
                    if tabela[i][j]<tabela[i-1][j]:
                        tabela[i][j]=tabela[i-1][j] 
        if SP[0][i]==SP[1][0]:
            wsp[0][SP[0][i]-1]=0
        else:
            wsp[0,SP[0][i]-1]=tabela[i][zapamietaj-1]

    
    P=SP[1]
    P=P[::-1]
    SP=[SP[0],
        P]
    
    tabela=np.zeros([len(k),len(k)])
    for i in range(len(k)):
        dalej=0;
        zapamietaj=0;
        for j in range(len(k)):
            if i==0:
                if SP[0][i]==SP[1][j]:
                    dalej=1
                    zapamietaj=j;
                if dalej==0:
                    tabela[i][j]=tabela[i][j]
                else:
                    tabela[i][j]=tabela[i][j]+k[SP[0][i]-1][1]     
            else:
                if SP[0][i]==SP[1][j]:
                    dalej=1
                    zapamietaj=j;
                    tabela[i][j]=tabela[i-1][j]+k[SP[0][i]-1][1]  
                if dalej==0:
                    tabela[i][j]=tabela[i-1][j]
                else:
                    if tabela[i][j]<tabela[i][j-1]:
                        tabela[i][j]=tabela[i][j-1]
                    if tabela[i][j]<tabela[i-1][j]:
                        tabela[i][j]=tabela[i-1][j] 
        if SP[0][i]==SP[1][0]:
            wsp[1][SP[0][i]-1]=0
        else:
            wsp[1][SP[0][i]-1]=tabela[i][zapamietaj-1]

    return wsp
# tabelka_prostokat(k, SP)