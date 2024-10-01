print("Welcome to this text based adventure!")
print("You currently stand in a place you don't recognise, the only clear way to go is forwards")
print("do you go forwards?")
choice = input()

while choice != "yes":
 print("that's not an option")
 print("do you go forwards?")
 choice = input()

if choice == "yes":
 print("you go forwards, suddenly you fall down a pit you didn't see and die")
 print("GAME OVER")
