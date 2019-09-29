a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lst = sorted(lst)
lft = ''.join(lst)
print(lft)