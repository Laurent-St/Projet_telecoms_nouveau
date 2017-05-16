import numpy as np
from Wall import *
from random import randint
from fctsmath import *

class Model:

    def __init__(self,xmax,ymax):
        self.xmax=xmax
        self.ymax=ymax
        #self.matrice=np.zeros([xmax_m,ymax_m])

        self.walls = [0]
        #listes de tuples reprenant les coins et aretes du probleme
        self.coins = []
        self.aretes = []

    def setwalls(self,xmax,ymax,cat,a):
        #a est un facteur multiplicatif pour les dimensions des murs
    #c'est la multiplication par rapport à des DIMENSIONS 250x250
        if cat==1:
            self.walls=[0]*16
            #1) contour de la maison (en briques)
                #pas de multiplication par a ici car ce sont les murs du contour, dictés par xmax et ymax
            self.walls[0]=Wall(0,xmax-1,0,0,1) #up
            self.coins.append((0,0))
            self.coins.append((xmax-1,0))
            self.walls[1]=Wall(0,xmax-1,ymax-1,ymax-1,1) #down
            self.coins.append((0,ymax-1))
            self.walls[2]=Wall(0,0,0,ymax-1,1) #left
            self.coins.append((xmax-1,ymax-1))
            self.walls[3]=Wall(xmax-1,xmax-1,0,ymax-1,1) #right
    
            #2) les murs en béton
            self.walls[4]=Wall(174*0.5*a,174*0.5*a,0,124*0.25*a,2)
            self.coins.append((174*0.5*a,0))
            self.aretes.append((174*0.5*a,124*0.25*a))
    
            self.walls[5]=Wall(174*0.5*a,174*0.5*a,207*0.25*a,457*0.25*a,2)
            self.aretes.append((174*0.5*a,207*0.25*a))
            self.aretes.append((174*0.5*a,457*0.25*a))
            self.walls[6]=Wall(174*0.5*a,174*0.5*a,540*0.25*a,749*0.25*a,2)
            self.aretes.append((174*0.5*a,540*0.25*a))
            self.walls[7]=Wall(299*0.5*a,299*0.5*a,0*a,124*0.25*a,2)
            self.aretes.append((299*0.5*a,124*0.25*a))
            self.walls[8]=Wall(299*0.5*a,299*0.5*a,207*0.25*a,540*0.25*a,2)
            self.aretes.append((299*0.5*a,207*0.25*a))
            self.walls[9]=Wall(299*0.5*a,299*0.5*a,431*0.25*a,623*0.25*a,2)
            self.aretes.append((299*0.5*a,623*0.25*a))
            self.walls[10]=Wall(0*a,224*0.5*a,831*0.25*a,831*0.25*a,2)
            self.coins.append((0*a,831*0.25*a))
            self.aretes.append((224*0.5*a,831*0.25*a))
            self.walls[11]=Wall(299*0.5*a,299*0.5*a,700*0.25*a, 831*0.25*a,2)
            self.aretes.append((299*0.5*a,700*0.25*a))
            self.aretes.append((299*0.5*a,831*0.25*a))
            self.walls[12]=Wall(0*a,175*0.5*a,749*0.25*a,749*0.25*a,2)
            self.coins.append((0*a,749*0.25*a))
            self.coins.append((175*0.5*a,749*0.25*a))
            self.coins.append((299*0.5*a,0*a))
    
            #3) les cloisons
            self.walls[13]=Wall(0*a,174*0.5*a,249*0.25*a,249*0.25*a,3)
            self.coins.append((0*a,249*0.25*a))
            self.coins.append((174*0.5*a,249*0.25*a))
            self.coins.append((299*0.5*a,499*0.25*a))
            self.coins.append((499*0.5*a,499*0.25*a))
            self.coins.append((299*0.5*a,749*0.25*a))
            self.coins.append((499*0.5*a,749*0.25*a))
            self.walls[14]=Wall(299*0.5*a,499*0.5*a,499*0.25*a,499*0.25*a,3)
            self.walls[15]=Wall(299*0.5*a,499*0.5*a,749*0.25*a,749*0.25*a,3)
    

        elif cat ==2:
            #ici on va créer un étage simple, avec uniquement 4 murs en brique
            self.walls= [0]*4
            self.walls[0]=Wall(0,xmax,0,0,1) #up
            self.walls[1]=Wall(0,xmax,ymax,ymax,1) #down
            self.walls[2]=Wall(0,0,0,ymax,1) #left
            self.walls[3]=Wall(xmax,xmax,0,ymax,1) #right

        elif cat == 3:
             #ici on va créer un mur infin en béton
            self.walls= [0]*5
            self.walls[0]=Wall(0,1,0,0,2) #up1
            self.walls[1]=Wall(xmax-1,xmax,0,0,2) #up2
            self.walls[2]=Wall(0,1,ymax,ymax,2) #down1
            self.walls[3]=Wall(xmax-1,xmax,ymax,ymax,2) #down2
            self.walls[4]=Wall(xmax/2,xmax/2,0,ymax,2) #down1

        elif cat == 4: #conducteur parfait au milieu
            # self.walls= [0]*5
            # self.walls[0]=Wall(0,xmax,0,0,1) #up
            # self.walls[1]=Wall(0,xmax,ymax,ymax,1) #down
            # self.walls[2]=Wall(0,0,0,ymax,1) #left
            # self.walls[3]=Wall(xmax,xmax,0,ymax,1) #right
            # self.walls[4]=Wall(xmax/2,xmax/2,0,ymax,4) #conducteur parfait

            self.walls=[0]
            self.walls[0]=Wall(xmax/2,xmax/2,0,ymax,4) #conducteur parfait

        elif cat == 5: #cage de Faraday
            self.walls=[0]*4

            #cage de Faraday
            self.walls[0]=Wall(4*xmax/10,6*xmax/10,4*ymax/10,4*ymax/10,4) #up
            self.walls[1]=Wall(4*xmax/10,4*xmax/10,4*ymax/10,6*ymax/10,4) #left
            self.walls[2]=Wall(4*xmax/10,6*xmax/10,6*ymax/10,6*ymax/10,4) #down
            self.walls[3]=Wall(6*xmax/10,6*xmax/10,4*ymax/10,6*ymax/10,4) #right

            #murs autour
            # self.walls[4]=Wall(0,xmax,0,0,1) #up
            # self.walls[5]=Wall(0,xmax,ymax,ymax,1) #down
            # self.walls[6]=Wall(0,0,0,ymax,1) #left
            # self.walls[7]=Wall(xmax,xmax,0,ymax,1) #right

            self.coins.append((0,0));
            self.coins.append((xmax,0));
            self.coins.append((0,ymax));
            self.coins.append((xmax,ymax))

            self.coins.append((4*xmax/10,4*ymax/10));
            self.coins.append((6*xmax/10,6*ymax/10));
            self.coins.append((4*xmax/10,6*ymax/10));
            self.coins.append((6*xmax/10,4*ymax/10));


        elif cat ==6:
            self.walls=[0]*6
            self.walls[0]=Wall(xmax/4,xmax/4,0,ymax/4,2)
            self.walls[1] = Wall(xmax/4,xmax/4, ymax/4+40,ymax,2)
            self.walls[2]=Wall(0,xmax,0,0,1) #up
            self.walls[3]=Wall(0,xmax,ymax,ymax,1) #down
            self.walls[4]=Wall(0,0,0,ymax,1) #left
            self.walls[5]=Wall(xmax,xmax,0,ymax,1) #right
            
        
        #On va mettre l'étage et rajouter un mur au hasard dans celui-ci           
        elif cat==7:
            
            self.walls=[0]*17
            #1) contour de la maison (en briques)
            self.walls[0]=Wall(0,xmax-1,0,0,1) #up
            self.coins.append((0,0))
            self.coins.append((xmax-1,0))
            self.walls[1]=Wall(0,xmax-1,ymax-1,ymax-1,1) #down
            self.coins.append((0,ymax-1))
            self.walls[2]=Wall(0,0,0,ymax-1,1) #left
            self.coins.append((xmax-1,ymax-1))
            self.walls[3]=Wall(xmax-1,xmax-1,0,ymax-1,1) #right

            #2) les murs en béton
            self.walls[4]=Wall(174*0.5,174*0.5,0,124*0.25,2)
            self.coins.append((174*0.5,0))
            self.aretes.append((174*0.5,124*0.25))

            self.walls[5]=Wall(174*0.5,174*0.5,207*0.25,457*0.25,2)
            self.aretes.append((174*0.5,207*0.25))
            self.aretes.append((174*0.5,457*0.25))
            self.walls[6]=Wall(174*0.5,174*0.5,540*0.25,749*0.25,2)
            self.aretes.append((174*0.5,540*0.25))
            self.walls[7]=Wall(299*0.5,299*0.5,0,124*0.25,2)
            self.aretes.append((299*0.5,124*0.25))
            self.walls[8]=Wall(299*0.5,299*0.5,207*0.25,540*0.25,2)
            self.aretes.append((299*0.5,207*0.25))
            self.walls[9]=Wall(299*0.5,299*0.5,431*0.25,623*0.25,2)
            self.aretes.append((299*0.5,623*0.25))
            self.walls[10]=Wall(0,224*0.5,831*0.25,831*0.25,2)
            self.coins.append((0,831*0.25))
            self.aretes.append((224*0.5,831*0.25))
            self.walls[11]=Wall(299*0.5,299*0.5,700*0.25, 831*0.25,2)
            self.aretes.append((299*0.5,700*0.25))
            self.aretes.append((299*0.5,831*0.25))
            self.walls[12]=Wall(0,175*0.5,749*0.25,749*0.25,2)
            self.coins.append((0,749*0.25))
            self.coins.append((175*0.5,749*0.25))
            self.coins.append((299*0.5,0))

            #3) les cloisons
            self.walls[13]=Wall(0,174*0.5,249*0.25,249*0.25,3)
            self.coins.append((0,249*0.25))
            self.coins.append((174*0.5,249*0.25))
            self.coins.append((299*0.5,499*0.25))
            self.coins.append((499*0.5,499*0.25))
            self.coins.append((299*0.5,749*0.25))
            self.coins.append((499*0.5,749*0.25))
            self.walls[14]=Wall(299*0.5,499*0.5,499*0.25,499*0.25,3)
            self.walls[15]=Wall(299*0.5,499*0.5,749*0.25,749*0.25,3)
            
            
                
            
    
    
            
            
            




##    def setmatrice(self):
##     #ajout des walls à la matrice
##        for wall in self.walls:
##            self.matrice[wall.x1:wall.x2+1,wall.y1:wall.y2+1]=wall.mat
##
##    def getmatrice(self):
##        return self.matrice

    def getwalls(self):

        return self.walls


    def getaretes(self):
        return self.aretes

    def getcoins(self):
        return self.coins
