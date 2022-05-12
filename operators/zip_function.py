# Groceries - write a function that take in a list of item and their price .Make it return list of item another of their price
def shopping_list(groceries):
    items,prices=zip(*groceries)
    return list(items), list(prices)
shoping=shopping_list([('milk',29),('eggs',19),('bananas',12)])
print(shoping)