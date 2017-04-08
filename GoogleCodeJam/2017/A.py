import sys
from collections import deque

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def inverse(s):
    if s == '+':
        return '-'
    elif s == '-':
        return '+'


def count_min(s, K):
    n = len(s)+1
    if '-' not in s:
        return 0
    elif '+' in s and K >= n-1:
        return -1
    q = deque([(s, 0)])
    stop = False
    already_seen = {s}
    found = -1
    while (not stop) and q:
        u, depth = q.popleft()
        for i in range(K, n):
            new = u[:i-K]+''.join(inverse(j) for j in u[i-K:i])+u[i:]
            # print(new)
            if '-' not in new:
                found = depth+1
                stop = True
                break
            elif new not in already_seen:
                q.append((new, depth+1))
                already_seen.add(new)
    return found


i = 1
for l in lines[1:]:
    s, K = l.split()
    K = int(K)
    c = count_min(s, K)
    if c > -1:
        print("Case #"+str(i)+": "+str(c))
    else:
        print("Case #"+str(i)+": IMPOSSIBLE")
    i += 1
