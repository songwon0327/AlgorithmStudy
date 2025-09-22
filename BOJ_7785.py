n = int(input())
record = {}
worker = []
for _ in range(n):
    name, state = input().split()
    record[name] = state #이름과 근무 상태 딕셔너리에 저장 (여러번 나오면 덮어씀)

for name, state in record.items(): 
    if state == 'enter': #근무 상태가 enter면 근무 중으로 판단
        worker.append(name)

sorted_worker = sorted(worker, reverse = True) #내림차순 정렬

for x in sorted_worker:
    print(x)
