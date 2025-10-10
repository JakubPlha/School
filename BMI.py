#načtu si data
vyska = float(input("Zadejte výšku v cm: "))
vaha = float(input("Zadejte váhu v kg: "))

#předělám výšku na metry
vyska_m = vyska / 100

#výpočet BMI
bmi = vaha / vyska_m ** 2

#výpis BMI čísla
print(f"Vaše BMI je: {bmi:.2f}")

#výpis informace o váze
if bmi < 18.5:
    print("Podváha")
elif bmi < 24.9:
    print("Normální váha")
elif bmi < 29.9:
    print("Nadváha")
else:
    print("Obezita")