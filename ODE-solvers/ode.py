import numpy as np

class ODE_Solver():
    """
    Class to solve the simple ODE x' = lambda x

    . Provides so far:
    - Implicit Euler
    - Explicit Euler
    """
    def __init__(self, lambda_, x0, T, N, n):
        """
        Input:
        - N, number of intervals
        - x0, inital condition at t = 0;
        - T, time interval from t = 0.
        - n,  the dimension of the vector x
        """
        self.T = T;
        self.N = N;
        self.h = T/(N) # intervals and uniform step size
        self.t = np.linspace(0,T,N+1);

        if n == 1:
            self.y = np.zeros(N+1); # apporx to x
            self.y[0] = x0; # set initial condition
        else:
            self.y = np.zeros((n,self.N+1), dtype = complex); # remember to cast as complex
            self.y[:,0] = x0;

        self.lmd= lambda_
        self.n = n

    def explicit_euler(self):
        for i in range(0,self.N):
            self.y[i+1] = self.y[i] + self.h*self.lmd*self.y[i]
        return self.t,self.y

    def implicit_eluer(self):
        for i in range(0,self.N):
            self.y[i+1] = 1/(1 - self.h*self.lmd)*self.y[i];
        return self.t,self.y

    def linear_system_EE(self, V):
        """
        Solves a system of ODES with explicit euler
        In this case, lambda is an n dimension vector
        with eigenvalues of A

        Input:
        - V is the matrix with eigenvectors of A
        """
        for time in range(0,self.N):
            for dims in range(0,self.n):
                self.y[dims,time+1] =  self.y[dims,time] + self.h*np.vdot([self.lmd[dims]],[self.y[dims,time]]);
        self.y = V@self.y

        return self.t,self.y
