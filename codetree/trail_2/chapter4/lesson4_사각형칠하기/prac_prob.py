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