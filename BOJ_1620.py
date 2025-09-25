n, m = map(int, input().split())
#시간복잡도 개선을 위해 양방향 딕셔너리 사용
ind_to_name = {} #포켓몬 이름이 key
name_to_ind = {} #포켓몬 번호가 key

for i in range(1,n+1): #포켓몬 이름과 번호를 각각의 딕셔너리에 추가
    name = input()
    ind_to_name[i] = name
    name_to_ind[name] = i

for _ in range(m):
    target = input()
    if target.isalpha(): #입력이 알파벳(포켓몬 이름)일 경우
        print(name_to_ind.get(target)) #포켓몬 이름이 key인 딕셔너리에서 값 찾기
    else:
        target = int(target) #입력이 숫자(포켓몬 번호)일 경우
        print(ind_to_name.get(target)) #포켓몬 번호가 key인 딕셔너리에서 값 찾기
