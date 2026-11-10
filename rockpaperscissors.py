import random

player = input("Rock (r), Paper (p), Scissors (s): ")
computer = random.choice(["r", "p", "s"])

# Player Wins
if player == "r" and computer == "s":
    print("Rock vs Scissors, Player Wins")

elif player == "p" and computer == "r":
    print("Paper vs Rock, Player Wins")

elif player == "s" and computer == "p":
    print("Scissors vs Paper, Player Wins")

# Player Loses
elif player == "s" and computer == "r":
    print("Scissors vs Rock, Computer Wins")

elif player == "r" and computer == "p":
    print("Rock vs Paper, Computer Wins")

elif player == "p" and computer == "s":
    print("Paper vs Scissors, Computer Wins")

# Draw
elif player == computer:
    print("It's a Draw!")

else:
    print("Wrong input!")

print("Computer chose:", computer)