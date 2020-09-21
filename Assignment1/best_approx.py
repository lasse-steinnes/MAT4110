### plot of best approximation interpolating polynomial ###
### Using basis functions
import numpy as np
import matplotlib.pyplot as plt

p = lambda x: np.exp(1) - 3/2 + x
f = lambda x: np.exp(x)

# make plot
x = np.linspace(0,1,1000)
plt.plot(x,p(x), label = 'p1')
plt.plot(x,f(x), label = 'f(x) = $e^{x}$')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
