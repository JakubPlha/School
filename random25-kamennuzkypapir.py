import random

game_list = ["Kámen", "Nůžky", "Papír"]
computer = c = 0
command = p = 0

print("Skóre: Počítač" + str(c) + " Hráč " + str(p))

run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Kámen, Nůžky, Papír nebo Opustit: ")
    if command == computer_choice:
        print("Remíza")

    elif command == "Kámen":
        if computer_choice == "Nůžky":
            print("Hráč Vyhrál!")
            p += 1

        else:
            print("Počítač Vyhrál!")
            c += 1

    elif command == "Papír":
        if computer_choice == "Kámen":
            print("Hráč Vyhrál!")
            p += 1 

        else:
            print("Počítač Vyhrál!")
            c += 1

    elif command == "Nůžky":
        if computer_choice == "Papír":
            print("Hráč Vyhrál")
            p += 1

        else:
            print("Počítač Vyhrál!")
            c += 1

    elif command == "Opustit":
        break

    else:
        print("Špatný command! ")

    print("Hráč: " + command)
    print("Počítač: " + computer_choice)
    print("")
    print("Skóre: Počítač " + str(c) + " Hráč " + str(p))
    print("")