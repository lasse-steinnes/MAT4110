# programme which runs the ODE_solvers
from ode import ODE_Solver
import numpy as np

N = int(input("Enter number of intervals:"));

print("Press 1 to run explicit euler")
print("Press 2 to run implicit euler")
print("Press 3 to run a 2 dimensional problem")
arg1 = input("Input number:");

## Declare
x0 = 1.0;
T = 2.0;
lambda_ = -5;


if int(arg1) == 1:
    solver = ODE_Solver(lambda_,x0, T, N,1)
    t,x = solver.explicit_euler()
    print(x)

elif int(arg1) == 2:
    solver = ODE_Solver(lambda_,x0, T, N,1)
    t,x = solver.implicit_eluer()
    print(x)

elif int(arg1) == 3:
    n = 2;
    x0 = np.transpose(np.array([1,0]))

    # set up lambda
    lambda_ = np.zeros((n), dtype = complex);
    lambda_[0] = 1j; lambda_[1] = 0.0-1j;

    # set up orthogonal matrix
    V = np.zeros((n,n), dtype=complex);
    V[0,0] = 1; V[1,0] = -1j; V[0,1] = 1; V[1,1] = 1j;
    V = 1/np.sqrt(2)*V

    # solve
    solver = ODE_Solver(lambda_,x0, T, N, n)
    t,x = solver.linear_system_EE(V)
    print(x)
