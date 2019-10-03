a = str (input("Enter the text: "))
k = int (input("Enter what is number in order: "))
s = 0
for m in  a:
    if m.isdigit():
        s = s + 1
    if s == k:
        print(m)
        break