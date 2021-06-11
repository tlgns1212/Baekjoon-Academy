import sys
N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int,sys.stdin.readline().split())))
B = [0]*len(A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i][0]>A[j][0] and A[i][1]>A[j][1]:
            B[i] += 1
        elif A[i][0]<A[j][0] and A[i][1]<A[j][1]:
            B[j] += 1
winner = 1
C = [0] *len(B)
for i in range(len(B),-1,-1):
    count = 0
    for j in range(len(B)):
        if i == B[j]:
            C[j] = winner
            count += 1
    winner += count
print(C.split(" "))