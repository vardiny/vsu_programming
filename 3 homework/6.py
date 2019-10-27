def retorn(ch):
    d = 2
    while not (ch % d == 0):
        d += 1
    if d == ch:
        return "True"
    else:
        return "False"
a = int(input("Enter your number: "))
print(retorn(a))