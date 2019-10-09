def retorn(ch):
    if ch%2 != 0 or ch%3 != 0 or ch == 2 or ch == 3:
        return ("True")
    else:
        return ("False")
a = int(input("Enter your number: "))
print(retorn(a))