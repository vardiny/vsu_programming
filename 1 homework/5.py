x = float(input())
y = float(input())
if x > 0 and y > 0:
    print('1/4 on 1')
elif x < 0 and y > 0:
    print('1/4 on 2')
elif x < 0 and y < 0 :
    print('1/4 on 3')
elif x > 0 and y < 0:
    print('1/4 on 4')
else:
    print('Point on axis')
