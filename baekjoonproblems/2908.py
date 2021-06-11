a,b = map(int,input().split())
a1 = 0
b1 = 0
while 1:
    a1 += a%10
    a //= 10
    a1 *=10
    if a == 0:
        a1 /= 10
        break
while 1:
    b1 += b%10
    b //= 10
    b1 *=10
    if b == 0:
        b1 /= 10
        break
if a1 > b1:
    print(int(a1))
else:
    print(int(b1))