# Print out a string depending on if food is a value in bakery_stock print out a string that states how many items are left.

# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])
 
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"There is {bakery_stock[food]} of {food} left")
else:
    print(f"{food}? We don't make that")