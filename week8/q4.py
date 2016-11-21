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

restr = ""
for x in range(0,6):
    restr += "&{}".format(int(round(binompdf(x,5, .31))))

print restr


