from fctsmath import *
import math as m
import numpy as np

"""
line1=[(0,-2),(1,1)]
line2=[(0,0),(2,0)]

theta1=calcAngle(line1,line2)
#t1deg=theta1*360/(2*m.pi)
print(theta1)
x1=abs(m.cos(theta1))
print(x1)

line3=[(1,1),(2,-2)]
line4=[(0,0),(2,0)]

theta2=calcAngle(line3,line4)
#t2deg=theta2*360/(2*m.pi)
x2=abs(m.cos(theta2))
print(x2)
print(theta2)"""

"""
#test liste
xmax=5
ymax=3
#ls_PRX_pt_ij = [[0 for x in range(0,xmax)] for y in range(0,ymax)]
ls_PRX_pt_ij=np.zeros((ymax,xmax))
#print(ls_PRX_pt_ij)

for i in range(0,ymax): #i= dimension y
    #print('lstemp:',ls_PRX_pt_ij)
    for j in range(0,xmax): #j= dimension x
            ls_PRX_pt_ij[i][j]=5
print(ls_PRX_pt_ij)
"""

#test for par pas décimal
for i in np.arange(0,5,0.1):
    print(i)
