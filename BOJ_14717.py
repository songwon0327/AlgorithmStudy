card = list(x for x in range(1,11) for _ in range(2)) #[1,1,2,2,3,3,4,4 ... 10,10]

cnt = 0 #영학이 이기는 횟수 저장

a, b = map(int,input().split(" "))

card.remove(a)
card.remove(b) #영학이 고른 카드 두 장 제외

if a == b: #영학이 고른 카드가 땡일 때
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            if (card[i] < a) or (card[i] != card[j]): #영학이 고른 카드의 숫자보다 작거나 두 카드가 같지 않으면(끗) 영학의 승리
                cnt += 1
else: #영학이 고른 카드가 끗일 때 (a != b)
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            if card[i] == card[j]: #두 카드가 같으면 (땡이면) 영학이 무조건 패배
                continue
            if ((card[i]+card[j]) % 10) < ((a+b) % 10): #영학의 카드보다 일의 자리 수가 작으면 영학의 승리
                cnt += 1
                
total = (len(card)*(len(card)-1)) / 2 #영학이 카드 뽑은 후 두 카드가 뽑힐 총 경우의 수
result = cnt/total #영학이 승리할 확률
print(f"{result:.3f}")                
                                