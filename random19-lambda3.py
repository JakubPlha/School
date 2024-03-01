fruit = ["Apple", "Grapes", "Orange", "Cherry", "Kiwi"]

result = filter(lambda x: len(x)<5, fruit)

for data in result:
    print(data, end = " ")