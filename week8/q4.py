import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy.special import erf
import math

def binompdf(x,n,p):
    a = math.factorial(n)
    b = math.factorial(x)
    c = math.factorial(n-x)
    nchoosek = float(a) / (b*c)
    return nchoosek * p**x * (1-p)**(n-x) * 215

def compChiSquar(x, np):
    num = (float(x) - np)**2
    den = np
    return float(num)/den

restr = ""
npList = []
for x in range(0,6):
    npList.append((int(round(binompdf(x, 5, .31)))))
    restr += "&{}".format(int(round(binompdf(x,5, .31))))

print restr

obs = [87,11,51,42,20,4]
restr = ""
comps = []
for x in range(0,6):
    comp = compChiSquar(obs[x], npList[x])
    comps.append(comp)
    restr += "&{}".format(round(comp,2))

print restr
print sum(comps)
