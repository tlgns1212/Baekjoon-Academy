N, K = map(int,input().split())
cirList = []
answer = []
for i in range(N):
    cirList.append(i+1)
i = 0
while cirList != []:
    i += K-1
    if i >= len(cirList):
        i %= len(cirList)
    answer.append(cirList.pop(i))
print("<",end = "")
print(*answer,sep = ", ",end = ">")