from urllib.request import urlopen

depth = 0
max_depth = 0

with urlopen('http://pastebin.com/raw/gCC8dE4h') as f:
    L = list(f.readline().strip())
    print(L)
    for brace in L:
        if brace == 123:
            depth+=1
            if depth > max_depth:
                max_depth = depth
        elif brace == 125:
            depth-=1


print(max_depth)