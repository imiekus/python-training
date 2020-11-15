from random import randint
player_wins = 0
computer_wins = 0

print("Hi you, let's play rock, paper, scissors!")

while player_wins < 2 and computer_wins < 2:
    print(f"Your score: {player_wins}, Computer score: {computer_wins}")

    player = input("...Rock...  ...Paper... ...Scissors... Make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"You played: {player}")
    print(f"Computer played: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move - rock, paper or scissors.")

if player_wins > computer_wins:
    print("You're the winner!")
elif player_wins == computer_wins:
    print("It's a tie, nobody wins.")
else:
    print("Sorry, Computer won this time.")

print(f"FINAL SCORE: you: {player_wins}, computer: {computer_wins}.")