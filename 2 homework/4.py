def bracket(x,l):
    for x in range(1,l):
        if x == "(":
            n=n+1
        if x == ")":
            s=s+1
return s,n
    
a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lst = sorted(lst)
lft = ''.join(lst)
l=len(lft)
bracket(lft,l)
print(s,n)