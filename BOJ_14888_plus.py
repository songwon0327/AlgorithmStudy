n = int(input())
num_list = list(map(int,input().split()))
plus, minus, mul, divi = list(map(int,input().split()))

maxi = -10**12
mini = 10**12

def dfs(idx, total, p, m, mu, d):
    global maxi, mini
    
    if idx == n:
        maxi = max(maxi, total)
        mini = min(mini, total)
        return
    
    if p > 0:
        dfs(idx+1, total+num_list[idx], p-1, m, mu, d)
    if m > 0:
        dfs(idx+1, total-num_list[idx], p, m-1, mu, d)
    if mu > 0:
        dfs(idx+1, total*num_list[idx], p, m, mu-1, d)
    if d > 0:
        dfs(idx+1, int(total/num_list[idx]), p, m, mu, d-1)
        
dfs(1, num_list[0], plus, minus, mul, divi)

print(maxi)
print(mini)