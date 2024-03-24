vyska = float(input("zadej vysku v cm: "))
vaha = float(input("zadej vahu v kg: "))

BMI = vaha / (vyska / 100) ** 2

print(f"Tvoje BMI je {BMI}.")

if BMI <= 18.4:
    print("Jsi podvyževený!")
elif BMI <= 24.9:
    print("Jsi normalní, Gratuluji :)!")
elif BMI <= 29.9:
    print("Máš nadváhu!")
elif BMI <= 39.9:
    print("Máš obezitu!")
else:
    print("Jsi morbidně obézní!")
