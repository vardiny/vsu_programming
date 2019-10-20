lst = []
l = str()
lst = input().split()
print(lst)
for x in range(len(lst)):
    if x == 0:
        A = int(lst[x])
    if x == 1:
        l == ' '.join(lst[x])
    if x == 2:
        B = int (lst[x])
print(A,B)
for x in lst:
    if x == "+":
        print(A + B)
    elif x == "*":
        print(A * B)
    elif x == "-":
        print(A - B)
    elif x == "%":
        print(A % B)
    elif x == "**":
        print(A ** B)
    elif x == "//":
        print(A // B)
    elif x == "/":
        print(A / B)
