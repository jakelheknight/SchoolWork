 # This is in python 3 I wrote it in my ide that I already had installed.
 # It goes above what we were doing in class. I hope that is alright.
 
# Setting variables-----------------------------------
Tax = .02;
Tip = .15;
true = 1;
done = 'n';
while true == 1:
    try:
        # Prompt user for amount --------------------------------
        amount = float(input("What was the bill amount? "));

        # Print amount
        print("Your subtotal is $" + str(amount));

        # Calcualte Tax and print
        print("The tax is $"+ str(Tax*amount));

        # Calculate Tip and print
        print("the tip is $"+ str(Tip*amount));

        # Calculate Total and print
        print("Your bill with tax and tip is $"+str(amount*(1+Tax+Tip)));
        print
        done = input("Are you done y/n ");
        print
        print 
        if done == 'y':
            true = 0;
    
    except ValueError:
        print("Plese input a number with no other charicters.");


 
