All = []
n = int(input('::'))
for i in range (1,(n**2)+1):
    All.append(3*i)
    
nAll = []
for i in range(1, n+1):
    nAll.append(All[:2*i -1])
    for x in All[:2*i -1]:
        All.remove(x)

for i in range(1, n+1):
    print(nAll[i-1], 'sum =', sum(nAll[i-1]))