#Code by GVV Sharma
#December 6, 2019
#released under GNU GPL
#Drawing a right angled triangle

import numpy as np
import matplotlib.pyplot as plt

from coeffs import *

#if using termux
#import subprocess
#import shlex
#end if

#Triangle vertices
A = np.array([0,0]) 
B = np.array([8,0]) 
C = np.array([8,7.8]) 
P= np.array([10,0])
M= np.array([5,4.9])
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_PM = line_gen(P,M)
x_BP = line_gen(B,P)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_PM[0,:],x_PM[1,:],label='$PM$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.03), M[1] * (1 - 0.1) , 'M')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
#plt.savefig('./figs/triangle/tri_right_angle.pdf')
#plt.savefig('./figs/triangle/tri_right_angle.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_right_angle.pdf"))
#else
plt.show()







