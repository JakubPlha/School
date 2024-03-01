fruit = ["Apple", "Grapes", "Orange", "Cherry", "Kiwi"]
prices = [120, 100, 52, 98, 65]

result = zip(fruit, prices)

for info in result:
    print(info, end = " ")