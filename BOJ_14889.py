n = int(input())
ability = []
visit = [0]*(n+1) #방문 표시
result = []

for _ in range(n):
    ability.append(list(map(int,input().split())))

def team_cal(start): #능력치 계산 함수
    global ability
    start_ab = link_ab = 0 #start 능력치, link 능력치
    global result
    link = list(k for k in range(1, n+1) if k not in start) #링크 팀 선수는 스타트 팀 선수가 아닌 수
    
    for i in start:
        for j in start:
            if i != j: #같은 선수일 경우의 비교 피함
                start_ab += ability[i-1][j-1]
    for i in link:
        for j in link:
            if i != j: #같은 선수일 경우의 비교 피함
                link_ab += ability[i-1][j-1]
    
    result.append(abs(start_ab - link_ab)) #두 팀의 능력치 차 절댓값으로 표현하여 리스트에 추가
    return 

def dfs(i, length):
    if length == n//2 : #length가 n//2가 되면
        start = list(k for k in range(1, n+1) if visit[k] == 1) # 스타트 팀 선수 목록을 방문한 수 리스트로 표현
        team_cal(start) #능력치 함수 호출
        return
             
    for j in range(i, n+1): #중복 방지 위하여 i부터
        if visit[j] != 1: #해당 수에 방문한 적 없으면
            visit[j] = 1 #방문 처리
            dfs(j+1,length+1) #lenght 증가, 다음 수 탐색
            visit[j] = 0 #백트래킹

dfs(1,0) #dfs 호출
print(min(result)) #모든 능력치 차이 값 중 가장 작은 값 출력
