def hash(key):
    result = 0
    for i in key:
        result += ord(i)
    return result % 13
storage = [0] * 13
q = 1
def deleted_f(index, key):
    j = index + q
    while storage[j] == 0 or storage[j].key != storage[index].key:
        if storage[j] == 0:
            storage[j] = key
            index = j
            return index
            break
        j += q
    storage[index] = storage[j]  
def set_value(key):
    index = hash(key)
    return storage[index]
def get_value(key,value):
    index = hash(key)
    if storage[index] != 0:
        deleted_f(index, key)
    else:
        storage[index] = value
get_value("XYZ", 7)
get_value("ABC", 42)
print(set_value("XYZ"))