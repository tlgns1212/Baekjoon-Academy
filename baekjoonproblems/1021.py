import sys
N,M = map(int,sys.stdin.readline().split())
qList = [i+1 for i in range(N)]
wanted = list(map(int,sys.stdin.readline().split()))
answer = 0
for i in wanted:            #2 , 9 , 5
    if i == qList[0]:
        qList.pop(0)
        N -= 1
    elif qList.index(i) <= len(qList)//2:
        for _ in range(qList.index(i)):
            qList.append(qList.pop(0))
            answer += 1
    else:
        for _ in range(N - qList.index(i)):
            qList.insert(0,qList.pop(-1))
            answer += 1
    if qList != []:
        if i == qList[0]:
            qList.pop(0)
            N -= 1
print(answer)
