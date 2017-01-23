from urllib.request import urlopen
from re import search

Permutations = []
def next_permutation(n):
    p = list(range(1,n+1))
    yield p
    test = True
    while test:
        i = n-1
        while i > 0 and p[i] <= p[i-1]:
            i-=1
        if i == 0:
            test = False
        else:
            j = n-1
            while j > i-1 and p[j] <= p[i-1]:
                j -= 1
            p[j], p[i-1] = p[i-1], p[j]
            p[i:] = p[-1:i-1:-1]
            yield p
Sum = 0
Gen = next_permutation(10)


with urlopen('http://pastebin.com/raw/JrBL9Rau') as f:
    for line in f:
        parameters = search("(\d+) (L|P) (\d+)", str(line))
        K, letter, N = int(parameters.group(1)), parameters.group(2), int(parameters.group(3))
        n = len(Permutations)
        if K > n:
            for _ in range(n, K):
                Permutations.append(list(next(Gen)))
        p = Permutations[K-1]
        if letter == 'L':
            Sum += p[N-1]
        elif letter == 'P':
            Sum += p.index(N)+1
    print(Sum)