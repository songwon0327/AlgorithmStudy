dec = int(input()) #분해합 입력

if dec == 1:
    print(0) #분해합이 1인 경우, 생성자 없으므로 0출력
else:    
    for gen in range(1, dec): #생성자는 항상 분해합보다 작으므로 (dec-1)까지만 반복
        N = sum(list(int(i) for i in str(gen))) #gen의 각 자릿수 list에 담아 sum
        result = gen + N 

        if result == dec: #생성자 찾으면 출력하고 break (가장 작은 생성자만 찾으면 되므로)
            print(gen)
            break
    if gen == (dec-1): #생성자가 없으면 0출력 (반복문이 끝까지 돌아간 경우)
        print(0)  
