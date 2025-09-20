from itertools import permutations

n = int(input())
num_list = list(map(int,input().split()))
operation_cnt = list(map(int,input().split()))
operations = []
maxi = -1000000001
mini = 1000000001

operations = ['+'] * operation_cnt[0] + ['-'] * operation_cnt[1] + ['*'] * operation_cnt[2] + ['/'] * operation_cnt[3] #연산자 4개 개수대로 변환

def calc(x): #각 연산자들 match문에 매칭시켜서 연산 수행 후 누적
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

for op in permutations(operations, n-1): #연산자 리스트로 가능한 모든 순열 만들기
    op = list(op)
    cur = calc(op)
    maxi = max(maxi,cur) #가장 큰 값
    mini = min(mini,cur) #가장 작은 값

print(maxi)
print(mini)
