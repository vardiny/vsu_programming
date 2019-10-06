a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lst = sorted(lst, reverse=True)
print(''.join(lst))