import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
MAX = 100000

dist = list(-1 for _ in range(MAX+1))
ways = list(0 for _ in range(MAX+1))
q = deque([n])
dist[n] = 0
ways[n] = 1 # 몇 번 방문했는 지 표시
flag = False

while q and not flag:
    for _ in range(len(q)):
        x = q.popleft()
        if x == k:
            flag = True
        for nx in (x*2, x+1, x-1):
            if (0 <= nx <= MAX) and (dist[nx] == -1): #처음 방문하는 수 일 경우
                dist[nx] = dist[x] + 1 #경과 시간 표시 (초)
                ways[nx] = ways[x] # 처음 방문이므로 ways는 1
                q.append(nx)
            elif (0 <= nx <= MAX) and (dist[nx] == dist[x] + 1): #처음 방문했을 때와 같은 시간에 재방문 (최단 경로)
                ways[nx] += ways[x] #ways만 1증가하여 방문 횟수만 증가

print(dist[k])
print(ways[k])
