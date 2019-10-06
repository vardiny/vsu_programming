def bracket(f):
    open_b = 0
    end_b = 0
    open_b = f.count("(")
    end_b = f.count(")")
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
m = str ()
m = bracket(lst)
print(m)