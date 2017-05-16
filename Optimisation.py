#Optimisation

from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *

#On effectue la recherche du debit binaire moyen max sur un étage de 25x25 par rapidité
xmax=250
ymax=250
model=Model(xmax,ymax)
cat=1
#a est le facteur multiplicatif par rapport à la dimension 250x250
a= 1/10
model.setwalls(xmax,ymax, cat,a)

facteur_echelle=(250*a)/12 #A ACCORDER AVEC CELUI DANS LA CLASSE RAY

gain=1.6981
raystot=[]
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
PRX=0 #puissance moyenne
debit_bin = 0 #debit binaire moyen
#lsPRX=[[0]*xmax]*ymax
lsPRX=np.zeros((ymax+1,xmax+1)) #np.zeros((lignes,colonnes))
ls_debit_binaire=np.zeros((ymax+1,xmax+1))
#lsPRX est la liste des puissances EN DBM
#MAIS ATTENTION il faut calculer le log après avoir sommé toutes les contributions,
#et pas sommer des logarithmes!!!


#debit binaire moyen et position de l'émetteur correspondante
debit_bin_tx_pos =[]

#On crée une antenne, et on calcule la couverture de l'étage moyenne à chaque itération

for y in range(0,int(ymax*a)):
    for x in range(0,int(xmax*a)):
        if isinwall(model.getwalls(),x,y) == False:
            tx=Antenna(gain,x,y)
            txx = tx.x
            txy = tx.y

            for i in range(0,int(ymax*a)): #i: dimension y
            #for i in np.arange(0.1,ymax,0.1):
                print('i=',i)
                for j in range(0,int(xmax*a)): #j: dimension x
                #for j in np.arange(0.1,xmax,0.1):
                    #print('j=',j)
                    if isinwall(model.getwalls(),j,i) == False:
                        rx=Antenna(gain,j,i) #on crée une antenne réceptrice en chaque point
                        rays=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
                        rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
                        rays.extend(rays_diff)
                        ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
                        #print('distance onde directe=',ray_direct.dis)
                        #if i==1 and j==txx:
                            #print('puissance onde directe=',ray_direct.get_PRX_individuelle(tx))
                            
                        #print('ray_direct.dis=',ray_direct.dis)
                        lsPRX[i][j]=ray_direct.get_PRX_individuelle(tx) #puissance recue juste au point considéré
            
                        #print('lsPRX[i][j]=',lsPRX[i][j])
                        #raystot.append(ray_direct)
                        if dis_eucl((txx,txy),(j,i))/facteur_echelle >= 0.3: #diviser la distance par une valeur supérieure à 1 augmente la zone où on remplace par 0,001
                            for ray in rays:
                                #raystot.append(ray)
                                if ray.dis != None:
                                        lsPRX[i][j]=lsPRX[i][j]+ray.get_PRX_individuelle(tx)
                                        
                        else:
                            lsPRX[i][j]=0.001 #pour négliger les points qui ne sont pas en champ lointain
                        
            
                        PRX=PRX+lsPRX[i][j]
                        lsPRX[i][j]=10*np.log(lsPRX[i][j]/0.001) #on passe en dBm seulement à la fin
                        ls_debit_binaire[i][j]=interpolation(lsPRX[i][j])
                        debit_bin+=ls_debit_binaire[i][j]
                #Cas où le récepteur est sur l'émetteur et donc distance nulle, mène à des résultats incohérents: on prend la moyenne des points autour
                lsPRX[txy][txx]=(lsPRX[txy-1][txx-1]+lsPRX[txy-1][txx]+lsPRX[txy-1][txx+1]+lsPRX[txy][txx-1]+lsPRX[txy][txx+1]+lsPRX[txy+1][txx-1]+lsPRX[txy+1][txx]+lsPRX[txy+1][txx+1])/8            
                ls_debit_binaire[txy][txx]=interpolation(lsPRX[txy][txx])
                
                nbre_pts=xmax*ymax 
                debit_bin_moy = debit_bin/nbre_pts
                #tuple avec couverture moyenne en x et position de l'émetteur en y
                debit_bin_tx_pos.append((debit_bin_moy,(x,y)))
        
 #ensuite on parcourt la liste pour obtenir le debit_bin_max et la position de l'émetteur associée
 
indice = 0
maxi = debit_bin_tx_pos[0][0]
for i in range(0,len(debit_bin_tx_pos)):
    if debit_bin_tx_pos[i][0]>maxi:
        maxi = debit_bin_tx_pos[i][0]
        indice = i

pos_x = debit_bin_tx_pos[indice][1][0] /facteur_echelle
pos_y = debit_bin_tx_pos[indice][1][1]/facteur_echelle
         
       
print("Voici le débit binaire moyen maximal et la position de l'émetteur associée en m:",(debit_bin_tx_pos[indice][0], (pos_x,pos_y)))