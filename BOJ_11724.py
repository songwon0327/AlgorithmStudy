import sys
sys.setrecursionlimit(2000)  #재귀 한도 상향 (RecursionError 방지)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list([] for _ in range(n+1)) #인접 리스트 준비
visited = list(0 for _ in range(n+1))
cnt = 0

for _ in range(m): #인접 리스트로 간선 좌표 담기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i): #dfs 진행
    visited[i] = 1
    for j in graph[i]:
        if visited[j] != 1:
            dfs(j)
    
for x in range(1,n+1):
    if (visited[x] != 1): #고립노드 포함해야함
        dfs(x)
        cnt+=1 #방문 처리 안된 노드만 dfs 진행한 후 연결 요소 개수 +1
              
print(cnt)
