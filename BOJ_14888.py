from itertools import permutations

n = int(input())
num_list = list(map(int,input().split()))
operation_cnt = list(map(int,input().split()))
operations = []
maxi = -1000000001
mini = 1000000001

operations = ['+'] * operation_cnt[0] + ['-'] * operation_cnt[1] + ['*'] * operation_cnt[2] + ['/'] * operation_cnt[3]

def calc(x):
    total = num_list[0]
    for i in range(n-1):
        match x[i]:
            case '+':
                total = total+num_list[i+1]
            case '-':
                total = total-num_list[i+1]
            case '*':
                total = total*num_list[i+1]
            case '/':
                total = int(total/num_list[i+1])
    return total

for op in permutations(operations, n-1):
    op = list(op)
    cur = calc(op)
    maxi = max(maxi,cur)
    mini = min(mini,cur)

print(maxi)
print(mini)
