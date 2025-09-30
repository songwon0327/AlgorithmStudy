import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split()) #x좌표, y좌표 반대 주의
    visited = [[0 for _ in range(m)] for _ in range(n)]
    field = [[0 for _ in range(m)] for _ in range(n)]
    offset = ((0,1),(0,-1),(1,0),(-1,0))
    cnt = 0
    
    for _ in range(k):
        b, a = map(int,input().split())
        field[a][b] = 1
        
    for i in range(n): #BFS 진행
        for j in range(m):
            if (field[i][j] == 1) and visited[i][j] != 1: #배추가 있고 방문하지 않은 곳이라면
                q = deque([(i,j)]) #큐에 추가
                visited[i][j] = 1 #방문 처리
                cnt += 1 #필요한 지렁이 +1
                while q: #큐에 원소가 없어지기 전까지
                    x, y = q.popleft() #pop
                    for ix, iy in offset: #pop한 위치에서 상하좌우 탐색
                        x_tmp = x+ix
                        y_tmp = y+iy
                        if (0 <= x_tmp < n) and (0 <= y_tmp < m) and (field[x_tmp][y_tmp] == 1) and visited[x_tmp][y_tmp] != 1: 
                            #상하좌우 중 field의 범위 안이고 배추가 있고 방문하지 않았다면
                            q.append((x_tmp, y_tmp)) #큐에 추가
                            visited[x_tmp][y_tmp] = 1 #방문 표시
    print(cnt)
