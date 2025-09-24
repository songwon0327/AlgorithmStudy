n = int(input())

for _ in range(n):
    cnt = 0 
    vfs = input()
    for i in range(len(vfs)):
        if vfs[i:i+1] == '(': 
            cnt += 1
        elif (vfs[i:i+1] == ')'):
            cnt -= 1
        if cnt < 0: #(보다 )가 먼저오면 무조건 vfs가 아니므로
            break
    if cnt == 0:
        print('YES')
    elif cnt != 0:
        print('NO')
