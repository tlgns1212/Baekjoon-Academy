N,L = map(int,input().split())
maze = [[0]*N]*N
boolmaze1 = [True]*N
boolmaze2 = [True]*N
for i in range(N):
    temp = list(map(int,input().split()))
    maze[i] = temp
for i in range(N):
    compare = maze[i][0]
    cnt_same = 1
    for j in range(1,N):
        if compare == maze[i][j]:
            cnt_same += 1
        elif compare != maze[i][j]:
            if cnt_same < 0:
                boolmaze1[i] = False
                break
            elif compare == maze[i][j] + 1:
                cnt_same = 1 - L
            elif compare + 1 == maze[i][j]:
                if cnt_same < L:
                    boolmaze1[i] = False
                    break
                else:
                    cnt_same = 1
            else:
                boolmaze1[i] = False
                break
        if cnt_same < 0 and j == N-1:
            boolmaze1[i] = False
        compare = maze[i][j]

    compare = maze[0][i]
    cnt_same = 1
    for j in range(1,N):
        if compare == maze[j][i]:
            cnt_same += 1
        elif compare != maze[j][i]:
            if cnt_same < 0:
                boolmaze2[i] = False
                break
            elif compare == maze[j][i] + 1:
                cnt_same = 1 - L
            elif compare + 1 == maze[j][i]:
                if cnt_same < L:
                    boolmaze2[i] = False
                    break
                else:
                    cnt_same = 1
            else:
                boolmaze2[i] = False
                break
        if cnt_same < 0 and j == N-1:
            boolmaze2[i] = False
        compare = maze[j][i]
a = boolmaze1.count(True)
b = boolmaze2.count(True)
print(a+b)

#import sys

#N,L = map(int,sys.stdin.readline().split())
#maze = [[0]*N]*N
#boolmaze1 = [True]*N
#boolmaze2 = [True]*N
#for i in range(N):
#    temp = list(map(int,sys.stdin.readline().split()))
#    maze[i] = temp
#for i in range(N):
#    compare = maze[i][0]
#    cnt_same = 1
#    for j in range(1,N):
#        if compare == maze[i][j]:
#            cnt_same += 1
#        elif compare != maze[i][j]:
#            if cnt_same < 0:
#                boolmaze1[i] = False
#                break
#            elif compare == maze[i][j] + 1:
#                cnt_same = 1 - L
#            elif compare + 1 == maze[i][j]:
#                if cnt_same < L:
#                    boolmaze1[i] = False
#                    break
#                else:
#                    cnt_same = 1
#            else:
#                boolmaze1[i] = False
#                break
#        if cnt_same < 0 and j == N-1:
#            boolmaze1[i] = False
#        compare = maze[i][j]

#    compare = maze[0][i]
#    cnt_same = 1
#    for j in range(1,N):
#        if compare == maze[j][i]:
#            cnt_same += 1
#        elif compare != maze[j][i]:
#            if cnt_same < 0:
#                boolmaze2[i] = False
#                break
#            elif compare == maze[j][i] + 1:
#                cnt_same = 1 - L
#            elif compare + 1 == maze[j][i]:
#                if cnt_same < L:
#                    boolmaze2[i] = False
#                    break
#                else:
#                    cnt_same = 1
#            else:
#                boolmaze2[i] = False
#                break
#        if cnt_same < 0 and j == N-1:
#            boolmaze2[i] = False
#        compare = maze[j][i]
#a = boolmaze1.count(True)
#b = boolmaze2.count(True)
#print(a+b)