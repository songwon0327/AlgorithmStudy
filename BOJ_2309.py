height = [] #난쟁이 9명의 키를 담을 list
flag = False

for tmp in range(9):
    tmp = int(input())
    height.append(tmp) #list에 총 9개의 입력 값 append

height_total = sum(height) #난쟁이 9명의 키 총 합

for i in range(9): #9명 키 총 합에서 난쟁이 둘을 뽑아 제외하며 100이되는 경우를 찾는다. 
    for j in range(i+1,9): 
        result = height_total - (height[i] + height[j])
        if result == 100:
            a, b = height[i], height[j]
            flag = True #반복문 탈출을 위한 flag
            break
    if flag:
        break   
    
height.remove(a) #height list에서 result가 100이 되는 경우의 height[i], height[j] 삭제
height.remove(b)

for k in sorted(height):
    print(k)      