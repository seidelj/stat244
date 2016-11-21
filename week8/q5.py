import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy.special import erf
import math

def compChiSquar(x, np):
    num = (float(x) - np)**2
    den = np
    return float(num)/den

obs = [121,120,79,33]
exp = [119.5, 122.26, 81.5, 30.5]
restr = ""
comps = []
for x in range(0,len(obs)):
    comp = compChiSquar(obs[x], exp[x])
    comps.append(comp)
    restr += "&{}".format(round(comp,2))

print restr
print sum(comps)
