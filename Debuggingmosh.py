def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("start")
print(multiply(2, 4, 5))
