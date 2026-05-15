# 겹치지 않는 사각형의 넓이

x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
grid = [[0] * 2001 for _ in range(2001)]
OFFSET = 1000

for x in range(x1[0] + OFFSET, x2[0] + OFFSET):
    for y in range(y1[0] + OFFSET, y2[0] + OFFSET):
        grid[x][y] += 1

for x in range(x1[1] + OFFSET, x2[1] + OFFSET):
    for y in range(y1[1] + OFFSET, y2[1] + OFFSET):
        grid[x][y] += 1

for x in range(x1[2] + OFFSET, x2[2] + OFFSET):
    for y in range(y1[2] + OFFSET, y2[2] + OFFSET):
        grid[x][y] = 0


cnt = 0

for i in grid:
    for j in i:
        if j != 0:
            cnt += 1

print(cnt)

# 색종이의 총 넓이 
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
grid = [[0] * 201 for _ in range(201)]

for i in range(n):
    cur_x = x[i] + 100
    cur_y = y[i] + 100

    for c_x in range(cur_x, cur_x + 8):
        for c_y in range(cur_y, cur_y + 8):
            grid[c_x][c_y] = 1 

cnt = 0
for g in grid:
    for val in g:
        if val > 0:
            cnt += 1

print(cnt)

# 잔해물을 덮기 위한 사각형의 최소 넓이