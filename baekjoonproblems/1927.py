import sys
import heapq
N = int(sys.stdin.readline())
heap = list()
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if heap == []:
            print(0)
        else :
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)