from urllib.request import urlopen
with urlopen('https://gist.githubusercontent.com/anonymous/7bbd0959b81b2e33589f00adce7a1b2b/raw/a573b4d0c38d6ca367d407c29ea7cec08871252f/gistfile1.txt') as f:
    L = sorted([int(i) for i in f.read().split()])
    S = set(L)
    n =  len(L)
    maxi = 2
    for i in range(n-1):
        for j in range(i+1, n):
            d = L[j] - L[i]
            k = 2
            while L[i]+k*d in S:
                k+=1
            if k > maxi:
                maxi = k
    print(maxi)



# with urlopen('https://gist.githubusercontent.com/anonymous/7bbd0959b81b2e33589f00adce7a1b2b/raw/a573b4d0c38d6ca367d407c29ea7cec08871252f/gistfile1.txt') as f:
#     L = [int(i) for i in f.read().split()]
#     n =  len(L)
#     maxi, X = 1, []
#     for i in range(1, 2**n):
#         #print(i)
#         binary_subset = ('{:0'+str(n)+'b}').format(i)
#         if sum(int(j) for j in binary_subset) <= 2:
#             continue
#         list_subset = sorted([L[j] for j in range(n) if bool(int(binary_subset[j]))])
#         length_subset = len(list_subset)
#         d = list_subset[1] - list_subset[0]
#         for j in range(1, length_subset-1):
#             if list_subset[j+1] - list_subset[j] != d:
#                 break
#         else:
#             if length_subset > maxi:
#                 X = list_subset
#             maxi = max(length_subset, maxi)
#     print(maxi)


