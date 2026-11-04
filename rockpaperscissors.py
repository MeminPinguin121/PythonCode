import random

player = input ("rock (r), paper (p), scissors (s)")
computer = random.randint (1,3)

#Player Wins
if player == "r" and computer == "s":
    print ("Rock vs Scissors, Player Wins")

elif player == "p" and computer == "r":
    print ("Paper vs Rock, Player Wins")

elif player == "s" and computer == "p":
    print ("Scissors vs Rock, Player Wins")

#Player Loses
elif player == "s" and computer == "r":
    print ("Scissors vs Rock, Computer Wins")

elif player == "r" and computer == "p":
    print (" Rock vs Paper, Computer Wins")

elif player == "p" and computer == "s":
    print ("Rock vs Scissors , Computer Wins")

#Draw
elif player == "r" and computer == "r":
    print ("Rock vs Rock, Draw")

elif player == "p" and computer == "p":
    print ("Paper vs Paper, Draw")

elif player == "s" and computer == "s":
    print ("Scissors vs Scissors, Draw")

else: print ("wrong imput")