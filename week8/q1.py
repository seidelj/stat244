import math

def lik(x, p):
    num = x * p * math.pow((1-p),(x-1)) * math.pow(x,(x-1))
    den = math.pow(x-1,(x-1))
    try:
        res = num/den
    except ZeroDivisionError:
        res = "undef"
    return res

def prob(x,p):
    return p * math.pow((1-p), (x-1))

for x in range(1,15):
    print "x={}: {}".format(x,lik(x,.7))

pr = []
for x in range(1,10):
    pr.append(prob(x, 1.0/x))
    print "x={}: {}".format(x, prob(x,1.0/x))

print sum(pr)
