## 패션왕 신혜빈 해시 - 실버 3

# 첫번째 입력 n만큼 반복
# m_1 에 첫번째 루프 headgear: [hat, turban] 이렇게 해야 하나 ? 딕셔너리로..

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 의류 종류 수
    clothes = {}

    for _ in range(n):
        name, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 0
        clothes[kind] += 1
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    print(result - 1)

# 공식 
# headgear, eyewear는 (2+1) + (((2+1)-1)!)
# headgear: 2
# eyewear: 1

# face는 3 + (1! = 0) = 3 
# face: 3
