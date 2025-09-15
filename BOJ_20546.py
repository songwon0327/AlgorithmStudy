money = int(input()) #현금
stock_price = list(map(int, input().split())) #14일 간의 주가

def BNP(x):
    stock = 0 #매수한 주식 수
    
    for st in stock_price:
        if st <= x: #그날 주가가 소지한 현금보다 낮으면
            stock += x // st #매수한 주식
            x = x % st #남은 현금
    result = x + stock_price[-1] * stock #마지막 날 자산
          
    return result

def TIMING(x):
    stock = 0 #매수한 주식 수
    up = 0 #연속 상승일
    down = 0 #연속 하락일
    
    for i in range(len(stock_price)):
        if i != 0: #$ 전 주가와 현 주가 비교를 위해
            if stock_price[i-1] < stock_price[i]: #전 주가가 현 주가보다 낮을 경우
                up += 1
                down = 0
            elif stock_price[i-1] > stock_price[i]: #전 주가가 현 주가보다 높을 경우
                down += 1
                up = 0
            else : #* 전 주가와 현 주가가 같을 경우 상승, 하락 끊어줘야함
                up = down = 0    
                
        if (down >= 3): #하락일이 3일 연속
            if stock_price[i] <= x: #그날 주가가 소지한 현금보다 낮으면
                stock += x // stock_price[i] #매수한 주식
                x = x % stock_price[i] #남은 현금       
        elif (up >= 3) and stock != 0: #상승일 3일 연속 and 가지고 있는 주식이 0이 아닌 경우
            x += stock*stock_price[i] #전 수량 매도
            stock = 0  
                  
    result = x + stock_price[-1] * stock #마지막날 자산
    #* 중간에 매도했다가 다시 매수할 경우 생각해야함.....
    
    return result       
            

b = BNP(money)
t = TIMING(money)

if b > t:
   print("BNP")
elif b < t:
    print("TIMING")
else:
    print("SAMESAME")
