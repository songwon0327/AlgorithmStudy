n, m = map(int, input().split()) #n= 행 m= 열
square = [] 
ck = min(n,m) 
flag = False

for _ in range(n):
    square.append(list(map(int,input().strip()))) #입력한 행의 수 만큼 입력을 받아 2차원 리스트로 만듦 
    
#k=만들 정사각형의 한 변 길이 (최대로 만들 수 있는 정사각형은 n,m 중 작은 쪽의 길이 만큼이므로 ck이용)
#넓이가 가장 큰 정사각형을 찾아야하므로 역으로 반복
for k in range(ck-1,-1,-1): 
    for i in range(n):
        if i+k >= n: #i+k가 인덱스 넘어감 방지
            break
        for j in range(m):
            if (j+k >= m): #j+k가 인덱스 넘어감 방지
                break            
            if square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]: #네 위치의 숫자가 같을 경우 (정사각형이 만들어질 경우)
                print((k+1)**2) #정사각형 넓이 출력
                flag = True
                break
        if flag:
            break
    if flag:
        break    
