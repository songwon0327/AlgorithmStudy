import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
MAX = 100000

dist = list(-1 for _ in range(MAX+1)) #초 체크
q = deque([n])
dist[n] = 0 #시작위치를 0초

while q:
    x = q.popleft()
    if x == k: #pop한 수가 종료 지점과 같으면
        print(dist[x]) #초 출력 후 break
        break
    for nx in (x*2, x+1, x-1): 
        if (0 <= nx <= MAX) and (dist[nx] == -1): #다음 수가 범위 내고 방문하지 않은 수이면
            dist[nx] = dist[x] + 1 #1초 증가
            q.append(nx) #큐에 추가
 