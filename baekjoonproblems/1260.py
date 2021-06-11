import sys
import queue
import copy
def DFS(link,found,v):
    if v not in found:
        print(v,end = " ")
        found.append(v)
    for i in link:
        if v == i[0]:
            link.pop(link.index(i))
            DFS(link,found,i[1])
        elif v == i[1]:
            link.pop(link.index(i))
            DFS(link,found,i[0])
def BFS(link,found,v):
    queueList = queue.Queue()
    queueList.put(v)
    print(max(link))
    for i in link:
        while queueList:
            if v == i[0]:
                queueList.put(i[1])
                link.pop(link.index(i))
                if i[1] not in found:
                    found.append(i[1])
                    print(i[1],end = " ")
            elif v == i[1]:
                queueList.put(i[0])
                link.pop(link.index(i))
                if i[0] not in found:
                    found.append(i[0])
                    print(i[0],end = " ")
N,M,V = map(int,sys.stdin.readline().split())
linkList = [] 
#linkList2 = []
found = []
for _ in range(M):
    linkList.append(list(map(int,sys.stdin.readline().split())))
linkList.sort()
DFS(linkList,found,V)
#linkList2 = copy.deepcopy(linkList)
#found2 = []
print("\n",linkList,found,V)
#print(linkList2,found2,V)
#BFS(linkList2,found2,V)