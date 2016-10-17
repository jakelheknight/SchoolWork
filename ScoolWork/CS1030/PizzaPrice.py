import sys
import datetime

# Print greeting
print("Welcome to wildcat pizzas Python ording system.")
print()
print()
# Prompt user for required input

name = input("Please enter your name: ")
print()

# For number inputs we need to make sure user inputs
try:
    size = abs(float(input("What size of pizza do you want to order in inches? ")))
except ValueError:
    print("Size must be a number. Please submit a new order. ");
    sys.exit()
print()

# Ask for toppings
try:
    numTop = abs(int(input("How many toppints would you like? ")))
except ValueError:
    print("Number of toppings must be a whole number. Please submit a new order. ")
    sys.exit()

print()
toppings = []
for ii in range(numTop):
    if ii != 0 and ii!=1 and ii!=2:
        toppings.append(input("What do you want as the %dth toping? " %(ii+1)))
    elif ii == 0:
        toppings.append(input("What do you want the 1st toping to be? "))
    elif ii == 1:
        toppings.append(input("What do you want the 2nd topping to be? "))
    elif ii == 2:
        toppings.append(input("What do you want the 3rd topping to be? "))
print()
print()

# Take out or delevory with loop to make sure proper input is accepted.
delivery = input("Take out (t) or Delevery (d)? ")
delivery = delivery.upper()
while(delivery != "D" and delivery != "T"):
    delivery = input("Invalid answer. Take out (t) or Delevery (d)? ").upper()
deliveryPrice = 0
print()

# Get address and strip off the zip code. Check to see if number.
if delivery == "D":
    address = input("Please enter street addres: ")
    city = input("Pleas enter City: ")
    zipcode = input("pleas enter the zip code: ")
    while not zipcode.isdigit():
        zipcode = input("Invalid zip code please enter a zip code.")
    zipcode = int(zipcode)
    print()

# Set delevery cost and time
    if zipcode == 84041:
        deliveryPrice = 6.50
        delivryTime = datetime.datetime.now()+datetime.timedelta(0, 30*60)
    else:
        deliveryPrice = 7.50
        delivryTime = datetime.datetime.now()+datetime.timedelta(0, 45*60)
        
        
#  Calculate price of pizza
pizzaPrice = 5.0 + size*0.5
orderPrice = pizzaPrice + deliveryPrice
print()
print()
print("*------------------------------------------------------*")
print()
# print important information
print("Thankyou %s for ordering from Wild Cat Pizza." %(name))
print()
print("Toppings: ")
for ii in range(numTop):
    print(toppings[ii])
print()
print("Pizza cost: %.2f" %(pizzaPrice))
if delivery == "D":
    print("Delevery cost: %.2f" %(deliveryPrice))
else:
    print("Delevery Price: Takeout")
print("-----")
print("Total Price: %.2f" %(orderPrice))
print()
print()
if delivery == "D":
    print("Your pizza will arrive at", delivryTime.strftime("%I") + ":" + delivryTime.strftime("%M"))
else:
    print("Your pizza will be ready in 15 minutes.")
