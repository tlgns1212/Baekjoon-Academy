N,K = map(int,(input().split()))
count = 0
while True:
    countWalk = K-N
    
    if abs(K - (N-1)*2) < abs(K - (N)*2):
        small = 0,abs(K - (N-1)*2)
    elif abs(K - (N+1)*2) < abs(K - (N)*2) and (K - (N+1)*2) <= (K - N*4):
        small = 2,abs(K - (N+1)*2)
    else:
        small = 1, abs(K - N*2)
    if abs(K - (N-1)*2) < countWalk:
        if small[0] == 0:
            N -= 1
            N *= 2
            count += 2
            if N == K:
                break
        elif small[0] == 2:
            N += 1
            N *= 2
            count += 2
            if N == K:
                break
        else:
            N *= 2
            count += 1
            if N == K:
                break
    elif K > N:
        if N == K:
            break
        N+= 1
        count += 1
    else:
        if N == K:
            break
        N-= 1
        count += 1
print(count)
