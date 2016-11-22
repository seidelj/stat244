import math
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy.special import erf



t1 = np.arange(1.0, 600.0, 0.1,dtype=np.float128)

def lik(x, p):
    c = 1-p
    xminus1= x-1
    num = np.log(p) + np.log(x) + xminus1 * np.log(c) - xminus1 *np.log(1- 1/x)
    #num = np.log(x) + np.log(p) + xminus1 * np.log(c) * xminus1 + x * np.log(xminus1) - xminus1 * np.log(xminus1)
    #num = x * p * np.power(c,xminus1) * np.power(x,xminus1)
    #den = np.power(xminus1, xminus1)

    return np.e**num

def prob(x,p):
    return p * math.pow((1-p), (x-1))

for x in range(1,15):
    print "x={}: {}".format(x,lik(x,.01))

pr = []
for x in range(1,10):
    pr.append(prob(x, 1.0/x))
    print "x={}: {}".format(x, prob(x,1.0/x))

print sum(pr)

plt.plot(t1, lik(t1,.01), lw=2, label="")

right = []
for x in range(1,5):
    right.append(prob(float(x), .001))

print "right: {}".format(np.nansum(right))

left = []
for x in range(1, 489):
    left.append(prob(float(x), .001))

print "left: {}".format(1-np.nansum(left))

plt.show()


