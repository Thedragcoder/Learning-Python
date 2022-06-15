# a tuple is another data structure which is read only list we cant add remove or modify the object or an item in tuple
point = (3, 4)
pointEmpty = ()
pointSecond = (9, 3)
pointConcatenate = point + pointSecond
print(pointConcatenate)
pointListToTuple = tuple([3, 44, 3, 3, 3])
print(pointListToTuple)
print(type(pointListToTuple))
print(pointListToTuple[0:2])
# unpacking a tuple
x, y = point
print(x)
print(y)
if 10 in point:
    print('exists')
else:
    print('the data doesn\'t exist')
