# 미완
T = int(input())
for _ in range(T):
    count = 0
    M, N, K = map(int,input().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        m, n = map(int,input().split())
        farm[n][m] = 1
    if farm[0][0] == 1:
        count += 1
        farm[0][0] = 2
        if farm[1][0] == 1:
            farm[1][0] = 2
        elif farm[0][1] == 1:
            farm[0][1] = 2
    if (farm[n - 2][m-1] == 2 or farm[n-1][m - 2] == 2) and farm[n-1][m-1] == 1:
        farm[n-1][m-1] = 2
    elif farm[n-1][m-1] == 1:
        count += 1
        farm[n-1][m-1] = 2
    if (farm[n-1][1] == 2 or farm[n-2][0] == 2) and farm[n-1][0] == 1:
        farm[n-1][0] = 2
    elif farm[n-1][0] == 1:
        count += 1
        farm[n-1][0] = 2
    if (farm[1][m-1] == 2 or farm[0][m-2] == 2) and farm[0][m-1] == 1:
        farm[0][m-1] = 2
    elif farm[0][m-1] == 1:
        count += 1
        farm[0][m-1] = 2
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if (farm[i-1][j] == 2 or farm[i][j-1] == 2 or farm[i+1][j] == 2 or farm[i][j+1] == 2) and farm[i][j] == 1:
                farm[i][j]= 2
            elif farm[i][j] == 1:
                count += 1
                farm[i][j] = 2
    
    print(count)
