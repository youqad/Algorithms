from math import sqrt
from scipy.special import cbrt

def whats_left(i):
    sqrti = sqrt(i)
    if sqrti == int(sqrti):
        return 0
    cbrti = cbrt(i)
    if cbrti == int(cbrti):
        return 0
    return 1

    
print(sum(map(int, str(sum(map(whats_left,range(1,10**6)))))))
