### Write optimizers in a class structure ###
import numpy as np

class Optimize():
    def __init__(self, guess = False):
        self.guess_random = guess

    def get_x(self):
        self.x = [i*self.h for i in range(self.N+1)]

    def initial_guess(self):
        self.z0 = np.zeros(self.N + 1)
        if self.guess_random == True:
            self.z0[0] = self.alpha;
            self.z0[self.N] = self.beta
            for i in range(1,self.N):
                self.z0[i] = np.random.uniform(low = 0, high = 10)

    def b(self,x):
        b_vec = np.zeros(self.N+1)
        b_vec[0] = self.alpha/self.hh; b_vec[-1] = self.beta/self.hh
        b_vec[1:-1] = self.hh*self.f(x[1:-1])
        return b_vec


    def setup_A(self):
        """
        Sets up the tridiagonal matrix which solves
        y''(x) = f(y(x)) numerically
        Input:
        - N (int)
        """
        N = self.N
        self.A = np.zeros((N+1,N+1))
        self.A[0,0] = 1.0; self.A[N,-1] = 1.0
        # set up matrix for inner points
        for i in range(1,N):
            self.A[i,i] = -2.0

        for i in range(0,N):
             self.A[i+1,i] = 1.0; # below diag
             self.A[i,i+1] = 1.0; # above diag

        # Modify for special rows
        self.A[0,1] = 0.; self.A[N,-2] = 0.

    def fixedpointODE(self,f, alpha, beta, N, tolerance):
        self.alpha, self.beta, self.N, self.f = alpha, beta, N, f;

        self.setup_A(); self.h = 1/N; self.hh = self.h**2

        E = 1; self.initial_guess(); z = self.z0
        while E > tolerance:
            z_new = np.linalg.solve(self.A,self.b(z))
            E = np.linalg.norm(self.h*(z_new - z))
            z = z_new
        print(E)
        self.get_x()
        return self.x, z


    def newtonODE(self,f, df, alpha, beta, N, tolerance):
        self.alpha, self.beta, self.N = alpha, beta, N;
        
        self.setup_A(N);
