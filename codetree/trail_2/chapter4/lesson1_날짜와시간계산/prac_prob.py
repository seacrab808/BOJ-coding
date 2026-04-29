## DateTime to DateTime

# 첫 시도
a, b, c = map(int, input().split())

# Please write your code here.

day, hour, min = 11, 11, 11
total_min = 0


while True:
    if day == a and hour == b and min == c:
        break

    if day > a:
        print(-1)
        break

    else:
        min += 1
        total_min += 1

        if min == 60:
            hour += 1
            min = 0
        
        elif hour == 24:
            day += 1
            hour = 0

if not day > a:
    print(total_min)



# 정답
a, b, c = tuple(map(int, input().split()))

diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

if diff < 0:
    print(-1)
else:
    print(diff)



## 요일 맞추기
# 30분 걸림 ㅜ

m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]

month, day = m1, d1

def get_total_days(m, d, month_days):
    return sum(month_days[1:m]) + d

day_1 = get_total_days(m1, d1, month_days)
day_2 = get_total_days(m2, d2, month_days)

diff = day_1 - day_2
 
if diff > 0:
    # 양수일 때
    print(days[diff % 7])
else:
    # 음수일 때
    print(days[diff % 7])