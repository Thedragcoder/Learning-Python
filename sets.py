convertToSet = [2, 3, 4, 5, 6]
toSet = set(convertToSet)
print(toSet)
secondSet = {6, 5, 2, 55, 34}
union = toSet | secondSet
intersection = toSet & secondSet
difference = toSet - secondSet
eitherInTosetOrsec = toSet ^ secondSet
print(union)
print(intersection)
print(difference)
print(eitherInTosetOrsec)
if 2 in secondSet:
    print('yes')
# accesing item is not supported in sets
