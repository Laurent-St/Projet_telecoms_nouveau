import math as m
import numpy as np

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return "no_inter"

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y




def isinsegment(pt_arr,pt_dep,pt_inter):
    if(dis_eucl(pt_dep,pt_inter)+dis_eucl(pt_inter,pt_arr) == dis_eucl(pt_dep,pt_arr)):
        return True



def segment_intersec(line1,line2):
    intersection_pt = line_intersection(line1, line2)

    if(intersection_pt == "no_inter"):
        return None
    else:
        if(isinsegment(line1[0],line1[1],intersection_pt)==True and isinsegment(line2[0],line2[1],intersection_pt)==True):
            return intersection_pt
        else:
            return None



def calcAngle_ref(lineA,lineB):
    #ATTENTION ne peut être utilisé que pour l'angle d'incidence de la réflexion et transmission
    line1Y1 = lineA[0][1]
    line1X1 = lineA[0][0]
    line1Y2 = lineA[1][1]
    line1X2 = lineA[1][0]

    line2Y1 = lineB[0][1]
    line2X1 = lineB[0][0]
    line2Y2 = lineB[1][1]
    line2X2 = lineB[1][0]

    #calculate angle between pairs of lines
    angle1 = m.atan2(line1Y1-line1Y2,line1X1-line1X2)
    angle2 = m.atan2(line2Y1-line2Y2,line2X1-line2X2)
    angleDegrees = (angle1-angle2) * 360 / (2*m.pi)

    costemp = abs(m.cos((m.pi/180)*(360-angleDegrees)))
    angleradian=m.acos(costemp)

    return angleradian

def dis_eucl(p1,p2):
	a = p1[0]-p2[0]
	b=p1[1]-p2[1]
	return(np.sqrt(a**2 + b**2))

def calc_angle_diff(vector1,vector2):
    norms = np.linalg.norm(vector1)*np.linalg.norm(vector2)
    theta = np.arccos((vector1[0]*vector2[0] + vector1[1]*vector2[1])/norms)
    return theta

#Fonction permettant de déterminer si oui ou non un point de calcul se situe dans un mur
def isinwall(walls,x,y):
    #Il existe deux cas possible, soit le point se trouve dans un mur horizontal soit vertical

    res = False

    for wall in walls:
        #Mur horizontal
        if y == wall.y1 and y == wall.y2:
            #il faut s'assurer du "sens" du mur x1> ou < que x2
            if wall.x1 < wall.x2:
                if wall.x1 <= x and wall.x2 >= x:
                    res = True
            elif wall.x1 > wall.x2:
                if wall.x1 >= x and wall.x2 <= x:
                    res = True

        #Mur vertical
        if x == wall.x1 and x == wall.x1:
            if wall.y1 < wall.y2:
                if wall.y1 <= y and wall.y2 >= y:
                    res = True
            elif wall.y1 > wall.y2:
                if wall.y1 >= x and wall.y2 <= y:
                    res = True
    return res

#fonction d'interpolation permettant de passer de la sensibilité en dBm au débit binaire

def interpolation (sensibility):
    #-93 dBm == 6 Mb/s
    #-73 dBm == 54 Mb/s
    #y = 6 + 2.4(x + 93)
    res=6 + 2.4*(sensibility + 93)

    return res
