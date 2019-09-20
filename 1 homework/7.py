x = int(input())
y = int(input())
for s in range(x, y + 1):
    if not s % 5:
        print(s)
