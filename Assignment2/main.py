### Run programmes from main ###
import numpy as np
from optimize import Optimize
import matplotlib.pyplot as plt

f = lambda z: -1;
df = lambda z: 0;
f2 = lambda z: -z**2;
df2 = lambda z: -2*z; 
funcs = (f,f2); alpha = (0,1);
beta = (1,1); tolerance = 1e-12; N = 50;

# test fixed point
for i in range(len(alpha)):
    fixed = Optimize();
    x,z = fixed.fixedpointODE(funcs[i],alpha[i],beta[i],N,tolerance)
    print('x',x)
    print('z',z)

# test
