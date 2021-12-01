# a,b = map(int,input().split())
# print(a+b)

# 다른 사람들이 한 거 보면 아래가 시간 64ms로 시간 최소화인데, 내가 해본 결과 위에께 68ms고 아래가 72ms로 내장함수 안쓰는게 더 좋음
print(sum(map(int, input().split())))
