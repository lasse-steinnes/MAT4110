import numpy as np
import matplotlib.pyplot as plt


def error_sine(c,k):
    error = ((k+1)**(-1/2))*((2*np.pi*k*np.exp(1))/((c-1)*(k+1)))**(k+1)
    return np.log(error)

def error_runge(c,k):
    error = ((10*k)/(c-1))**(k+1)
    return np.log(error)

k = np.linspace(1,100,100)
c = 300  # c is larger than 1 always # fix this
N = np.linspace(1,10,100)

plt.plot(k,error_sine(c,k),label = 'sin(x)');
plt.xlabel('k');
plt.ylabel('$\log({error})$');
plt.legend()
plt.show()

plt.plot(k,error_runge(c,k), label = 'runge');
plt.xlabel('k');
plt.ylabel('$\log({error})$');
plt.legend()
plt.show()
