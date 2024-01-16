
player = [2564, 5]
enemy = [3, 4]
hp = 100
a = player[0] - enemy[0]
b = player[1] - enemy[1]
c = (a**2 + b**2) ** 0.5
if c < 2:
    hp -= 15



print(hp)
