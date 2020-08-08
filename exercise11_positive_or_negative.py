from random import randint
x = randint(-100, 100)
while x == 0:
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:
    y = randint(-100, 100)

if x > 0 and y > 0:
    print("both are positive numbers")
elif x < 0 and y < 0:
    print("both are negative numbers")
elif x > 0 and y < 0:
    print("x is positive and y is negative number")
else:
    print("y is positive and x is negative number")
