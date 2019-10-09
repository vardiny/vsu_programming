text = input()
lsttext = text.split()
max_ = 0
for i in range(len(lsttext)):
    if len(lsttext[max_]) < len(lsttext[i]):
        max_ = i
print(lsttext[max_])
f = 0
for i in lsttext:
        n = lsttext.count(i)
        if f < n:
            f = n
            max_ = i
print(max_)