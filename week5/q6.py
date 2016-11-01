import numpy as np
import matplotlib.pyplot as plt

def f(t, c):
    return (1 + c*t)/2

t1 = np.arange(0, 1.0, 0.1)

plt.plot(t1, f(t1, -.5), label="-.5")
plt.plot(t1, f(t1, .5), label=".5")
plt.plot(t1, f(t1, 0), label="1")

plt.legend(loc='best')
plt.show()
