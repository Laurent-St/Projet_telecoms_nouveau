from fctsmath import *
import math as m
from Ray import *
from Wall import *

def onde_directe(tx,rx,walls):
    ray1=Ray(tx[0],tx[1],rx[0],rx[1],1,dis_eucl(tx,rx))
    for wall in walls:
        if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
            theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
            ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)
    return ray1

def onde_directe_compteur(tx,rx,walls):
    compteur=0
    ls_pos=[]
    ray1=Ray(tx[0],tx[1],rx[0],rx[1],1,dis_eucl(tx,rx))
    for wall in walls:
        if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None:
            pos=segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            ls_pos.append(pos)
            compteur=compteur+1
            theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
            ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)
    return ray1,compteur,ls_pos

def reflexion(tx,rx,walls):
    """
    tx et rx sont des tuples contenant la position en x et en y de l'émetteur et du récepteur
    ATTENTION: les recherches des 4 murs ainsi que des pts images, et l'attribution des rayons sont toujours faits dans l'ordre suivant:
    RIGHT, UP, LEFT, DOWN
    """

    #1) trouver les 4 murs les plus proches dans les 4 directions
    interright=[]
    interrup=[]
    interleft=[]
    interdown=[]
    wallright=[]
    wallup=[]
    wallleft=[]
    walldown=[]
    imright=[]
    imup=[]
    imleft=[]
    imdown=[]
    for wall in walls:
##        minright=100000  #valeur très élevée pour que le premier élément de inter... soit d'office le premier min
##        minup=100000
##        minleft=100000
##        mindown=100000

        if wall.x1>=tx[0] and wall.x1==wall.x2: #murs verticaux à droite de tx
            interright.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallright.append(wall)
            #calcule l'intersection entre une ligne horizontale partant de tx vers la droite, et le mur
            imright.append((2*wall.x1-tx[0],tx[1]))
##            if abs(interright[0]-tx[0])<minright: #cherche le mur qui a l'intersection la plus proche, cad la difference de x la plus faible
##                minright=abs(interright[0]-tx[0])
##                wallminright=wall

        elif wall.y1<=tx[1] and wall.y1==wall.y2: #murs horizontaux au-dessus de tx
            interrup.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallup.append(wall)
            #calcule l'intersection entre une ligne verticale partant de tx vers le haut, et le mur
            imup.append((tx[0],2*wall.y1-tx[1]))
            # print(2*wall.y1-tx[1])
            # print('testup')
            # print(wallup[0].x1)
            # print(imup[0])
##
##            if abs(interrup[1]-tx[1])<minup:
##                minup=abs(interrup[1]-tx[1])
##                wallminup=wall

        elif wall.x1<=tx[0] and wall.x1==wall.x2: #murs verticaux à gauche de tx
            interleft.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallleft.append(wall)
            imleft.append((2*wall.x1-tx[0],tx[1]))
            # print('testleft')

##            if abs(interleft[0]-tx[0])<minleft:
##                minleft=abs(interleft[0]-tx[0])
##                wallminleft=wall

        else: #murs horizontaux en-dessous de tx
            interdown.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            walldown.append(wall)
            imdown.append((tx[0],2*wall.y1-tx[1]))
            # print('testdown')

##            if abs(interdown[1]-tx[1])<mindown:
##                mindown=abs(interdown[1]-tx[1])
##                wallmindown=wall

##    reswall=[wallminright,wallminup,wallminleft,wallmindown]

    #2) trouver les points images: comprendre les distances à l'aide d'un dessin
##    im=[0]*4
##    im[0]=(2*reswall[0].x1-tx[0],tx[1])
##    im[1]=(tx[0],2*reswall[1].y1-tx[1])
##    im[2]=(2*reswall[2].x1-tx[0],tx[1])
##    im[3]=(tx[0],2*reswall[3].y1-tx[1])

    #3) pts d'intersection entre mur et droite ptimage-rx, et tracer les rayons
##    pt_inter=[]
    rays=[] #2 fois plus grande que pt_inter car 2 rayons par réflexion
    # print(wallup[0])
##    j=0 #compteur pour les rayons
##    for i in range (0,4):
##        pt_inter[i]=segment_intersec([im[i],rx],[(reswall[i].x1,reswall[i].y1),(reswall[i].x2,reswall[i].y2)])
##        rays[j]=[tx,pt_inter[i]] #un rayon=une ligne cad [tuple,tuple]
##        j=j+1
##        rays[j]=[pt_inter[i],rx]
##        j=j+1
    pt_inter_right=[]
    for i in range(0,len(wallright)):
        pt_inter_right_i=segment_intersec([imright[i],rx],[(wallright[i].x1,wallright[i].y1),(wallright[i].x2,wallright[i].y2)])
        pt_inter_right.append(pt_inter_right_i)
        if pt_inter_right_i != None:

            #line1=[tx,pt_inter_right[i]]
            ray1=Ray(tx[0],tx[1],pt_inter_right[i][0],pt_inter_right[i][1],1,None) #rayon 1 entre tx et le pt d'intersection, coef est mis à 1
            #recherche des transmissions de ray1
            for wall in wallright: #juste sur les murs à droite de l'émetteur (logique)
                if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall !=wallright[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
                    ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)

            ray2=Ray(pt_inter_right[i][0],pt_inter_right[i][1],rx[0],rx[1],ray1.coef,dis_eucl(imright[i],rx)) #rayon 2 entre le pt d'intersection et rx
            #recherche des transmisssions de ray2
            for wall in walls:
                if segment_intersec([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != wallright[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                    ray2.coef=ray2.coef*wall.get_coeff_trans(theta_itr)

            theta_i= m.pi/2 - calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)], [(wallright[i].x1,wallright[i].y1),(wallright[i].x2,wallright[i].y2)]) #angle d'incidence de REFLEXION
            ray2.coef=ray2.coef*wallright[i].get_coeff_reflex(theta_i) #multiplication du coefficient de ray2
            rays.append(ray1)
            rays.append(ray2)

    pt_inter_up=[]
    for i in range(0,len(wallup)):
        # print('interupok')
        pt_inter_up_i=segment_intersec([imup[i],rx],[(wallup[i].x1,wallup[i].y1),(wallup[i].x2,wallup[i].y2)])
        pt_inter_up.append(pt_inter_up_i)
        if pt_inter_up_i != None:

            # print(pt_inter_up)
            ray1=Ray(tx[0],tx[1],pt_inter_up[i][0],pt_inter_up[i][1],1,None) #rayon 1 entre tx et le pt d'intersection, coef est mis à 1
            #recherche des transmissions de ray1
            for wall in wallup: #juste sur les murs à droite de l'émetteur (logique)
                if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != wallup[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
                    ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)

            ray2=Ray(pt_inter_up[i][0],pt_inter_up[i][1],rx[0],rx[1],ray1.coef,dis_eucl(imup[i],rx)) #rayon 2 entre le pt d'intersection et rx
            #recherche des transmisssions de ray2
            for wall in walls:
                if segment_intersec([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != wallup[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                    ray2.coef=ray2.coef*wall.get_coeff_trans(theta_itr)

            theta_i= m.pi/2 - calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)], [(wallup[i].x1,wallup[i].y1),(wallup[i].x2,wallup[i].y2)]) #angle d'incidence de REFLEXION
            ray2.coef=ray2.coef*wallup[i].get_coeff_reflex(theta_i) #multiplication du coefficient de ray2
            rays.append(ray1)
            rays.append(ray2)

    pt_inter_left=[]
    for i in range(0,len(wallleft)):
        # print('wallleftok')
        pt_inter_left_i=segment_intersec([imleft[i],rx],[(wallleft[i].x1,wallleft[i].y1),(wallleft[i].x2,wallleft[i].y2)])
        pt_inter_left.append(pt_inter_left_i)
        if pt_inter_left_i != None:

            ray1=Ray(tx[0],tx[1],pt_inter_left[i][0],pt_inter_left[i][1],1,None) #rayon 1 entre tx et le pt d'intersection, coef est mis à 1
            #recherche des transmissions de ray1
            for wall in wallleft: #juste sur les murs à droite de l'émetteur (logique)
                if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != wallleft[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
                    ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)

            ray2=Ray(pt_inter_left[i][0],pt_inter_left[i][1],rx[0],rx[1],ray1.coef,dis_eucl(imleft[i],rx)) #rayon 2 entre le pt d'intersection et rx
            #recherche des transmisssions de ray2
            for wall in walls:
                if segment_intersec([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != wallleft[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                    ray2.coef=ray2.coef*wall.get_coeff_trans(theta_itr)

            theta_i= m.pi/2 - calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)], [(wallleft[i].x1,wallleft[i].y1),(wallleft[i].x2,wallleft[i].y2)]) #angle d'incidence de REFLEXION
            ray2.coef=ray2.coef*wallleft[i].get_coeff_reflex(theta_i) #multiplication du coefficient de ray2
            rays.append(ray1)
            rays.append(ray2)

    pt_inter_down=[]
    for i in range(0,len(walldown)):
        pt_inter_down_i=segment_intersec([imdown[i],rx],[(walldown[i].x1,walldown[i].y1),(walldown[i].x2,walldown[i].y2)])
        pt_inter_down.append(pt_inter_down_i)
        if pt_inter_down_i != None:

            ray1=Ray(tx[0],tx[1],pt_inter_down[i][0],pt_inter_down[i][1],1,None) #rayon 1 entre tx et le pt d'intersection, coef est mis à 1
            #recherche des transmissions de ray1
            for wall in walldown: #juste sur les murs à droite de l'émetteur (logique)
                if segment_intersec([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != walldown[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
                    ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)

            ray2=Ray(pt_inter_down[i][0],pt_inter_down[i][1],rx[0],rx[1],ray1.coef,dis_eucl(imdown[i],rx)) #rayon 2 entre le pt d'intersection et rx
            #recherche des transmisssions de ray2
            for wall in walls:
                if segment_intersec([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!=None and wall != walldown[i]:
                    theta_itr=m.pi/2-calcAngle_ref([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                    ray2.coef=ray2.coef*wall.get_coeff_trans(theta_itr)

            theta_i= m.pi/2 - calcAngle_ref([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)], [(walldown[i].x1,walldown[i].y1),(walldown[i].x2,walldown[i].y2)]) #angle d'incidence de REFLEXION
            ray2.coef=ray2.coef*walldown[i].get_coeff_reflex(theta_i) #multiplication du coefficient de ray2
            rays.append(ray1)
            rays.append(ray2)



    #4) Reflexion double: A FAIRE


    #reflexions double pour tous les murs de droite (s'il y a transmission)
    #calcul des points images seconde Y'' en haut et en bas du mur considéré (ici le droit)
    #la première intuituion serait de chercher à éliminer certains murs: on pourrait chercher à savoir s'il existe des potentielles
    #réflexions dans les murs du haut/bas mais en fait l'ensemble des murs du haut/bas sont suceptible de créer des réflexions
    #on est donc obligé de faire tout les murs possibles
    #création de liste des images secondes, on a déjà celle des premières images
    imsecrightup = []
    imsecrightdown = []
    imsecleftup = []
    imsecleftdown = []
    imsecupright = []
    imsecupdown = []
    imsecdownright = []
    imsecdownleft = []

    #création de la liste des points de deuxième réflexion (le rayon part de l'emetteur touche une première fois le mur
    # est réfléchis, puis touche un second mur (c'est ce point qui sont dans ptreflex2) avant d'aller (c'est ce rayon qui est dans rayreflex2)
    # au recepteur) et des rayons attitrés
    ptreflex2 = []
    rayreflex2 = []
    #création de la liste des points de première réflexion et des rayons attitrés (même principe)
    ptreflex1 = []
    rayreflex1 = []
    #création de la liste des rayons allant du point de première réflexion à l'emetteur
    rayemett = []
    #attention imright doit etre modifié!!! i doit comprendre les points images de tout les murs pas seulement ceux qui possèdent un x
    #ou y égal à xT ou yT


    #afin de récupérer les murs de droite qui permetterons de calculer le point de première réflection il est nécessaire
    #d'ittérer sur des indices et non pas sur des objets, on sait que la liste des murs à droite de l'émetteur et
    #la liste des images à droites évoluent en parallèle onc pour chaque image de droite utilisé il y a le mur de droite correspondant,
    #ils sont au même indice

    ########################################################################################################################
    #Mur de droite

    for i in range(0,len(imright)) :
        im = imright[i]
        tempwall = wallright[i]
        #Mur de droite partie haute
        ###############
        for wall in wallup :
            #print('for wall in wallup')
            #calcul des points d'image seconde au dessus

            ypp_up = (im[0],2 * wall.y1 - im[1])
            imsecrightup.append(ypp_up)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_up],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #print('p2droitehaut=',p2)
            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                #print('p1droitehaute',p1)
                if p1 != None:
                    #en effet, il se peut que le mur devant subir la seconde réflexion soit "trop court", et donc que le point p2 se retrouve
                    #sur le mur de droite et pas celui du haut, ce qui aurait pour conséquence  que p1 == p2 il faut donc proscrire l'ensemble de
                    #ces cas
                    if p1 != p2:
                        #print('droitehaut')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_up,rx))
                        rayreflex2.append(r2)

                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                #2e cdt du if pour ne pas calculer un coeff de transmission sur le mur sur lequel on est réfléchi
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                #les 2e et 3e cdts du if sont pour éviter de calculer une transmission sur les 2 murs gauche et haut sur lesquels il y a réflexion
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recepteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                #ici pas de 3e cdt car on est juste sur le mur du dessus
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)

        ###############
        #Mur de droite partie basse
        for wall in walldown :
            #calcul des points d'image seconde au dessous
            ypp_down = (im[0],2 * wall.y1 - im[1])
            imsecrightdown.append(ypp_down)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_down],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #print('2e p2:',p2)
            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                if p1 != None:

                    if p1 != p2:
                        #print('droitebas')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_down,rx))
                        rayreflex2.append(r2)

                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                         #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)]) != None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur du bas
    for i in range(0,len(imdown)) :
        im = imdown[i]
        tempwall = walldown[i]

        #####################
        #Mur du bas partie droite
        for wall in wallright :
            #calcul des points d'image seconde de droite
            ypp_right = (2 * wall.x1 - im[0], im[1])
            imsecdownright.append(ypp_right)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_right],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #print('3e p2=',p2)
            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                if p1 != None:
                    if p1 != p2:
                        #print('basdroite')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_right,rx))
                        rayreflex2.append(r2)

                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)

        ############################
        #Mur du bas partie gauche
        for wall in wallleft :
            #calcul des points d'image seconde de gauche

            ypp_left = (2*wall.x1-im[0],im[1])
            imsecdownleft.append(ypp_left)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_left],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                if p1 != None:

                    if p1 != p2:
                        #print('basgauche')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_left,rx))
                        rayreflex2.append(r2)

                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur de gauche

    for i in range(0,len(imleft)) :
        im = imleft[i]
        tempwall = wallleft[i]

        ####################
        #Mur de gauche partie haute
        for wall in wallup :
            #calcul des points d'image seconde au dessus

            ypp_up = (im[0],2 * wall.y1 - im[1])
            #print('imagegauchehaut',ypp_up)
            imsecleftup.append(ypp_up)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_up],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #print('p2gauchehaut=',p2)

            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                #print('p1gauchehaut=',p1)

                if p1 != None:

                    if p1 != p2:
                        #print('gauchehaut')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_up,rx))
                        rayreflex2.append(r2)

                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)

        ########################
        #Mur de gauche partie basse
        for wall in walldown :
            #calcul des points d'image seconde au dessous
            ypp_down = (im[0],2 * wall.y1 - im[1])
            #print('imagegauchebas',ypp_down)
            imsecleftdown.append(ypp_down)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_down],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #print('p2gauchebasse',p2)

            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                if p1 != None:

                    if p1 != p2:
                        #print('gauchebas')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_down,rx))
                        rayreflex2.append(r2)

                        #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                        p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur du haut
    for i in range(0,len(imup)) :
        im = imup[i]
        tempwall = wallup[i]

        #Mur du bas partie droite
        for wall in wallright :
            #calcul des points d'image seconde de droite
            ypp_right = (2 * wall.x1 - im[0], im[1])
            imsecdownright.append(ypp_right)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_right],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                if p1 != None:

                    if p2 != p1:
                        #print('hautdroit')
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_right,rx))
                        rayreflex2.append(r2)

                        #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                        p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)

        ################
        #Mur du bas partie gauche
        for wall in wallleft :
            #calcul des points d'image seconde de gauche
            ypp_left = (2*wall.x1-im[0],im[1])
            imsecdownleft.append(ypp_left)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),ypp_left],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            if p2 != None:
                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                if p1 != None:
                    if p1 != p2:
                        ptreflex2.append(p2)
                        r2 = Ray(p2[0],p2[1],rx[0],rx[1],1,dis_eucl(ypp_left,rx))
                        rayreflex2.append(r2)

                        #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                        p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                        ptreflex1.append(p1)
                        r1 = Ray(p1[0],p1[1],p2[0],p2[1],1,None)
                        rayreflex1.append(r1)

                        #calcul de l'angle d'incidence de première et 2e réflexion
                        theta_2 = m.pi/2 - calcAngle_ref([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                        theta_1 = m.pi/2 - calcAngle_ref([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                        #tracage des rayons allant de l'emetteur au premier point de réflexion
                        r0 = Ray(tx[0],tx[1],p1[0],p1[1],1,None)
                        rayemett.append(r0)

                        #Calcul des coefficients de transmission des rayons emetteur-p1
                        for wallbis in wallright:
                            if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                        #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                        for wallbis in walls:
                            if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                        r1.coef=r1.coef*r0.coef*tempwall.get_coeff_reflex(theta_1)

                        #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                        for wallbis in walls:
                            if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                                theta_itr=m.pi/2-calcAngle_ref([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                                r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                        r2.coef=r2.coef*r1.coef*r0.coef*wall.get_coeff_reflex(theta_2)

    #concaténation de toute les listes
    rays.extend(rayemett)
    rays.extend(rayreflex1)
    rays.extend(rayreflex2)

    return rays

    #SI ON VEUT JUSTE AVOIR LES DOUBLES REFLEXIONS
    # print(rayemett)
    # print(rayreflex1)
    # print(rayreflex2)
    #
    # raysbis=rayemett
    # raysbis.extend(rayreflex1)
    # raysbis.extend(rayreflex2)
    #
    # return raysbis
