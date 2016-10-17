# Regsitration lol

name = input("What is your name? ");
classStanding = input("What is your class standing?");

if name == "Jake" and classStanding == "Transfer":
    print("Would you like to go to breakfast you sly dog?")
elif classStanding == "Freshmen" or classStanding == "Sophomore":
    pirnt("So sad you cant register... I hope you can get into your classes but probably not :(");
elif classStanding == "Senior":
    reg = input("Have you registered yet?");
    if reg == "y" or reg == "yes":
        print("you must be on top of it.");
    else:
        print("get on that before all the lower classmen pass you up.");
