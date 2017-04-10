import sys
from heapq import heapify, heappop, heappush

lines = []
i = 0
for line in sys.stdin:
    if i == 0:
        i += 1
        continue
    lines.append(tuple(map(int, line.rstrip('\n').split())))

for N, K in lines:
    maxi, mini = (N//2), ((N-1)//2)
    h = []
    heappush(h, -maxi)
    heappush(h, -mini)
    for _ in range(1, K):
        n = -heappop(h)
        maxi, mini = (n//2), ((n-1)//2)
        heappush(h, -maxi)
        heappush(h, -mini)
    print("Case #"+str(i)+": "+str(maxi)+" "+str(mini))
    i += 1
