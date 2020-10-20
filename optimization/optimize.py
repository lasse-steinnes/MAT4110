### Write an optimization class ###
## With steepest descent and Newton's method
import numpy as np

class Optimization_Quadratic():
    """
    Class with methods to find minima of a quadratic function
    f(x) = 1/2 transpose(x)Ax - transpose(b) + c
    """
    def __init__(self,A,b,c):
        """
        Set initial params:
        input:
        A - matrix n times n dims
        b = vector n dims
        """
        self.A = A
        self.b = b
        self.c = c

    def f(self,vec):
        return 1/2*np.dot(vec.T,self.A@vec) - self.b.T + self.c

    def check_pos_def(self):
        """
        Check if the matrix is positive definite
        meaning all eigenvalues are larger than 0)
        """
        return np.all(np.linalg.eigvals(self.A) > 0)

    def steepest_descent(self,x):
        """
        Uses steepest_descent with direct line search
        """
        A, b = self.A, self.b;

        # Check if symmetric and positive definite
        if (self.check_pos_def() == False) or np.any(A != A.T):
            raise ValueError("A needs to be symmetric positive definite."
            + " Cannot ensure existance of global minimum")

        dk = -(A@x - b)  # set first step

        k = 0
        # for exact line search
        while np.linalg.norm(dk) > 1e-12:  #setting a tolerance for convergence
            alpha = np.dot(dk.T,dk)/np.dot(dk.T,A@dk)
            x = x + alpha*dk
            dk = -(A@x - b)
            k = k + 1

        return x, self.f(x)


    def newtons_method(self, x):
        A, b = self.A, self.b;

        # Check if symmetric and positive definite
        if (self.check_pos_def() == False) or np.any(A != A.T):
            raise ValueError("A needs to be symmetric positive definite."
            + " Cannot ensure existance of global minimum")

        grad_f = A@x - b
        dk = -np.linalg.inv(A)@grad_f               # set first step

        k = 0
        # for exact line search
        while np.linalg.norm(dk) > 1e-12:  #setting a tolerance for convergence
            alpha = np.dot(dk.T,dk)/np.dot(dk.T,A@dk)
            x = x + alpha*dk
            grad_f = A@x - b
            dk = -np.linalg.inv(A)@grad_f
            k = k + 1

        return x, self.f(x)

"""
class Optimization_General():
    """
    #Takes in a function R^n --> R and find it

    """
    def __init__(self,f):
        """
    #    Set initial params. Send in f as a matrix, e.g. if you have two params f is
        """
        self.f = f

    def steepest_descent(self,x):

        dk = -np.grad(f)

        k = 0
        while np.linalg.norm(dk) > 1e-12: # Setting a tolerance for convergence




    def newtons_method(self,x):
    """
