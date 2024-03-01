import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><["

all_chars = lower + upper + numbers + symbols
for_what = str(input("k cemu heslo: "))
lenght = int(input("napis jak dlouhy to ma byt: "))

password = "".join(random.sample(all_chars, lenght))
print("heslo k " + for_what + ":", password)