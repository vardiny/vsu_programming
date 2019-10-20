def fibona44i(n):
    s = 0
    d = 1
    lst = [0]
    for x in range(n-1):
        if s > d:
            d = d + s
            lst.append(s)
        else:
            s = s + d
            lst.append(d)
    return(lst)
n = int(input("Enter the amount of number of Fibonachchi: "))
print(fibona44i(n))
