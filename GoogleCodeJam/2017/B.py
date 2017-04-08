import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def tidy(n):
    l = len(n)
    if l == 1:
        return n
    k = 0
    for i in range(1, l):
        if int(n[i-1]) > int(n[i]):
            j = i-1
            c = int(n[i-1])-1
            c_new = str(c)
            break
        elif int(n[i-1]) == int(n[i]):
            k += 1
        else:
            k = 0
    else:
        return n
    if c > 0:
        return (n[:j-k] + c_new + '9'*(k+l-j-1))
    else:
        return '9'*(k+l-j-1)


i = 1
for n in lines[1:]:
    print("Case #"+str(i)+": "+tidy(n))
    i += 1
