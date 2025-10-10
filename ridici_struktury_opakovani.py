#zadá se číslo
n = int(input("Zadej číslo větší než 0: "))

#všechno co chci vědet si nastavim na nula
sudych = 0
lichych = 0
prvocisel = 0

for i in range(1, n + 1):
    #zkouším jestli to je Sudé nebo liché
    if i % 2 == 0:
        sudych += 1
        typ = "sudé"
    else:
        lichych += 1
        typ = "liché"

    #jesli je Dělitelný 3
    if i % 3 == 0:
        del3 = "ano" 
    
    else:
        del3 = "ne"

    #jesli jePrvočíslo
    prvo = True
    if i < 2:
        prvo = False
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prvo = False
                break

    #vypisuju ty čisla
    if prvo == True:
        prvocisel += 1
        print(f"{i} - {typ}, dělitelné 3: {del3}, prvočíslo: ano")
    else:
        print(f"{i} - {typ}, dělitelné 3: {del3}, prvočíslo: ne")

#vypisuju souhrn
print("Sudých:", sudych)
print("Lichých:", lichych)
print("Prvočísel:", prvocisel)