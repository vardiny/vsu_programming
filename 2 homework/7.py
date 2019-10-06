import random
a = int(-1)
m = random.randint(0,100)
while a != m:
    a = int(input("Enter the number: "))
    if a == m:
        print("Right!!!")
    elif a > m:
        print("Less!!!")
    else:
        print("More!!!")