import sys
N, M = map(int,sys.stdin.readline().split())
plague = []
for _ in range(N):
    plague.append(list(map(int,sys.stdin.readline().split())))
print(plague)
# 0,0에서 위, 좌를 어떻게 제외할까????? 
# 하나씩 제외하면 경우의 수가 얼마나 많은데...