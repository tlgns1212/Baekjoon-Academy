N,M = map(int, input().split())
A = list(map(int,input().split()))
close = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            if (M - (A[i]+A[j]+A[k])) < (M-close):
                if M - (A[i]+A[j]+A[k]) >= 0:
                    close = A[i]+A[j]+A[k]
print(close)