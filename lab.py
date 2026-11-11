# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

print("Welcome to the Debugging Lab!")

name = input("Enter your name:")
print("Hello " + name + "!" + " Let's calculate your test scores.")

#removed the colums in 88
scores = [85, 90, 78, 88, 92]

total = 0

#added : at the end of scores and an s in total + scores
for score in scores:
    total = total + score

#added a comma next to average because for print to show the score, it needs the average. 
average = total / len(scores)

#added a comma before average
print("Your average score is:", average)

highest = 0
for s in scores:
    if s > highest:
        highest = s
#added a comma before highest aswell
print("Your highest score was:", highest)

