# print("Hello My name is Janer, I'm using Python in vscode!")

NAME = "Janer"
PIN = "1234"

entered_name = input("Enter your card name: ")
entered_pin = input("Enter your PIN (4 digits): ")

card_Valid = (entered_name == NAME)
pin_Correct = (entered_pin == PIN)

if card_Valid == NAME and pin_Correct == PIN:
    print("Access card accepted and Access granted")

else:
   if card_Valid != NAME and pin_Correct != PIN:
      print("Invalid access and Incorrect pin")

   else:
      if card_Valid == NAME and pin_Correct != PIN:
         print("Access card accepted but Incorrect pin")

      else: 
         if card_Valid != NAME and pin_Correct == PIN:
            print("Invalid access but correct-pin")