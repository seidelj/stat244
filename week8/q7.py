import math

_LAM=.7
number = [x for x in range(0, 7)]
obs = [144, 91, 32, 11, 2, 0, 0]

def get_expected(x, lam):
    prob = math.exp(-lam) * (lam**x/math.factorial(x))
    return prob * sum(obs)

def get_comp_chisq(obs, expd):
    return (obs-expd)**2 / expd

expected = []
for x in number:
    value = get_expected(x, _LAM)
    expected.append(value)

groupExpected = []
temp = [0]
for x in expected:
    if x > 5:
        groupExpected.append(x)
    else:
        temp.append(x)

groupExpected.append(sum(temp))

groupObs = []
for x in range(len(groupExpected)-1):
    groupObs.append(obs.pop(0))

groupObs.append(sum(obs))

components = []
for x in range(len(groupObs)):
    components.append(get_comp_chisq(groupObs[x], groupExpected[x]))

expStr = ""
for x in groupExpected:
    expStr += "&{:1.2f}".format(x)
compStr = ""
for x in components:
    compStr += "&{:1.2f}".format(x)

print expStr
print compStr
print sum(components)
