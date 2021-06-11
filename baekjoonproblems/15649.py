N,M = map(int,input().split())
i = 1
while 1:
    k = 0
    for j in range(M):
        print(i,end=" ")
    print()
    i+=1
    if i > N:
        break