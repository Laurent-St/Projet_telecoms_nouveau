from GUI import *
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *

# main_detector
xmax=250
ymax=250
a=1
facteur_echelle=250/12 #A ACCORDER AVEC CELUI DANS LA CLASSE RAY

#ATTENTION ici tx et rx désignent l'émetteur et le récepteur, mais
#dans la fct reflexion ils désignent le tuple contenant la position

gain=1.6981

model1=Model(xmax,ymax)
model2=Model(xmax,ymax)

cat1=7
cat2=1
model1.setwalls(xmax,ymax,cat1,1)
model2.setwalls(xmax,ymax,cat2,1)
#émetteur et récepteur bougeant simultanément en parallèle

k=0
intrus=False
while intrus==False and k<(ymax-1):
    k=k+1
    
    #émetteur et récepteur
    tx=Antenna(gain,1,k)
    rx=Antenna(gain,xmax-1,k)
    
    #avec mur en plus
    ray1,compteur1,ls_pos1=onde_directe_compteur((tx.x,tx.y),(rx.x,rx.y),model1.getwalls())

    #sans mur en plus
    ray2,compteur2,ls_pos2=onde_directe_compteur((tx.x,tx.y),(rx.x,rx.y),model2.getwalls())

    if compteur1 > compteur2:
        intrus=True
        res=list(set(ls_pos1)-set(ls_pos2))
        print('INTRUS DETECTE EN',res)

#print('Intrus=',intrus)
pos_intrus=(res[0][0],res[0][1])
GUI_detector(model2.getwalls(),xmax,ymax,pos_intrus)

            
    
