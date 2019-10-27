lst = input().split()
dct = dict.fromkeys(lst,0)
for x in lst:
    n = lst.count(x)
    dct[x] = n
print(dct)