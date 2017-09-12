import numpy as np
import matplotlib.pyplot as plt
def f(x):
   return 2.5*np.sin(x)+2015
x1 = np.arange(0.0, 10.0, 0.1)
plt.plot(x1, f(x1), 'mo', x1, f(x1), 'k')
plt.savefig('graficaproblema2.png')
