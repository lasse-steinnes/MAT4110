### Write optimizers in a class structure ###
import numpy as np
import time

class Optimize():
    def __init__(self, guess = False):
        self.guess_random = guess

    def get_x(self):
        """
        function that generates x
        """
        self.x = [i*self.h for i in range(self.N+1)]
        self.x = np.array(self.x)

    def initial_guess(self):
        """
        if guess_random = True, generates a random guess
        othewise just intializes boundary conditions
        """
        self.z0 = np.zeros(self.N + 1)
        self.z0[0] = self.alpha;
        self.z0[self.N] = self.beta
        if self.guess_random == True:
            for i in range(1,self.N):
                self.z0[i] = np.random.uniform(low = 0, high = 10)

    def b(self,x):
        """
        Set up the right hand side
        """
        b_vec = np.zeros(self.N+1)
        b_vec[0] = self.alpha; b_vec[-1] = self.beta
        b_vec[1:-1] = self.hh*self.f(x[1:-1])
        return b_vec

    def grad_b(self,x):
        """
        Calculates the gradient of b
        """
        g_b = np.zeros((self.N+1,self.N+1))
        for i in range(1,self.N):
            g_b[i,i] = self.df(x[i])
        return g_b

    def g(self,x):
        """
        Calculates the fixed point iteration
        """
        g_vec = self.A@x - self.b(x)
        return g_vec


    def grad_g(self,x):
        """
        Calculates the gradient of g
        """
        return self.A - self.hh*self.grad_b(x)

    def setup_A(self):
        """
        Sets up the tridiagonal matrix which solves
        y''(x) = f(y(x)) numerically
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
        """
        Calculates z which solves the ODE y''(x) = f(y(x))
        Input:
        - f (function)
        - alpha: z0 (float)
        - beta: zN (float)
        - N: number of intervals (int)
        """
        self.alpha, self.beta, self.N, self.f = alpha, beta, N, f;

        self.setup_A(); self.h = 1/N; self.hh = self.h**2;

        E = 1; self.initial_guess(); z = self.z0
        time.clock(); iterations = 0
        while E > tolerance:
            z_new = np.linalg.solve(self.A,self.b(z))
            E = np.linalg.norm(self.h*(z_new - z))
            z = z_new
            iterations = iterations + 1
        print("Runtime fixedpointODE: {:.6} ms".format(time.clock()*1000))
        print("Number of iterations: {:d}\n".format(iterations))
        self.get_x()
        return self.x, z


    def newtonODE(self,f, df, alpha, beta, N, tolerance):
        """
        Calculates z which solves the ODE y''(x) = f(y(x))
        Input:
        - f (function)
        - df (derivative of function)
        - alpha: z0 (float)
        - beta: zN (float)
        - N: number of intervals (int)
        """
        self.alpha, self.beta, self.N = alpha, beta, N;
        self.f, self.df = f, df;
        self.setup_A(); self.h = 1/N; self.hh = self.h**2;

        E = 100; self.initial_guess(); z = self.z0
        time.clock()*1000; iterations = 0
        while E > tolerance:
            rhs = self.grad_g(z)@z - self.g(z)
            z_new = np.linalg.solve(self.grad_g(z),rhs)
            E = np.linalg.norm(self.h*(z_new - z))
            z = z_new
            iterations = iterations + 1
        print("Runtime fixedpointODE: {:.6} ms".format(time.clock()*1000))
        print("Number of iterations: {:d}\n".format(iterations))
        self.get_x()
        return self.x,z
