n = int(input())
stack = []
upsideStack = [0]
answer = []
for _ in range(n):
    stack.append(int(input()))
j = 0
for i in range(n):
    if i < n :
        upsideStack.append(i+1)
        answer.append("+")
        j += 1
    while stack[0] == upsideStack[j]:
        stack.pop(0)
        upsideStack.pop()
        answer.append("-")
        j -= 1
        if stack == []:
            break
    if i == n - 1 and stack != []:
        answer.clear()
        break
if answer == []:
    print("NO")
else :
    for i in answer:
        print(i)