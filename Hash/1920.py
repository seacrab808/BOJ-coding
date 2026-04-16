## 수 찾기 해시 - 실버 5

N = int(input())
n_set = set(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))


for i in m_list:
    if i in n_set:
        print(1)
    else:
        print(0)

# set을 쓴 이유: 이 숫자가 있는지 단순 여부 확인용이라 순서 상관 없음 - 엄청 빠름
# list를 쓴 이유: 순서대로 출력되어야 해서 set보다 100배 느린 list 사용

# dict도 초고속이지만 key-value 매핑할 때 사용
# 이 문제에서 key-value는 필요 없음
