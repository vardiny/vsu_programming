a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lst = sorted(lst, reverse=True)
lft = ''.join(lst)
print(lft)