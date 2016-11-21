import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy.special import erf
import math

def pdf(x):
    return x * np.exp(-x)

t1 = np.arange(0.0, 8.0, 0.1)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.ylabel("$f(x \mid \\theta_0)$", fontsize=18)
plt.xlabel("$x$", fontsize=18)
plt.plot(t1, pdf(t1), lw=2, label="")

plt.show()
