def hash(key):
    result = 0
    for i in key:
        result += ord(i)
    return result % 13
storage = [0] * 13
def set_value(key):
    index = hash(key)
    return storage[index]
def get_value(key,value):
    index = hash(key)
    storage[index] = value
get_value("XYZ", 7)
get_value("ABC", 42)
print(set_value("XYZ"))