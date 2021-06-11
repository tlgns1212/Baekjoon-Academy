import sys
import heapq
V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
heap = list()
ga = [float('inf')]*(V+1)
graph = [[] for _ in range(V + 1)]

def find_distance(K):
    ga[K] = 0
    heapq.heappush(heap,(0,K))
    while heap:
        ga1, me = heapq.heappop(heap)
        for g, next in graph[me]:
            next_g = g + ga1
            if next_g < ga[next]:
                ga[next] = next_g
                heapq.heappush(heap,(next_g,next))

for _ in range(E):
    u, v, w = list(map(int,sys.stdin.readline().split()))
    graph[u].append((w,v))
find_distance(K)
for i in range(1,V+1):
    print("INF" if ga[i] == float('inf') else ga[i])





