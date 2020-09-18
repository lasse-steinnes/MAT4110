### Program that piecewise interpolates functions linearly ###
import numpy as np
import matplotlib.pyplot as plt

N = 8 # n
k = 2
a = 1
b = 2
h = (b - a)/float(N); print('h',h )
x = [a + i*h for i in range(N+1)]           # Have N+1 points
print('x',x)
x_j = np.zeros((k+1,N)) #kolonnevektorer
for i in range(1,len(x)):
    for j in range(k+1):
        x_j[j,i-1] = x[i-1] + j/k*h # Lager åtte intervaller for splinen lagt inn kolonnevis


print('x_j',x_j)

def piecewisepol(f,a,b,N,k, makefig = True):
    """
    Input:
    f: User defined function to be interpolated
    N: number of intervals in [a,b] (s.t. N+1 points)
    k: Degree of spline
    a: startpoint
    b: endpoint
    """
    x = [a + i*h for i in range(N+1)] # n+1 points
    # Make subinterval for spline
    x_j = np.zeros((k+1,N)) #kolonnevektorer
    for i in range(1,len(x)):
        for j in range(k+1):
            x_j[j,i-1] = x[i-1] + j/k*h # Lager åtte intervaller for splinen lagt inn kolonnevis

    #### Så interpoler med disse x_j-ene ved hjelp av generell algo




    if makefig():
        plt.plot
    return px,fx
