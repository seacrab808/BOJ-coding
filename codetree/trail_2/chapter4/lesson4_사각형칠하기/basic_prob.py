# 사각형의 총 넓이 
n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grid = [[0] * 201 for _ in range(201)]

for i in range(n):
    cur_x1, cur_y1 = x1[i] + 100, y1[i] + 100
    cur_x2, cur_y2 = x2[i] + 100, y2[i] + 100

    for x in range(cur_x1, cur_x2):
        for y in range(cur_y1, cur_y2):
            grid[x][y] = 1

cnt = 0
for b in grid:
    for k in b:
        if k == 1:
            cnt += 1

print(cnt)