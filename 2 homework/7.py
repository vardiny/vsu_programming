import random
a = int (8)
m = 0 #random.randint(0,100)
while a != m:
    a = int (input("Enter the number: "))
    if a == m:
        print("Right!!!")
    elif a > m:
        print("Less!!!")
    else:
        print("More!!!")