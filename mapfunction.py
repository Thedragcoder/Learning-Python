items = [
    ('bluelabel', 25000),
    ('blacklabel', 20000),
    ('redlable', 19000)

]

# one way of extracting prices from items and displaying it in a separate list

forPriceList = []
for item in items:
    forPriceList.append(item[1])

print(forPriceList)

# the more elegant way to do this is using a map function

items = [
    ('bluelabel', 25000),
    ('blacklabel', 20000),
    ('redlable', 19000)

]

prices = list(map(lambda item:  item[1], items))
print(prices)
