from ast import Break
import random

w, h, mines = 10, 5, 51


field = [[0 for y in range(h)] for x in range(w)]

for i in range(mines):
    rx = random.randint(0, w - 1)
    ry = random.randint(0, h - 1)
    field[rx][ry] = "M"
    if field[rx][ry] == "M":
        field[rx][ry] = field[rx+1][ry]
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()
