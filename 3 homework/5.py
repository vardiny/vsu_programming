a = int(input())
lst = []
while a:
    lst.append(int(a))
    a = input()
print(sum(lst) / len(lst))