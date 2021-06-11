while True:
    really = False
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    a1 = a**2
    b1 = b**2
    c1 = c**2
    if c1 == b1 + a1:
        really = True
    elif b1 == c1 + a1:
        really = True
    elif a1 == b1 + c1:
        really = True
    print("right" if really else "wrong")