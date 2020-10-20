### Contour plot of the Rosenbrock function ###
import numpy as np
import matplotlib.pyplot as plt

def Rosenbrock(x1,x2):
    return 100*(x2 - x1**2)**2 + (1-x1)**2

x1 = np.linspace(-1.5,2.5,1000)
x2 = np.linspace(-1,3,1000)

X,Y = np.meshgrid(x1,x2)

Z = Rosenbrock(X,Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z) # or use contour or streamline
ax.clabel(CS, fontsize=10)
# Thicken the zero contour.
zc = CS.collections[6]
plt.setp(zc, linewidth=4)

plt.show()
