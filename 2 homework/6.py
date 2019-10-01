a = str (input("Enter the text: "))
k = int (input("Enter what is number in order: "))
m = int (0)
s = int (0)
l = len(a)
for m in  range(0,l):
    if a[m].isdigit():
        s = s + 1
    if s == k:
        print(a[m])