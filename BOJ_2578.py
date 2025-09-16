bingo = [] #빙고판
present = [] #부르는 순서
check = [[0 for _ in range(5)] for _ in range(5)]
cnt = 0 #빙고 횟수 카운트
flag = False

for _ in range(5):
    bingo.append(list(map(int,input().split())))

for _ in range(5):
    present.append(list(map(int,input().split())))
    
for i in range(5):
    for j in range(5):
        cnt = 0
        find = present[i][j] #현재 부른 숫자
        for k in range(5):
            if find in bingo[k]: #빙고판의 k행에 부른 숫자가 있다면
                a = bingo[k].index(find)
                check[k][a] = 1 #check에서 1로 바꿔 표시
                break
        rcheck = list(zip(*check)) #$ 행과 열을 바꿔줌
        for l in range(5):
            if sum(check[l]) == 5: #행 l이 빙고이면
                cnt+=1
            if sum(rcheck[l]) == 5: #열 l이 빙고이면
                cnt+=1
        cond1 = sum([check[0][0], check[1][1], check[2][2], check[3][3], check[4][4]]) == 5 #대각선 확인
        cond2 = sum([check[0][4], check[1][3], check[2][2], check[3][1], check[4][0]]) == 5 #대각선 확인
        cnt += sum([cond1, cond2])
        
        if cnt >= 3: #* 빙고가 3개면 (한 번에 4개 이상의 빙고가 생길 수도 있음)
            print(((i*5)+j)+1)
            flag = True
            break

    if flag:
        break
