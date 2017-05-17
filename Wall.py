import numpy as np


eps_0 = 8.85*(10**(-12)) #permittivité électrique du vide
c = 3*(10**8) #vitesse de la lumière
mu_0 = 4*np.pi*(10**(-7)) #perméabilité magnétique du vide
w = 2*np.pi*2.45*(10**9) #pulsation des ondes
sig_parfait=10**(12) #valeur élevée pour simuler l'infini pour un conducteur parfait

class Wall:
    "Classe mur contenant les coordonnées (x1,y1) et (x2,y2)"
    def __init__(self,x1,x2,y1,y2,mat):
        #mat=material
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.mat=mat
        if mat==1: # 1 = brique
            self.eps_r=4.6
            self.sig=0.02
            self.d=0.1
        elif mat==2: # 2 = beton
            self.eps_r=5
            self.sig=0.014
            self.d=0.25
        elif mat==3: # 3 = cloison
            self.eps_r=2.25
            self.sig=0.04
            self.d=0.05
        elif mat ==4: #4 = conducteur parfait
            self.eps_r=1 #valeur pour le cuivre
            self.sig=sig_parfait #valeur élevée pour simuler l'infini
            self.d=0.25 #meme épaisseur qu'une cloison

    def getmat(self):
        return self.mat

        #Permet d'obtenir le module du coeff. de réflexion sur un mur d'épaisseur d en fonction de l'angle d'incidence, qui doit être en RADIANS

    def get_coeff_reflex(self, theta_i):

        #Calcul des permittivités
        eps = self.eps_r*eps_0
        eps_comp = eps - 1j*(self.sig/w)

        #Calcul des impédances caractéristiques
        Z0 = np.sqrt(mu_0/eps_0)
        Zm = np.sqrt(mu_0/eps_comp)


       #Calcul de l'angle de transmission

        theta_t = np.arcsin(np.sqrt(1/self.eps_r)*np.sin(theta_i))



        #Calcul de la distance parcourue dans le mur

        s = self.d/np.cos(theta_t)




        #Calcul du terme de propagation dans l'air

        beta=w/c


        #Calcul du terme de propagation dans le mur

        gamma_m = 1j*w*np.sqrt(mu_0*eps_comp)

        #Calcul du coeff de réflexion pour un angle theta_i, comme si le mur était semi-infini

        Gamma_per = (Zm*np.cos(theta_i)-Z0*np.cos(theta_t))/(Zm*np.cos(theta_i)+Z0*np.cos(theta_t))


        #Calcul du coeff de réflexion total et de son module

        C = Gamma_per**2
        D = np.exp(-2*gamma_m*s)
        E = np.exp(2j*beta*s*np.sin(theta_t)*np.sin(theta_i))
        F = (1-C)
        G = F*Gamma_per*D*E
        H = 1-C*D*E
        Gamma_m = Gamma_per + G/H

        #print('coef reflex=',np.absolute(Gamma_m))
        # if self.sig==sig_parfait:
        #     print('coef reflex cond parfait',np.absolute(Gamma_m))

        return(np.absolute(Gamma_m))




     #Permet d'obtenir le module du coeff. de transmission sur un mur d'épaisseur d en fonction de l'angle d'incidence, qui doit être en RADIANS

    def get_coeff_trans (self, theta_i):
        T_m = 1 - self.get_coeff_reflex(theta_i)
        # if self.sig==sig_parfait:
        #     print('coef transcond parfait',T_m)

        #print('coef trans=',T_m)
        return(T_m)
