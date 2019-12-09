size = 6
storage = [[] for _ in range(size)]
 
def hash(key):
    result = 0
    for i in key:
        result += ord(i)
    return result % size
 
def set_value(key, value):
    index = hash(key)
    for x in storage[index]:
        if x[0] == key:
            x[1] = value
            break
    else:
        storage[index].append([key, value])
 
def get_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            return i[1]

def del_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            storage[index].remove(i)
            break
 
set_value('abc', 1)
set_value('abc', 2)

set_value('cba', 4)
set_value('cba', 10)

set_value('abdc', 1123)
set_value('abdc', 2123)
set_value('zxc', 2123)

set_value('XYN', 3)
set_value('XYN', 11)
print(storage)
del_value('XYN')

print(get_value('abc'))
print(get_value('cba'))
print(get_value('XYN'))

print(get_value('abdc'))
print(get_value('abdc'))
print(get_value('zxc'))

print(storage)
