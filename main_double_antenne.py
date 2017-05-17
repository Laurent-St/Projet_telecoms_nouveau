from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *

gain=1.6981
xmax=100
ymax=100
model=Model(xmax,ymax)
cat=2
#a est le facteur multiplicatif par rapport à la dimension 250x250, pour la catégorie 1
a= 1
model.setwalls(xmax,ymax,cat,a)

facteur_echelle=100/12 #A ACCORDER AVEC CELUI DANS LA CLASSE RAY

txx1=20
txy1=10
txx2=20
txy2=50

#main double antenne
tx1=Antenna(gain,txx1,txy1)
tx1.setpower_emission(0.1)

tx2=Antenna(gain,txx2,txy2)
tx2.setpower_emission(0.1)

rxx=80
rxy=10
rx=Antenna(gain,rxx,rxy)

onde_dir_1=onde_directe((txx1,txy1),(rxx,rxy),model.getwalls())
onde_dir_2=onde_directe((txx2,txy2),(rxx,rxy),model.getwalls())

elec1=onde_dir_1.get_elec_field(tx1)
elec2=onde_dir_1.get_elec_field(tx2)
elec3=elec1+elec2
ampli_elec3=np.abs(elec3)



