m = int(input())
point = 1

for _ in range(m):
    a, b = map(int,input().split())
    
    if point == a:
        point = b
    elif point == b:
        point = a

print(point)   