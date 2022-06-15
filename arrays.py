# lists are very powerful but we have to use array when we are dealing with large number of data let's say more than 10000
# array perform faster and take less memory space than lists
from array import array
numbers = array("i", [3, 4, 5, 3, 2, 43, 4, 3])
print(numbers)
numbers.append(99)
print(numbers)
numbers.insert(3, 44)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(4)
print(numbers)
