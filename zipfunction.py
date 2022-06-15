itemOne = [3, 4, 6, 7, 8]
itemTwo = [33, 44, 55, 66, 88]
# using the zip function convert the list into [(itemOne,itemTwo),[(itemOne,itemtwo)]
convertedItem = list(zip(itemOne, itemTwo))
print(convertedItem)
# now add abcde in the same list
convertAndAdd = list(zip('abcde', itemOne, itemTwo))
print(convertAndAdd)
