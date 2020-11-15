import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# Let player play again if they want!

while True:
    player = int(input("Guess a number between 1 and 10: "))
    if player > 10 or player < 1:
        print("Ugh... That's out of range, read instructions please...")
    elif player > random_number:
        print("Too high, try again :)")
    elif player < random_number:
        print("Too low, try again :)")
    else:
        print("Alright, you guesssed it! You won!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
        else:
            print("It was fun, thanks!")
            break
