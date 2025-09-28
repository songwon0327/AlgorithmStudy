import sys
input = sys.stdin.readline
n, m, v = map(int,input().split())
graph = list([0 for _ in range(n)] for _ in range(n))
visited_dfs = [0 for _ in range(n)] #방문 체크
visited_bfs = [0 for _ in range(n)] #방문 체크
check_dfs = []
check_bfs = []

for _ in range(m): #간선으로 이어진 정점의 인덱스 1로 변경
    a, b = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1

def dfs(i): #재귀 이용
    if not check_dfs:
        visited_dfs[i] = 1 #경로 리스트가 비어있으면 채워줌
        check_dfs.append(i+1)
    for j in range(n):
        if i == j:
            continue
        if (graph[i][j] == 1) and (visited_dfs[j] != 1): #간선이고 방문을 하지 않은 곳이라면
            visited_dfs[j] = 1
            check_dfs.append(j+1)
            dfs(j) #방문처리 + 경로 체크 + 다음 경로 찾기
            
def bfs(i):
    q = [i] #queue역할 리스트
    visited_bfs[i] = 1 #방문 처리
    head = 0 #현재 위치 표시
    while head < len(q):
        c = q[head]
        head += 1
        check_bfs.append(c+1)
        for j in range(n):
            if (graph[c][j] == 1) and (visited_bfs[j] != 1):  #간선이고 방문을 하지 않은 곳이라면
                visited_bfs[j] = 1
                q.append(j) #queue에 추가
dfs(v-1)
bfs(v-1)
print(*check_dfs)
print(*check_bfs)
