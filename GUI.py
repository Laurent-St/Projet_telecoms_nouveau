
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

from Wall import Wall

def GUI(walls,xmax,ymax,rays,lsPRX,plot_type):
    "L'origine des coordonnées (x=0,y=0) est en haut à gauche"
    "ATTENTION quand on accède à une matrice c'est colonnes puis lignes"
    "ATTENTION le index commencent en (0,0)"

    "Génère les murs de la maison d'Alexandre: xmax=500, ymax=998"
    "Chaque porte fait 83 éléments"

    "rx est un tuple avec le point en haut à gauche de la zone de réception"

    "Un 0 représente un élément sans rien, un 1 de la brique, 2 béton et 3 une cloison"

    #tracé des murs


    for wall in walls:
        if(wall.mat==1):
            x='black'
        elif (wall.mat==2):
            x='red'
        elif (wall.mat==3):
            x='blue'
        elif (wall.mat==4):
            x='green'
        plt.plot((wall.x1,wall.x2),(wall.y1,wall.y2),color=x,linewidth=3.0)

    plt.gca().invert_yaxis()

#### AFFICHAGE DES RAYONS #################################################

    if plot_type==1:
        for ray in rays:
            plt.plot((ray.x1,ray.x2),(ray.y1,ray.y2),color=ray.getcolor())

############################################################################

#### AFFICHAGE DE LA PUISSANCE #############################################
    if plot_type==2:
        cmap = plt.get_cmap('jet')
        plt.imshow(lsPRX, interpolation="nearest", cmap=cmap)
        cb = plt.colorbar()
        cb.set_label('Puissance reçue [dBm]')
#############################################################################
    plt.ion()
    plt.show()



##    for i in range(0,4):
##        for j in range(0,4):
##            rect=Rectangle(Point(rx[0]+i,rx[1]+j),Point(rx[0]+i+1,rx[1]+j+1))
##            puissance=ls_PRX_pt_ij[i+j]
##            #AFFICHER LA COULEUR EN FCT DE L'INTENSITE


##    while(1):
##        clickpoint = win.checkMouse()
##        if (clickpoint!=None):
##            print(clickpoint)







#hlines= lignes horizontales
#vlines= lignes verticales
