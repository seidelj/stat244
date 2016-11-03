import numpy as np
import matplotlib.pyplot as plt

def g(x,s):
    abdiff = sum([abs(sn - x) for sn in s])
    return abdiff

def X(t):
    num = 2*(t*t) -3*t +1
    denom = 6
    return num/denom

t1 = np.arange(0.0, 5.0, 0.1)
X  = [1,2,4,3,1,0,3]
X2 = [0,1,2,3,4,5,5]
plt.plot(t1, g(t1,X), label="X=[0,1,1,2,3,3,4]")
plt.plot(t1, g(t1,X2), label="X=[0,1,2,3,4,5,5]")

plt.legend(loc='best')
plt.show()
