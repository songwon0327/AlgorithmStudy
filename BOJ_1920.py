n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))

'''for b in list_b:
    if b in list_a:
        print(1)
    else:
        print(0)'''
# 시간 초과

'''def binary(target):
    left = 0
    right = n-1
    
    while left <= right:
        mid = (left+right) // 2
        
        if list_a[mid] == target:
            return 1
        elif list_a[mid] < target:
            left = mid+1
        elif list_a[mid] > target:
            right = mid-1
    return 0

for x in list_b:
    print(binary(x))'''
# 이진 탐색

for b in list_b:
    if b in set_a:
        print(1)
    else:
        print(0)
#set 이용 (내부적으로 해시 테이블 이용)
