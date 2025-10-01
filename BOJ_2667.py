import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
total = 0 #총 단지 수
complexs = [] #개별 단지 개수 저장
offset = ((1,0),(-1,0),(0,1),(0,-1))
maps = []
for _ in range(n):
    maps.append(list(map(int,input().strip())))

visited = list([0 for _ in range(n)] for _ in range(n))

for r in range(n):
    for c in range(n):
        cnt = 0 #개별 집 개수 초기화
        if (maps[r][c] == 1) and (visited[r][c] != 1): #집이 있고 아직 방문 안했을 경우 (초기 위치)
            visited[r][c] = 1 #방문 처리
            q = deque([(r,c)]) #queue에 삽입
            total += 1 
            cnt += 1 #총 단지 수, 개별 집 개수 +1
            while q: #큐에 원소가 다 없어질 때까지
                x,y = q.popleft() #pop
                for tmpx, tmpy in offset: #pop한 좌표의 위치에서 상하좌우 검사
                    nx = x+tmpx
                    ny = y+tmpy
                    if (0 <= nx < n) and (0 <= ny < n) and (maps[nx][ny] == 1) and (visited[nx][ny] != 1): #상하좌우 위치 중 집이 있고 아직 방문 안한 곳이 있을 경우
                        visited[nx][ny] = 1 #방문 처리
                        q.append((nx,ny)) #queue에 추가
                        cnt+=1 #개별 집 개수 +1
            complexs.append(cnt)
print(total)
for z in sorted(complexs):
    print(z)
