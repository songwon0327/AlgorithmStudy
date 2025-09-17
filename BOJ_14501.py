task_list = []
n = int(input())

for _ in range(n):
    task_list.append(list(map(int, input().split())))

def work(i): #재귀 이용
    if i >= n: #i가 n 이상이면, 퇴사 날을 넘어가므로 0 리턴
        return 0
    output = work(i+1) #작업을 하지않고 다음날로 넘길 경우의 수익
    if task_list[i][0] + i <= n: #i+작업 일 수가 n 이하라면 (작업을 끝내도 퇴사 날을 넘지 않을 경우)
        output = max(output, task_list[i][1]+work(task_list[i][0]+i)) #작업을 하지 않고 넘긴 수익과 작업을 했을 때 수익을 비교해서 큰 쪽 선택
    return output

print(work(0))
