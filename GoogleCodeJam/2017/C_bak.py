import sys
from collections import deque

lines = []
i = 0
for line in sys.stdin:
    if i == 0:
        i += 1
        continue
    lines.append(tuple(map(int, line.rstrip('\n').split())))

for N, K in lines:
    maxi, mini = (N//2), ((N-1)//2)
    q = deque([maxi, mini])
    for _ in range(1, K):
        n = q.popleft()
        maxi, mini = n//2, (n-1)//2
        m = q.pop()
        L = []
        while m < maxi:
            L.append(m)
            if not q:
                break
            m = q.pop()
        q.append(maxi)
        q.extend(L[::-1])
        q.append(mini)
    print("Case #"+str(i)+": "+str(maxi)+" "+str(mini))
    i += 1
