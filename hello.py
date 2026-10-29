# print("Hello My name is Janer, I'm using Python in vscode!")
card_Valid = True
pin_Correct = True

card_Valid = float(input("Enter your card name: "))
pin_Correct= float(input("Enter your PIN (4 digits)"))

if card_Valid == True and pin_Correct == True:
    print("Access Granted")

    if card_Valid == False and pin_Correct == False:
       print("Invalid Access")
       
else: 
   print("Invalid Access")