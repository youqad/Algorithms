n, m = map(int, input().split())
G = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
x = int(input())
marked = [False]*(n+1)
P = [x]
marked[x] = True

while P:
    v = P.pop()
    for w in G[v]:
        if not marked[w]:
            marked[w] = True
            P.append(w)

print((n-sum(int(b) for b in marked)))
