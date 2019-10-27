def time_of_year(n):
    if n < 3 or n == 12:
        return "Winter"
    elif n < 6:
        return "Spring"
    elif n < 9:
        return "Summer"
    elif n < 12:
        return "Autumn"
n = int(input("Enter the number of month: "))
print(time_of_year(n))