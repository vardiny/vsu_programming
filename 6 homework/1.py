storage = {}
def set_value(key):
    return storage[key]
def get_value(key,value):
    storage[key] = value
get_value("XYZ", 7)
get_value("ABC", 42)
print(set_value("XYZ"))