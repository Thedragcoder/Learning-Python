shoppingList = [
    ('product1', 200),
    ('product2', 300),
    ('product3', 400),
    ('product4', 500),
    ('product5', 600),
    ('product6', 700),
    ('product7', 800),
]

usingMapFunction = list(map(lambda item: item[1], shoppingList))
print(usingMapFunction)
# Achieving the same result using list comprephension
usingListComprehension = [item[1] for item in shoppingList]
print(usingListComprehension)

usingFilterFunction = list(filter(lambda item: item[1] >= 400, shoppingList))
print(usingFilterFunction)
# achieving the same result using list comprehension
filterUsingListComprehension = [
    item for item in shoppingList if item[1] >= 300]
