from functools import reduce

i = 1
T = int(input())
for _ in range(T):
    N, P = [int(s) for s in input().split()]
    S = [int(s) for s in input().split()]
    K = []
    for _ in range(N):
        K.append([int(s) for s in input().split()])
    for n in range(N):
        for p in range(P):
            k, s = K[n][p], S[n]
            sk = set()
            m = k//s
            j = 0
            cont = True
            stop = False
            stop2 = False
            while cont:
                local_test = False
                if 0.9*(m+j)*s <= k <= 1.1*(m+j)*s:
                    sk.add(m+j)
                    local_test = True
                if 0.9*(m-j)*s <= k <= 1.1*(m-j)*s:
                    sk.add(m-j)
                    local_test = True
                j += 1
                if not local_test:
                    if not stop:
                        stop = True
                    elif stop:
                        cont = False

            K[n][p] = sk
    count = 0
    Set = reduce(set.intersection, [reduce(set.union, l) for l in K])
    while Set:
        k = Set.pop()
        for n in range(N):
            for p in range(P):
                if k in K[n][p]:
                    K[n][p] = set()
                    break
        count += 1
        Set = reduce(set.intersection, [reduce(set.union, l) for l in K])

    print("Case #"+str(i)+": "+str(count))
    i += 1
