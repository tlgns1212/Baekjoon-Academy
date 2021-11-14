N,K = map(int,input().split())
n = []
count = 0
sum = 0
for i in range(N):
    n.append(int(input()))
max = len(n) - 1
while not K == sum:
    if n[max] <= (K - sum):
        a = (K - sum) // n[max]
        sum += (a * n[max])
        count += a
    if n[max] > (K - sum):
        max -= 1
print(count)