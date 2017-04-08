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


def count_min(s):
    n = len(s)+1
    if '-' not in s:
        return 0
    q = deque([(s, 0)])
    stop = False
    already_seen = {s}
    while not stop:
        u, depth = q.popleft()
        for i in range(n):
            new = ''.join(inverse(j) for j in u[i-1::-1])+u[i:]
            print(new)
            if '-' not in new:
                found = depth+1
                stop = True
                break
            elif new not in already_seen:
                q.append((new, depth+1))
                already_seen.add(new)
    return found


i = 1
for s in lines[1:]:
    print("Case #"+str(i)+": "+str(count_min(s)))
    i += 1
