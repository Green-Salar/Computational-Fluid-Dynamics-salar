import math

import numpy as np

pi = math.pi
Nx = 9
Ny = 7
delatTetaX = pi/(Nx-1)
delatTetaY = pi/(Ny-1)
deltaYn = 1/(Ny-1)
deltaXn = 1/(Nx-1)
k = 44     # W/m2C
ro = 7830  #kg/m3
cp = 481   #j/kgC
alpha =k/(ro*cp)
dt=0.1
T = np.zeros(Nx*Ny)
for i in range(0,int(Nx*Ny)):
    T[i] = 115