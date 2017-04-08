import sys

sequence = ['0', '1']

def generate_seq(k):
    global sequence, count
    lgk = floor(log2(k+2))
    l = len(sequence[-1])
    lim = 2**l
    while k > l:
        L0 = [c+'0' for c in sequence[-lim:]]
        L1 = [c+'1' for c in sequence[-lim:]]
        sequence.extend(L0)
        sequence.extend(L1)
        l += 1
        lim *= 2
    return sequence[k]


lines = []
i = 0
for line in sys.stdin:
    if i == 0:
        i += 1
        continue
    lines.append(tuple(map(int, line.rstrip('\n').split())))


i = 1

for N, K in lines:
    if K == 1:
        print("Case #"+str(i)+": "+str(N//2)+" "+str((N-1)//2))
        i += 1
        continue
    n = N
    for j in generate_seq(K-2):
        if int(j):
            n -= 1
        n //= 2
    # print(str(K) + " " + generate_seq(K-2))
    print("Case #"+str(i)+": "+str(n//2)+" "+str((n-1)//2))
    i += 1
