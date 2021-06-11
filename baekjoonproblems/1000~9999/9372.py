#import sys
#T = int(sys.stdin.readline())
#for _ in range(T):
#    N,M = map(int,sys.stdin.readline().split())
#    air = [[0]*N]*N
#    print(air)
#    for _ in range(M):
#        a = list(map(int,sys.stdin.readline().split()))
#        air[a[0]][a[1]] = 1
#        air[a[1]][a[0]] = 1
#    # 이건 모르겠네


#for i in range(64):
#    n,m = i//8,i%8
#    if a[n][m] == 0:
#        a[n][m] = 1
#    for j in range(8):
#        n,m = j//8,j%8
#    if a[n][m] == 0:
#        if a[n][m] == 0:
#        for k in range(8):
#            n,m = i//8,i%8    
#            if a[n][m] == 0:
#                # 확인 알고리즘
#            a[n][m] = 0
#        a[n][m] = 0
#    a[n][m] = 0

#N,M = map(int,input().split(' '))
#a = [[int(x) for x in input().split()]for y in range(N)]
#count=0
#for i in range(N*M):
#    n,m = i//M,i%N
#    if a[n][m] == 0:
#        a[n][m] = 1
#    for j in range(N):
#        n,m = j//M,j%N
#        if a[n][m] == 0:
#            a[n][m] == 1:
#            for k in range(8):
#                n,m = i//M,i%N    
#                if a[n][m] == 0:
#                    a[n][m] = 1
#                    count+=1
#                a[n][m] = 0
#            a[n][m] = 0
#        a[n][m] = 0

#print(count)