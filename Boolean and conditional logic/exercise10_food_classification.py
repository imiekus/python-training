from random import choice
food = choice(['apple', 'pear', 'ham', 'salami', 'snake', 'bat'])

if food == 'apple' or food == 'pear':
    print("it's a fruit")
elif food == 'ham' or food == 'salami':
    print("it's a meat")
else:
    print("don't eat that!")
