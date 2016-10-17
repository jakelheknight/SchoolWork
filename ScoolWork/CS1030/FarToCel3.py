# This is a temperature converted I also wrote in python 3

# Take user input make sure its a number

true = 1;
done = 'n';
far = -1000;
cel = -1000;
conv = ""


while true == 1:
    
    conv = input("Press C to convert to celsius. Press F to convert to fahrenheit")
    
    try:
        if conv == "C" or conv == "c":
            far = float(input("Enter the temperiture in fahrenheit. "));
            # Convert to cel
            cel = (far - 32)*(5.0/9.0);
            print("%.1f degrees fahrenheit is %.1f degrees celsius." %(far,cel))
        elif conv == "F" or conv == "f":
            cel = float(input("Enter the temperiture in celsius. "));
            # Convert to cel
            far = 32.0 + (cel*9.0/5.0);
            print("%.1f degrees celsius is %.1f degrees fahrenheit." %(cel,far))
        else:
            print("Not an option.")
            exit
        #check with user if they are done
        done = input("Are you done? (y/n) ");
        print
        print 
        if done == 'y':
            true = 0;
        ## deal with user stupidity.......
    except ValueError:
        print("Plese input a number with no other charicters.");


