height = [] #난쟁이 9명의 키를 담을 list
found = False

for tmp in range(9):
    tmp = int(input())
    height.append(tmp) #list에 총 9개의 입력 값 append

height_total = sum(height) #난쟁이 9명의 키 총 합

for i in height:
    for j in height[height.index(i)+1:]:
        result = height_total - (i+j)
        if result == 100:
            found = True
            break
    if found:
        break   
    
height.remove(i)
height.remove(j)

for k in sorted(height):
    print(k)