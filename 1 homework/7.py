x = int(input())
y = int(input())
n = 0
for s in range(x, y + 1):
    if not s % 5:
        n += s
print (n)
 