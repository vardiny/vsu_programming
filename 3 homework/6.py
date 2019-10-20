def retorn(ch):
    if (ch % 2 == 0 or ch % 3 == 0) and ch > 3:
        return "False"
    else:
        return "True"
a = int(input("Enter your number: "))
print(retorn(a))