import numpy as np
import matplotlib.pyplot as plt

def f(t, c):
    numo =  (c*c)*((t*t) - (4 * t) +6)
    denom = 6
    return numo/denom

t1 = np.arange(0.0, 5.0, 0.1)

plt.plot(t1, f(t1,1), label="Theta=1")
plt.plot(t1, f(t1,.5), label="Theta=.5")
plt.plot(t1, f(t1, .333), label="Theta=.333")

plt.legend(loc='best')
plt.show()
