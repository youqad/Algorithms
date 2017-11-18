T = int(input())
i = 1
for _ in range(T):
    D, N = [int(s) for s in input().split()]
    time = 0
    for _ in range(N):
        K, S = [int(s) for s in input().split()]
        time = max((D-K)/S, time)
    print("Case #"+str(i)+": "+str(format(D/time, '.6f')))
    i += 1
