import sys
N,P = map(int,(sys.stdin.readline().split()))
all = []
used = [True]*P
for _ in range(P):
    all.append(list(map(int,sys.stdin.readline().split())))
i = 0
answer = 0
now = all[0][1]
print()
print()
all.pop(0)
while 1:
    for j in range(len(all)):
        if all[j][0] == now and all[j][1] == 2:
            now = all[j][1]
            print(all.pop(j))
            break
        elif j == len(all)-1:
            i += 1
    if now == 2:
        now = all[i][1]
        answer += 1
    if i > len(all):
        break
print(answer)
