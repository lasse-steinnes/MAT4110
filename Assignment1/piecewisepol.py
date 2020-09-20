### Program that piecewise interpolates functions linearly ###
import numpy as np
import matplotlib.pyplot as plt
import argparse

def f1(x):
    return np.sin(x)

def f2(x):
    return 1/(1+25*x**2)

def divdiff(x, d, k):           # Use a matrix for divided difference
    for i in range(1, k+1):
        for j in range(k+1 - i):
            d[j,i] = ((d[j,i - 1] - d[j + 1,i - 1]) /
                                     (x[j] - x[i + j]));
    return d[0,:];

def piecewisepol(f,a,b,N,k):
    """
    Input:
    f: User defined function to be interpolated
    N: number of subintervals in [a,b] (s.t. N+1 points)
    k: Degree of spline
    a: startpoint
    b: endpoint
    """

    h = (b - a)/float(N);
    x = [a + i*h for i in range(N+1)] # n+1 points
    # Make subinterval for spline
    x_j = np.zeros((k+1,N))               #  Column vectors are subintervals of interval xi xi-1
    f_mat = np.zeros((k+1,N))
    c = np.zeros(k+1)                     # Initialize coefficient of p
    x_ints = np.zeros((k+1,100))          # Initialize intervals x-x_i
    diff_tab = np.zeros((k+1,k+1))
    coeff = np.zeros((N,k+1))
    for i in range(1,len(x)):
        for j in range(k+1):
            x_j[j,i-1] = x[i-1] + j/k*h     # Fill in subintervals for spline columnwise, make matrix of f as well
            f_mat[j,i-1] = f(x_j[j,i-1]);

            diff_tab[:,0] = f_mat[:,i-1]
        coeff[i-1,:] = divdiff(x_j[:,i-1],diff_tab,k)

    # make polyn
    for i in range(0,len(x)-1):
        x_ints[0,:] = 1;
        pol = np.full(100,coeff[i,0])
        for j in range(1,k+1):
            xj = x_j[j,i]; xj_prev =  x_j[j-1,i]
            x_sub = np.linspace(x_j[0,i],x_j[k,i],100);
            xjp_vec = np.full(100,xj_prev);
            x_ints[j,:] = x_ints[j-1,:]*(x_sub-xjp_vec)
            pol += coeff[i,j]*x_ints[j,:];
        # for each sub interval
        plt.plot(x_sub,pol,'--', color = 'green')
        plt.plot(x_j[:,i], f(x_j[:,i]),'.')

# plot final
    x_a = np.linspace(a,b, 1000)
    plt.plot(x_a,f(x_a),label = 'Analytical', alpha = 0.7)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('N:{:d}, k: {:d}'.format(N,k))
    plt.show()



#run and produce results

def fx(x):
    return x

r1 = 'sine'
r2 = 'Runge'
N = (8,1); k = (1,8)

for i in range(len(N)):
    print(r1)
    piecewisepol(f1,-np.pi,np.pi,N[i],k[i])
    print(r2)
    piecewisepol(f2,-1,1,N[i],k[i])
