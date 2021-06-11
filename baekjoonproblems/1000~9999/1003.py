#def fibonacci(n):
#    if n == 0:
#        count[0] += 1
#        return 0
#    elif n == 1:
#        count[1] += 1
#        return 1
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)


#import sys
#T = int(sys.stdin.readline())
#for _ in range(T):
#    count = [0,0]
#    N = int(sys.stdin.readline())
#    fibonacci(N)
#    print(count[0],count[1])

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a = []
    sum = 1
    sum1 = 1
    N = int(sys.stdin.readline())
    if N == 0:
        sum = 0
        print(1,0,sep =" ")
        continue
    elif N == 1:
        sum = 1
        print(0,1,sep =" ")
        continue
    else:
        a.append(1)
        a.append(1)
        for i in range(1,N-2):
            a.append(sum)
            sum += a[i]
    for i in range(1,N -1):
        a.append(sum)
        sum1 += a[i]
    print(sum,sum1)

