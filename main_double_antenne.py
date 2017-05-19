from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *

gain=1.6981
xmax=150
ymax=150
model=Model(xmax,ymax)
cat=2
#a est le facteur multiplicatif par rapport à la dimension 250x250, pour la catégorie 1
a= 1
model.setwalls(xmax,ymax,cat,a)

facteur_echelle=1 #A ACCORDER AVEC CELUI DANS LA CLASSE RAY

txx1=5
txy1=100
txx2=5
txy2=100+2

#main double antenne
tx1=Antenna(gain,txx1,txy1)
tx1.setpower_emission(0.1)

tx2=Antenna(gain,txx2,txy2)
tx2.setpower_emission(0.1)

rxx=txx1+100*np.sin(np.pi*70/180)
rxy=txy1-100*np.cos(np.pi*70/180)
rx=Antenna(gain,rxx,rxy)

onde_dir_1=onde_directe((txx1,txy1),(rxx,rxy),model.getwalls())
onde_dir_2=onde_directe((txx2,txy2),(rxx,rxy),model.getwalls())

elec1=onde_dir_1.get_elec_field(tx1)
elec2=onde_dir_1.get_elec_field(tx2)
elec3=elec1+elec2
ampli_elec3=np.abs(elec3)
print(ampli_elec3)

raystot=[]
raystot.append(onde_dir_1)
raystot.append(onde_dir_2)
lsPRX=[]

print(raystot)
GUI(model.getwalls(),xmax,ymax,raystot,lsPRX,1)



