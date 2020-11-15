#use a while loop to generate a random number between 1 to 10 and until you get the number 5. Every time loop runs increment variable i.

from random import randint
 
number = 0
i = 0
 
while number != 5:
    i += 1
    number = randint(1, 10)
    print(number)