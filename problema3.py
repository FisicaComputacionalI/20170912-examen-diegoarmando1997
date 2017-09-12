import numpy as np
import matplotlib.pyplot as plt
def f(x):
   return 2.5*np.sin(x)+2015
def g(x):
   return x+1997
x1 = np.arange(0.0, 20.0, 0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(x1, f(x1), 'mo', x1, g(x1), 'k')
plt.subplot(212)
plt.plot(x1, f(x1), 'gs')
plt.savefig('graficasproblema3.png')
