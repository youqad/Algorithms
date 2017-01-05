from urllib.request import urlopen
from collections import deque
import ast

Sum = 0

with urlopen('http://pastebin.com/raw/VPfpDRVW') as f:
    for line in f:
        L = deque(ast.literal_eval(line.strip().decode("utf-8")))
        n = len(L)
        counter = 0
        while any(L[i]>L[i+1] for i in range(n-1)) and counter < n:
            L.rotate()
            counter+=1
        if counter == n:
            counter = -1
        Sum += counter

print(Sum)