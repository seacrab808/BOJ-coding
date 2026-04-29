# 문제는 통과, 효율성 테스트 실패
def solution(phone_book):
    stack = []
    for i in phone_book:
        for j in phone_book:

            if j.startswith(i) and i!=j:
                stack.append(j)
    if stack:
        return False
    else:
        return True

# sort 이용한 ver.
def solution(phone_book):
    phone_book.sort() # 정렬하면 접두사인 놈이 바로 앞에 옴. 붙어 있음
    
    for i in range(len(phone_book) - 1):
        # 바로 다음 요소와 비교
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

# 해시 이용한 ver.
def solution(phone_book):
    # 해시셋에 저장
    hash_set = set(phone_book)
    
    # 각 번호 돌며 잘라보기 
    for number in phone_book:
        temp = ""
        for char in number:
            temp += char
            # 내 자신이 아닌 접두사가 set에 존재하는지 확인
            if temp in hash_set and temp != number:
                return False
            
    return True