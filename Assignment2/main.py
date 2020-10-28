### Run programmes from main ###
import numpy as np
from optimize import Optimize
import matplotlib.pyplot as plt

f = lambda z: -1;
df = lambda z: 0;
f2 = lambda z: -z**2;
df2 = lambda z: -2*z;
funcs = (f,f2); alpha = (0,1);
dfuncs = (df,df2)
beta = (1,1); tolerance = 1e-12; N = 50;

ana = lambda x: 0.5*x*(3-x);

print("Press 1 to run fixed point optimization")
print("Press 2 to run Newtons method")
arg = input("Input number:");

if int(arg) == 1:
    # test fixed point
    for i in range(len(alpha)):
        fixed = Optimize();
        x,z = fixed.fixedpointODE(funcs[i],alpha[i],beta[i],N,tolerance)
        plt.plot(x,z,'--.',label = "numerical")
        if i == 0:
            plt.plot(x,ana(x),'-', label = "analytical")
        plt.title("Fixed point method")
        plt.xlabel("x",fontsize = 13)
        plt.ylabel("z",fontsize = 13)
        plt.legend(loc = "upper right",fontsize = 15)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()



# test Newtons method
elif int(arg) == 2:
    for i in range(len(alpha)):
        newt = Optimize();
        x,z = newt.newtonODE(funcs[i], dfuncs[i], alpha[i], beta[i], N, tolerance);
        plt.plot(x,z,'--.',label = "numerical")
        if i == 0:
            plt.plot(x,ana(x),'-', label = "analytical")
        plt.title("Newtons method")
        plt.xlabel("x",fontsize = 13)
        plt.ylabel("z",fontsize = 13)
        plt.legend(loc = "upper right",fontsize = 15)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

else:
    print("Input Error: Not a method. Choose option 1 or 2 (integers)")
