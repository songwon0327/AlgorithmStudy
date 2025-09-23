n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
target_cnt = []
card_cnt = {}

for x in card:
    if x not in card_cnt.keys(): #딕셔너리 key에 해당 수의 카드가 없을 경우
        card_cnt[x] = 1 #추가
    else: #있을 경우
        card_cnt[x] = card_cnt.get(x) + 1 #원래 value 값에 + 1

for y in target: # 카드에 있는 수의 개수 파악
    if y in card_cnt.keys(): #딕셔너리 key에 target 수가 있을 경우
        target_cnt.append(card_cnt.get(y)) # 해당 target과 같은 key의 value 추가
    else: #없을 경우
        target_cnt.append(0) #0 추가

print(' '.join(map(str, target_cnt)))
