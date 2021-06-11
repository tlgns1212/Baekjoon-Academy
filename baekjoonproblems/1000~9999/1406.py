import sys
alphas = list(sys.stdin.readline())
N = len(alphas)
M = int(sys.stdin.readline())
pointer = N - 1
for _ in range(M):
    choice = sys.stdin.readline().split()
    print(choice)
    if choice[0] == "L":
        if pointer > 0:
            print("L",pointer)
            pointer -= 1
    elif choice[0] == "D":
        if pointer < len(alphas) - 1:
            print("D",pointer)
            pointer += 1
    elif choice[0] == "B":
        if pointer > 0:
            pointer -= 1
            print("B",pointer)
            alphas.pop(pointer)
            
    else :
        print(pointer)
        alphas.insert(pointer,choice[1])
        pointer += 1
alphas.pop()
print("".join(alphas))

# 뭔가 스택, 큐, 덱을 사용해야 할 듯 싶음.....
# 음.......큐는 안될 것 같고, 덱이나 스택???
# 어차피 덱은 큐랑 같은거니깐 스텍????