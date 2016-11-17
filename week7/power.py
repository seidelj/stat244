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
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.ylabel("$\pi$", fontsize=18)
plt.xlabel("$H_a$: $u_1$", fontsize=18)
plt.plot(t1, power_fnc(t1), lw=4, label="")

plt.show()
