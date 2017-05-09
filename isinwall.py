

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