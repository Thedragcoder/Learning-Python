letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4, 5, 6, 7, 4, 3, 5, 3, 5, 3, 5, 2, 1]
matrix = [[1, 2], [2, 3]]
combinedLettersNumbers = letters + numbers
print(combinedLettersNumbers)
zeros = [0] * 5
print(zeros)
numbers = list(range(20))
print(numbers)
chars = list('This is list in python')
print(len(chars))

# Accessing items
print(letters[0])
letters[1] = "B"
print(letters)
print(letters[0:3])
# adding steps to accessing items
print(letters[0:4:2])

# list unpacking
numbersUnpacking = [1, 66, 66, 4, 45, 546, 23, 4346, 475]
firstUnpacked, secondUnpacked, *otherUnpacked = numbersUnpacking
print(firstUnpacked, secondUnpacked, otherUnpacked)
