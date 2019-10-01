def bracket(f,l):
    n = int (0)
    s = int (0)
    for x in range(0,l):
        if f[x] == "(":
            n = n+1
        elif f[x] == ")":
            s = s+1
    k = str(s - n)
    m = str(n - s)
    if s > n:
        if k == 1:
            return ("You miss the opening 1 bracket")
        else:
            return ( "You miss the opening"+" "+k+" "+"brackets")
    elif s < n:
        if m == 1:
            return ("You miss the ending 1 bracket")
        else:
            return ("You miss the ending"+" "+m+" "+"brackets")
    elif s == n == 0:
        return("You forgot to write something (((")
    else: 
            return ("Well done!!!")
a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lft = ''.join(lst)
l = len(lft)
m = str ()
m = bracket(lft,l)
print(m)