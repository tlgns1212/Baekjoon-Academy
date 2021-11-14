N = int(input())
answer = 0
for i in range(N//2,N):
    answer += i
    j = i
    while j!=0:
        #print(i, "======",end="")
        answer += j % 10
        #print(answer)
        j //= 10
    if answer == N:
        print(i)
        break
    answer = 0
if answer != N:
    print(0)