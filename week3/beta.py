import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

fig, ax=plt.subplots(1,1)

a,b = 4, 98

mean, var, skew, kurt = beta.stats(a,b, moments='mvsk')

x = np.linspace(beta.ppf(0.001, a,b), beta.ppf(0.99,a,b), 100)

ax.plot(x, beta.pdf(x,a,b), 'r-', lw=5, alpha=.6, label='case 1')

a, b = 3.5, 102

mean, var, skew, kurt = beta.stats(a,b, moments='mvsk')

x = np.linspace(beta.ppf(0.001, a,b), beta.ppf(0.99,a,b), 100)

ax.plot(x, beta.pdf(x,a,b), 'b-', lw=5, alpha=.6, label='case 2')

ax.legend(loc='best', frameon=False)
plt.show()
