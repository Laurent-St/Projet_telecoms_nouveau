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
debit_bin = 0 #debit binaire moyen
lsPRX=np.zeros((ymax+1,xmax+1)) #np.zeros((lignes,colonnes))
ls_debit_binaire=np.zeros((ymax+1,xmax+1))

#debit binaire moyen et position de l'émetteur correspondante
debit_bin_tx_pos =[]

#On crée une antenne, et on calcule la couverture de l'étage moyenne à chaque itération

for y in range(0,int(ymax*a)):
    print(y)
    for x in range(0,int(xmax*a)):
        
        if isinwall(model.getwalls(),x,y) == False:
            tx=Antenna(gain,x,y)
            tx.setpower_emission(0.1)
            txx = tx.x
            txy = tx.y

            for i in range(0,int(ymax*a)): #i: dimension y
                for j in range(0,int(xmax*a)): #j: dimension x

                    if isinwall(model.getwalls(),j,i) == False:
                        rx=Antenna(gain,j,i) #on crée une antenne réceptrice en chaque point
                        rays=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
                        rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
                        rays.extend(rays_diff)
                        ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())

                        lsPRX[i][j]=ray_direct.get_PRX_individuelle(tx) #puissance recue juste au point considéré
            
                        if dis_eucl((txx,txy),(j,i))/facteur_echelle >= 0.3: #diviser la distance par une valeur supérieure à 1 augmente la zone où on remplace par 0,001
                            
                            for ray in rays:
                                #raystot.append(ray)
                                if ray.dis != None:
                                        lsPRX[i][j]=lsPRX[i][j]+ray.get_PRX_individuelle(tx)
                                    
                                        
                        else:
                            lsPRX[i][j]=0.001 #pour négliger les points qui ne sont pas en champ lointain
                        
            
                        lsPRX[i][j]=10*np.log(lsPRX[i][j]/0.001) #on passe en dBm seulement à la fin
                        ls_debit_binaire[i][j]=interpolation(lsPRX[i][j])
                        debit_bin+=ls_debit_binaire[i][j]
                #Cas où le récepteur est sur l'émetteur et donc distance nulle, mène à des résultats incohérents: on prend la moyenne des points autour
                lsPRX[txy][txx]=(lsPRX[txy-1][txx-1]+lsPRX[txy-1][txx]+lsPRX[txy-1][txx+1]+lsPRX[txy][txx-1]+lsPRX[txy][txx+1]+lsPRX[txy+1][txx-1]+lsPRX[txy+1][txx]+lsPRX[txy+1][txx+1])/8            
                ls_debit_binaire[txy][txx]=interpolation(lsPRX[txy][txx])
            
                #tuple avec couverture en x et position de l'émetteur en y
            debit_bin_tx_pos.append((debit_bin,(x,y)))
            debit_bin=0
        
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