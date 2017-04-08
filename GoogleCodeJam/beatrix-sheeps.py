import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.rstrip('\n')))


def last_num(N):
    already_seen = [False for _ in range(10)]
    k = 1
    while not all(already_seen):
        kN = k*N
        for d in str(kN):
            if not already_seen[int(d)]:
                already_seen[int(d)] = True
                if all(already_seen):
                    last = kN
                    break
        k += 1
    return last


i = 1
for N in lines[1:]:
    if N == 0:
        print("Case #"+str(i)+": INSOMNIA")
    else:
        print("Case #"+str(i)+": "+str(last_num(N)))
    i += 1
