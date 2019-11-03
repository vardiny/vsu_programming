size = 13
storage = [None] * size
 
def hash(key):
    result = 0
    for i in key:
        result += ord(i)
    return result % size
 
def set_value(key, value):
    index = hash(key)
    while storage[index]:
        index += 1
    storage[index] = key, value
 
def get_value(key):
    index = hash(key)
    key2, value = storage[index]
    while key2 != key:
        index += 1
        key2, value = storage[index]
    return value
 
 
print(storage)
set_value('abc', 7)
print(storage) 
set_value('cba', 42)
print(storage)
print(get_value('cba'))
print(storage)