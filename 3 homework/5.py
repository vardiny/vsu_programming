a = input()
lst = []
newlst = []
sum_ = 0
n = 0
while a: 
    lst.append(a)
    a = input()
for i in lst:
    newlst.append(float(i))
    n = n + 1
sum_ = sum(newlst) 
print(sum_ / n)