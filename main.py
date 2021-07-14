import shapely
from shapely.geometry import LineString, Point
import numpy as np
import math
import math
import matplotlib.pyplot as plt
import numpy as np
# from Grid_and_ds_generator import *
# from dnds_dndt import *

# grid and ds dx has been generated in th Grid file
# dnds dndt for integration points

from dndx_dndy_vol_forip import *


#   dnds dndt of volumes center of sub cv
# dndx dndy and volumes for each ip

def DNDXY(X, Y):
    volumes = np.zeros(4)
    dndx = np.zeros((4, 4))
    dndy = np.zeros((4, 4))

    for ip in range(0, 4):
        temp = dndx_dndy_vol_ip(ip, X, Y)
        dndx[ip] = temp[0]
        dndy[ip] = temp[1]
        volumes[ip] = temp[2]

    return dndx, dndy, volumes,


# atention for dsx k and j  + -
def CEOF(dsx_el, dsy_el, dndx, dndy, V, alpha, T_old):
    D = np.zeros(4)
    C = np.zeros((4, 4))
    for i in range(0, 4):

        j = i
        k = j - 1
        if j == 0:
            k = 3

        for m in range(0, 4):

            C[i][m] = - alpha * (
                        dndx[i][m] * (dsx_el[j]) + dndy[i][m] * (dsy_el[j]) - dndx[i][m] * dsx_el[k] - dndy[i][m] *
                        dsy_el[k])
            if m == i:
                C[i][m] = V[i] / dt

        D[i] = T_old * V[i] / dt
    return C, D


# for hame eleman haro bere squares:

elemNum = 0
A = np.zeros((Nx * Ny, Nx * Ny))
B = np.zeros(Nx * Ny)
for square in squaresQordinations:
    X = []
    Y = []
    for XY in square:
        X.append(XY[0])
        Y.append(XY[1])
    temp = DNDXY(X, Y)
    dndx = temp[0]
    dndy = temp[1]
    Volumes = temp[2]
    answer_CD = CEOF(dsx[elemNum], dsy[elemNum], dndx, dndy, Volumes, alpha, T[elemNum])
    C = answer_CD[0]
    D = answer_CD[1]

    il = squareNums[elemNum]

    for i in range(0, 4):
        for j in range(0, 4):
            A[il[i]][il[j]] = A[il[i]][il[j]] + C[i][j]
            B[il[i]] = B[il[i]] + D[i]

    elemNum = elemNum + 1
k = 5
print(k, Nx)
