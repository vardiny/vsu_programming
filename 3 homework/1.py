A = float (input("Enter the first number: "))
B = float(input("Enter the second number: "))
x = str(input("Enter the math sign (+,-,/,*,//,%,**):"))
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
