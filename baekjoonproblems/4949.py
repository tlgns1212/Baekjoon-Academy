import sys
a = []
while 1:
    a = sys.stdin.readline()# input 사용하면 356ms
    b = []                  # sys 사용하면 96ms
    end = True              # 이 문제 1000ms가 한도
    if a == (".\n"):
        break
    for a1 in a:
        if a1 in ("])"):
            if b == []:
                end = False
                break
            elif a1 == "]":
                if b.pop() == "(":
                    end = False
                    break
            elif a1 == ")":
                if b.pop() == "[":
                    end = False
                    break
        elif a1 in ("[("):
            b.append(a1)
    if b != []:
        end = False
    print("yes" if end else "no")
        
