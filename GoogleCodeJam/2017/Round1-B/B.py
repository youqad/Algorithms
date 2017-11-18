col = frozenset(['R', 'B', 'Y'])

def succ(fs):
    global col
    avail = col - fs
    yield avail
    if len(avail) != 1:
        for c in avail:
            yield frozenset([c])

def fs_to_str(fs):
    if 'B' in fs:
        if 'Y' in fs:
            return 'G'
        if 'R' in fs:
            return 'V'
        return 'B'
    if 'R' in fs:
        if 'Y' in fs:
            return 'O'
        return 'R'
    return 'Y'


def chain(s, fs, set_col):
    print(len(s))
    print(set_col)
    if not set_col:
        return s + fs_to_str(fs)
    for suc in succ(fs):
        if suc in set_col:
            set_col[suc] -= 1
            if set_col[suc] <= 0:
                del set_col[suc]
            res = chain(s + fs_to_str(fs), suc, set_col)
            if res is not None or len(suc) == 2:
                return res
            if suc in set_col:
                set_col[suc] += 1
            else:
                set_col[suc] = 1
    return None


T = int(input())
i = 1
for _ in range(T):
    N, R, O, Y, G, B, V = [int(s) for s in input().split()]
    set_col = dict()
    if R:
        set_col[frozenset(['R'])] = R
    if B:
        set_col[frozenset(['B'])] = B
    if Y:
        set_col[frozenset(['Y'])] = Y
    if O:
        set_col[frozenset(['R', 'Y'])] = R
    if V:
        set_col[frozenset(['R', 'B'])] = V
    if G:
        set_col[frozenset(['Y', 'B'])] = G

    fs = list(set_col.keys())[0]
    set_col[fs] -= 1
    if set_col[fs] == 0:
        del set_col[fs]
    resu = chain("", fs, set_col)

    if resu is None:
        resu = "IMPOSSIBLE"

    print("Case #"+str(i)+": "+resu)
    i += 1
