size = int(input("zadej velikost: "))

for a in range(int(size / 2), size + 1, 2):
    for b in range(1, size - a, 2):
        print(" ", end = "")
    
    for b in range(1, a + 1):
        print("A", end = "")  

    for b in range(1, (size - a) + 1):
        print(" ", end = "")
            
    for b in range(1, a):
        print("A", end = "")

    print("")

for a in range(size, -1, -1):
    for b in range(a, size):
        print(" ", end = "")
            
    for b in range(1, (a * 2)):
        print("B", end = "")

    print("")