""" Final exam for CS 1030
You have been hired by an auto dealership to writ a program that calcuates the total price of a vehicle based on type of car.

Prompt the salesperson for the price and type of each car then display the total price

5% tax on antique cars
7.5% on luxury cars
10% tax on race cars
2.5% tax on all others

"""
import sys
#Welcome to the program.
print("Welcome to WildCat used cars price calculator.")

#Name arrays for car type base price and price after tax so info is stored and easy to access.
carBasePrice = []
carType = []
carPrice = []

#Loop 14 times once for each car.
for ii in range(14):
    
        #prompt user for car price info in a friendly way.
        if ii != 0 and ii!=1 and ii!=2:
            carBasePrice.append(input("What is the %dth car's price? " %(ii+1)))
        elif ii == 0:
            carBasePrice.append(input("What is the 1st car's price? "))
        elif ii == 1:
            carBasePrice.append(input("What is the 2nd car's price? "))
        elif ii == 2:
            carBasePrice.append(input("What is the 3rd car's price? "))
            
        #Make sure price is a number.
        try:
            tmp = float(carBasePrice[ii])
        except ValueError:
            print("Please start over and enter prices as numbers.")
            sys.exit()

        #prompt user for the car type.
        print()
        print("For car type use A for Antique car, L for Luxury car, R for Race car, and O for Other type of car.")
        if ii != 0 and ii!=1 and ii!=2:
            carType.append(input("What is the %dth car's type? " %(ii+1)).upper())
        elif ii == 0:
            carType.append(input("What is the 1st car's type? ").upper())
        elif ii == 1:
            carType.append(input("What is the 2nd car's type? ").upper())
        elif ii == 2:
            carType.append(input("What is the 3rd car's type? ").upper())
        while not (carType[ii]=="A" or carType[ii]=="L" or carType[ii]=="R" or  carType[ii]=="O"):
            carType[ii] = input("Please enter a valid code For car type. ").upper()

        #Assign tax value.
        if carType[ii] == "A":
            taxRate = .05
        elif carType[ii] == "L":
            taxRate = .075
        elif carType[ii] == "R":
            taxRate = .10
        else:
            taxRate = .025
        #calcuate the iith cars price
        carPrice.append((1+taxRate)*tmp)
        print()
        if ii != 0 and ii!=1 and ii!=2:
            print("The %dth car's price is. %.2f" %(ii+1, carPrice[ii]))
        elif ii == 0:
            print("The 1st car's price is %.2f " %(carPrice[ii]))
        elif ii == 1:
            print("The 2nd car's price is %.2f " %(carPrice[ii]))
        elif ii == 2:
            print("The 3rd car's price is %.2f " %(carPrice[ii]))
        print()
        print("*---------------------------------------------*")
        print()

print()
print()
print()
# print out all the car prices.
print("The car prices on the lot are: ")
for ii in range(14):
    print("Car %d costs : $%.2f" %(ii+1,carPrice[ii]) )
print()
print()
print("Thank you for using the car price calcuator.")
