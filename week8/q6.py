
r1 = [5, 12, 2]
r2 = [4, 42, 15]
r3 = [1, 14, 10]

arr = []
arr.append(r1)
arr.append(r2)
arr.append(r3)

total = sum(sum(arr[x]) for x in range(len(r1)))

chisquare = []
for i in range(0,3):
    rTotal = sum(arr[i])
    for j in range(0,3):
        cTotal = arr[0][j]+arr[1][j] + arr[2][j]
        expected = (rTotal*cTotal)/float(total)
        num = (arr[i][j] - expected)**2
        chisquare.append(float(num)/expected)
print sum(chisquare)

