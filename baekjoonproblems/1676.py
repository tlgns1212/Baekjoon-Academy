import sys
N = int(sys.stdin.readline())
sum = 1
cnt = 0
for i in range(N):
    sum *= (i+1)
strsum = str(sum)
for i in strsum[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)