cisla = [float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())]
print(cisla)

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

for j in range(len(cisla) - 1):
    for i in range(len(cisla) - 1):
        if cisla[i] > cisla[i + 1]:
            cisla[i], cisla[i + 1] = cisla[i + 1], cisla[i]
    print(cisla)
