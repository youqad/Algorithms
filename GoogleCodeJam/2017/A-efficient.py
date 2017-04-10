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
    L = [-1 for _ in range(n)]
    c = s[:K].count('-')
    if c > K/2:
        L[K] = c
    for i in range(K+1, n):
        if s[i-K] == '-':
            c -= 1
        if s[i-1] == '-':
            c += 1
        if c > K/2:
            L[i] = c
    count = 0
    while '-' in s:
        if all(c < 0 for c in L):
            return -1
        else:
            maxi = max(L)
            i = L.index(maxi)
            if K-maxi > K/2:
                L[i] = K - maxi
            else:
                L[i] = -1
            s = s[:i-K]+''.join(inverse(j) for j in s[i-K:i])+s[i:]
            print(s)
            print(L)
            for k in range(1, K):
                if i-k >= K:
                    cc = s[i-K:i-k].count('-')
                    if L[i-k] - (K-k-cc) + cc > K/2:
                        L[i-k] += -(K-k-cc) + cc
                    else:
                        L[i-k] = -1
                if i+k < n:
                    cc = s[i-K+k:i].count('-')
                    if L[i+k]-(K-k-c) + c > K/2:
                        L[i+k] += -(K-k-c) + c
                    else:
                        L[i+k] = -1
            count += 1
    return count


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
