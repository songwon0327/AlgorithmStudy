import sys
input = sys.stdin.readline
n = int(input())
input_list = []
stack = []
check = []
i = 0
cnt = 0

for _ in range(n):
    input_list.append(int(input())) #n만큼 입력 받음

while i < n: #input_list 인덱스가 n보다 작을 때까지
    if not stack: #스택이 비어있으면
        stack.append(cnt+1) #스택에 추가
        check.append('+') 
        cnt+=1 #스택에 추가할 수 갱신
        continue
    if stack[-1] == input_list[i]: #스택의 top이 target 수와 같을 경우
        stack.pop() # pop으로 스택에서 top의 수 빼냄
        check.append('-')
        i += 1 #다음 target으로 갱신
    elif stack[-1] < input_list[i]: #스택의 top이 target 수보다 작을 경우
        stack.append(cnt+1) #스택에 추가
        check.append('+')
        cnt += 1 #스택에 추가할 수 갱신
    elif stack[-1] > input_list[i]: #스택의 top이 target 수보다 클 경우
        print('NO')
        sys.exit() # 더 이상 수열이 생성될 수 없으므로 NO 출력 후 종료

for x in check:
    print(x)
#print("\n".join(check))
