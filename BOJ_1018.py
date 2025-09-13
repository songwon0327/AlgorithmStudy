n, m = map(int,input().split()) # 행, 열 입력
chess = []
check = []

for _ in range(n):
    chess.append(list(input().strip()))

for i in range(n):
    if i+8 > n: #인덱스 범위 제한
        break
    for j in range(m): #입력받은 chess list 탐색
        if j+8 > m: #인덱스 범위 제한
            break
        tmp = list(row[j:j+8] for row in chess[i:i+8]) #8*8인 2차원 리스트로 잘라서 tmp
        cnt = 0   #각 8*8 체스판에서 색 다시 칠하는 횟수 저장
        if tmp[0][0] == 'W': #시작 색이 W이면
            for k in range(8):
                for l in range(8):
                    if (((k+l) % 2 == 0) and (tmp[k][l] != 'W')) or (((k+l) % 2 == 1) and (tmp[k][l] != 'B')):
                        #짝 수번째 칸인데 B이거나 홀 수번째 칸인데 W일 경우
                        cnt+=1 #다시 칠함
        elif tmp[0][0] == 'B': #시작 색이 B이면
            for k in range(8):
                for l in range(8):
                    if (((k+l) % 2 == 0) and (tmp[k][l] != 'B')) or (((k+l) % 2 == 1) and (tmp[k][l] != 'W')):
                        #짝 수번째 칸인데 W이거나 홀 수번째 칸인데 B일 경우
                        cnt+=1  #다시 칠함
        cnt = min(cnt, 64-cnt) #시작 색을 다시 칠하면 진행하는 경우도 있으므로 두 경우 중 더 적게 칠하는 경우를 고름               
        check.append(cnt) #각 횟수 추가
            
print(min(check)) #가장 적게 칠하는 경우 출력

