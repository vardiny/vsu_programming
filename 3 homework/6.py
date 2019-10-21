def retorn(ch):
    if (not ch % 2 or not ch % 3) and ch > 3:
        return "False"
    else:
        return "True"
a = int(input("Enter your number: "))
print(retorn(a))