import random
w = 10
h = 5
mines = 5

field = [[0 for a in range(h)] for b in range(w)]

for i in range(mines):
    a = random.randint(0, w - 1)
    b = random.randint(0, h - 1)
    field[a][b] = "M"

for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()
