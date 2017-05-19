# main
from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *

#taille de la carte et initialisation des murs
xmax=500
ymax=500
model=Model(xmax,ymax)
cat=1
#a est le facteur multiplicatif par rapport à la dimension 250x250, pour la catégorie 1
a= 2
model.setwalls(xmax,ymax, cat,a)

facteur_echelle=500*a/12 #A ACCORDER AVEC CELUI DANS LA CLASSE RAY

#ATTENTION ici tx et rx désignent l'émetteur et le récepteur, mais
#dans la fct reflexion ils désignent le tuple contenant la position

"""Calcul sur toute une zone"""
#ATTENTION NE PAS METTRE RECEPTEUR DANS LES MURS

gain=1.6981
txx=450
txy=50
raystot=[]
tx=Antenna(gain,txx,txy)
#tx2=Antenna(gain,50,30)
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
#tx2.setpower_emission(0.1)
PRX=0 #puissance moyenne
#lsPRX=[[0]*xmax]*ymax
lsPRX=np.zeros((ymax+1,xmax+1)) #np.zeros((lignes,colonnes))
ls_debit_binaire=np.zeros((ymax+1,xmax+1))
#lsPRX est la liste des puissances EN DBM
#MAIS ATTENTION il faut calculer le log après avoir sommé toutes les contributions,
#et pas sommer des logarithmes!!!

point_P_min=[0,0] #pour rechercher le point à puissance minimale
for i in range(0,ymax): #i: dimension y
#for i in np.arange(0.1,ymax,0.1):
    print('i=',i)
    for j in range(0,xmax): #j: dimension x
    #for j in np.arange(0.1,xmax,0.1):
        #print('j=',j)
        if isinwall(model.getwalls(),j,i) == False:
            rx=Antenna(gain,j,i) #on crée une antenne réceptrice en chaque point
            rays=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
            #rays2=reflexion((tx2.x,tx2.y),(rx.x,rx.y),model.getwalls())
            #rays.extend(rays2)
            rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
            #rays2_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx2.x,tx2.y),(rx.x,rx.y))
            rays.extend(rays_diff)
            #rays.extend(rays2_diff)
            ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
            #ray2_direct=onde_directe((tx2.x,tx2.y),(rx.x,rx.y),model.getwalls())
            #print('distance onde directe=',ray_direct.dis)
            #if i==1 and j==txx:
                #print('puissance onde directe=',ray_direct.get_PRX_individuelle(tx))
                
            #print('ray_direct.dis=',ray_direct.dis)
            lsPRX[i][j]=ray_direct.get_PRX_individuelle(tx) #puissance recue juste au point considéré
            #lsPRX[i][j]+=ray2_direct.get_PRX_individuelle(tx)
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
            if lsPRX[i][j]<lsPRX[point_P_min[1]][point_P_min[0]]:
                point_P_min=[j,i]
            ls_debit_binaire[i][j]=interpolation(lsPRX[i][j])

#Cas où le récepteur est sur l'émetteur et donc distance nulle, mène à des résultats incohérents: on prend la moyenne des points autour
lsPRX[txy][txx]=(lsPRX[txy-1][txx-1]+lsPRX[txy-1][txx]+lsPRX[txy-1][txx+1]+lsPRX[txy][txx-1]+lsPRX[txy][txx+1]+lsPRX[txy+1][txx-1]+lsPRX[txy+1][txx]+lsPRX[txy+1][txx+1])/8            
ls_debit_binaire[txy][txx]=interpolation(lsPRX[txy][txx])
#print(lsPRX)

#point à puissance minimale
point_P_min=(point_P_min[0],point_P_min[1])
P_min=lsPRX[point_P_min[1]][point_P_min[0]]
print('Point à puissance minimale=',point_P_min)
print('Puissance minimale=',P_min)


#nbre_pts=xmax*ymax
#PRX=PRX/nbre_pts
#PRX_dBm=10*np.log(PRX/0.001)

#AFFICHAGE PUISSANCE:
GUI(model.getwalls(),xmax,ymax,raystot,lsPRX,2)
#AFFICHAGE DEBIT BINAIRE:
#GUI(model.getwalls(),xmax,ymax,raystot,ls_debit_binaire,3)


"""Calcul juste en un point
gain=1.6981
txx=50
txy=50
rxx=151
rxy=151
tx=Antenna(gain,txx,txy)
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
rx=Antenna(gain,rxx,rxy)
raystot=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
raystot.extend(rays_diff)
ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
raystot.append(ray_direct)


#calcul de la puissance
PRX=0
##for ray in raystot:
##    if ray.dis != None:
##        PRX=PRX+ray.get_PRX_individuelle(tx)

##PRX_dBm=10*np.log(PRX/0.001)
##print('Puissance moyenne=',PRX)
##print('Puissance moyenne[dBm]=',PRX_dBm)


for ray in raystot:
    if ray.dis != None:
        PRX+=ray.get_PRX_individuelle(tx)

PRX=10*np.log(PRX/0.001) #on passe en dBm seulement à la fin
print(PRX)

#print(lsPRX)
GUI(model.getwalls(),xmax,ymax,raystot,PRX,1) #le 1 est pour juste afficher les rayons
"""

