
#Fonction lançant la détection de mur


from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_onde_directe import *
from diffraction import *
from random import randint

#taille de la carte et initialisation des murs, pour l'étage normal
gain=1
xmax=200
ymax=200
model=Model(xmax,ymax)
cat=1
model.setwalls(xmax,ymax, cat)
walls = model.getwalls()
#liste vide des intersections
intersec_pts=[]


#on crée un émetteur au milieu de la map
i=1

for j in range(1,xmax): #j: dimension 
        print(j)
        if isinwall(model.getwalls(),j,i) == False:
            tx=Antenna(gain,j,i) #on crée une antenne émettrice en chaque point au milieu de la map
            #Pour chaque position de l'antenne émettrice, on trace un segment vertical vers le haut et un autre vers le bas
            #Ensuite, on calcule les intersections potentielles avec tous les murs, que l'on ajoute à une liste
            for wall in walls:
                if segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
                    intersec_pts.append(segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
                elif segment_intersec([(tx.x,tx.y),(tx.x,ymax)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
                    intersec_pts.append(segment_intersec([(tx.x,tx.y),(tx.x,ymax)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))


#taille de la carte et initialisation des murs, pour l'étage normal et un mur placé au hasard dedans
cat=7
model.setwalls(xmax,ymax, cat)


#ajour du mur au hasard ici
#on place un mur au hasard de longueur 5 unités sans qu'il n'ait d'intersection avec les autres murs

inter = True
while(inter == True)  : 
    x1 = randint(1,498)
    y1 = randint(1,498)
    x2 = x1+5
    y2 = y1
    for wall in walls:
       if(segment_intersec([(x1,y1),(x2,y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None):
            inter == True
       else:
            inter == False
            

#on ajoute le mur au modèle - matériau au hasard
walls.append(x1,x2,y1,y2,1)



i=ymax/2

for j in range(0,xmax): #j: dimension x
        tx=Antenna(gain,j,i) #on crée une antenne émettrice en chaque point au milieu de la map
        #Pour chaque position de l'antenne émettrice, on trace un segment vertical vers le haut et un autre vers le bas
        #Ensuite, on calcule les intersections potentielles avec tous les murs, que l'on ajoute à une liste
        for wall in walls:
            if segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
                #on vérifie si le point d'intersection se trouve déjà dans la liste initiale
                res = True
                for intersec in intersec_pts:
                    if (intersec == segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])):
                        intersec_pts.remove(intersec)
                        res = False
                if res == True:
                    intersec_pts.append(segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
                    
                        
            elif segment_intersec([(tx.x,tx.y),(tx.x,ymax)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
                res1 = True
                for intersec in intersec_pts:
                    if (intersec == segment_intersec([(tx.x,tx.y),(tx.x,0)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])):
                        intersec_pts.remove(intersec)
                        res1 = False
                if res1 == True:
                    intersec_pts.append(segment_intersec([(tx.x,tx.y),(tx.x,ymax)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
                    


                    
                



