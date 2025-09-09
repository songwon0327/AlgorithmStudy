triangle_num = list((n*(n+1))//2 for n in range(1,46)) #T_46까지의 삼각수 list에 저장
input_list = [] #입력값 저장 list

trying = int(input())

for _ in range(trying):
    tmp = int(input())
    input_list.append(tmp)

for i in triangle_num:
    for j in triangle_num:
        for k in triangle_num:
            tri_sum = i+j+k # 삼중 루프 돌면서 3개의 삼각합일 경우 구현
            if tri_sum in input_list: # i+j+k가 입력값 중 동일한 값이 있다면
                input_list[input_list.index(tri_sum)] = 1 #해당 입력값을 1로 변경
                
result = list(0 if x!=1 else x for x in input_list) #1로 변경된 값 제외 나머지 값을 0으로 변경       

for l in result:
    print(l)
    