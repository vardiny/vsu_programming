def bracket(f,l):
    open_b = 0
    end_b = 0
    for x in f:
        if x == "(":
            open_b = open_b + 1
        elif x == ")":
            end_b = end_b + 1
    k = str(end_b - open_b)
    m = str(open_b - end_b)
    if end_b > open_b:
        if k == 1:
            return ("You miss the opening 1 bracket")
        else:
            return ( "You miss the opening" + " " + k + " " + "brackets")
    elif end_b < open_b:
        if m == 1:
            return ("You miss the ending 1 bracket")
        else:
            return ("You miss the ending" + " " + m + " " + "brackets")
    elif open_b == open_b == 0:
        return("You forgot to write something (((")
    else: 
            return ("Well done!!!")
a = input()
lst = []
while a: 
    lst.append(a)
    a = input()
lst2 = ''.join(lst)
l = len(lst2)
m = str ()
m = bracket(lst2,l)
print(m)