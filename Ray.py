import numpy as np
import math as math

c = 3*(10**8) #vitesse de la lumière
w = 2*np.pi*2.45*(10**9) #pulsation des ondes

class Ray:
    "Un rayon va être un vecteur avec un tuple (x,y) caractérisant son point de départ,"
    "et un tuple (x,y) caractérisant son point d'arrivée"

    def __init__(self,x1,y1,x2,y2,coef,dis):
        #coef=coefficient total par lequel la valeur du champ est multiplié
        #dis=distance euclidienne parcourue par tous les rayons composants une réflexion, donc cet attribut ne sera
        #mis que pour le dernier rayon d'une réflexion
        a=1
        facteur_echelle=(100*a)/12
        #facteur_echelle=41.66/2 # /pour faire correspondre les dimensions python aux dimensions de la pièce
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.coef=coef
        self.dis=dis
        if dis != None:
            self.dis=dis/facteur_echelle

    def get_elec_field(self,tx):
        # tx est un OBJET de type Antenna, c'est l'émetteur
        beta=w/c
        #print('self.dis=',self.dis)
        if self.dis != None and self.dis != 0:
            E=self.coef*np.sqrt(60*tx.gain*tx.power_emission)*np.exp(-1j*beta*self.dis)/self.dis
        else:
            E=None
        return E

    def get_PRX_individuelle(self,tx):
        "Calcule la puissance reçue (par l'antenne réceptrice donc) pour UNE onde incidente"
        E=self.get_elec_field(tx)
        if E != None:
            PRX=(1/(8*tx.r_tot))*(np.absolute(tx.h_e*E))**2
        else:
            PRX=0
        #print('PRX[dBm]=',10*np.log(PRX/0.001))
        return PRX



    def getcolor(self):
        if self.coef>0.8:
            color='red'
        elif self.coef<=0.8 and self.coef>0.6:
            color='orange'
        elif self.coef<=0.6 and self.coef>0.4:
            color='yellow'
        elif self.coef<=0.4 and self.coef>0.2:
            color='blue'
        else:
            color='cyan'
        return color
