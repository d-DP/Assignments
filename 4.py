import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if


len = 50
r1 = 6
A = np.array([5,3.23]) 
B = np.array([0,0]) 
C = np.array([10,0])
M = np.array([5,0]) 
D=np.array([5.09,-3.12])
E = np.array([5,6]) 
F = np.array([5.09,-6]) 

theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ2 = np.zeros((2,len))


x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)



x_circ1 = (x_circ1.T).T
x_circ2 = (x_circ2.T).T

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_CD = line_gen(C,D)
x_BC = line_gen(B,C)
x_BD = line_gen(B,D)
x_AM = line_gen(A,M)
x_MD = line_gen(M,D)
x_AE = line_gen(A,E)
x_DF = line_gen(D,F)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')



#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_AM[0,:],x_AM[1,:],label='$AM$')
plt.plot(x_MD[0,:],x_MD[1,:],label='$MD$')
plt.plot(x_AE[0,:],x_AE[1,:])
plt.plot(x_DF[0,:],x_DF[1,:])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.03), M[1] * (1 - 0.1) , 'M')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/circle/circumcircle.pdf')
#plt.savefig('./figs/circle/circumcircle.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()
