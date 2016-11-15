import os, csv


def createtab(row):
    string = ""
    for r in row:
        string += "&{}".format(r)
    return string

with open("likelihoodratios.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    pixel = []
    theta0 = []
    theta6 = []
    ratio = []
    for row in reader:
        pixel.append(row[0])
        theta0.append(row[1])
        theta6.append(row[2])
        ratio.append(row[3])

print createtab(pixel)
print createtab(theta0)
print createtab(theta6)
print createtab(ratio)
