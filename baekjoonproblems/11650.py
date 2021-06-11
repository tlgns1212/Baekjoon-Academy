import sys
N = int(sys.stdin.readline())
numList = []
for _ in range(N):
    numList.append(list(map(int,sys.stdin.readline().split())))
numList.sort()
for i in numList:
    print(i[0],i[1])