a = input("Enter any text: ")
lst = []
while a:
    lst.append(a)
    a = input()
while lst:
    for x in lst:
        n = lst.count(x)
        print(x,n)
        for l in range(n):
            lst.remove(x)
