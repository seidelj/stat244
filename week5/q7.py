import numpy as np
import matplotlib.pyplot as plt

def cX(t):
    num = t*t - 1
    denom = 3
    return num/denom

def X(t):
    num = 2*(t*t) -3*t +1
    denom = 6
    return num/denom

t1 = np.arange(0.0, 5.0, 0.1)

plt.plot(t1, cX(t1), label="cX")
plt.plot(t1, X(t1), label="X")

plt.legend(loc='best')
plt.show()
