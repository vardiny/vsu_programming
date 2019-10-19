def combsort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:    ## variant "comb-11"
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return alist
a = input("Enter any numbers: ")
lst = []
while a:
    lst.append(a)
    a = input()
print(combsort(lst))