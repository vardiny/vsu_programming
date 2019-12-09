from collections import deque
name = {
    "Pavel": ["Lily", "Sophy"],
    "Lily": ["Amy", "Bob"],
    "Bob": ["Darel", "Dima", "Sasha"]
}
def doter(x):
    return not len(x) % 2 and x[0] == "D"

a = deque(name["Pavel"])
b = []
while name:
    person = a.popleft()
    if person not in b:
        if doter(person):
            print(person)
            break
        else:
            a += name.get(person, [])
        b.append(person)