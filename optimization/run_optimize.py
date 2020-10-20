import numpy as np
from optimize import Optimization

### for f
Af = np.array([[2,0],[0,4]])
b = np.array([[-4],[-6]])
x_start =  np.array([[-3],[-2]])                # starting point of descent method
c = 0

f_optim = Optimization_Quadratic(Af, b, c)
x_newton,f_newton = f_optim.newtons_method(x_start)
x_sd,f_sd = f_optim.steepest_descent(x_start)
print('Results:Newton',x_newton,f_newton)
print('Results:Steepest descent:',x_sd,f_sd)

### for g
"""
Ag = np.array([[2,0],[0,-4]])
g_optim = Optimization(Ag,b,c)
x,g = g_optim.steepest_descent(x_start)
print(x,g)
"""
