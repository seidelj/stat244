import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy.special import erf
import math

def power_fnc(x):
    C = 9.29
    mu = x
    sigma = 2
    znum = C - mu
    zden = (sigma * math.sqrt(2))
    z = znum / zden
    err = erf(z)
    return 1 - (.5 * (1 + err))


t1 = np.arange(6.0, 15.0, 0.1)
plt.plot(t1, power_fnc(t1), label="")

plt.show()