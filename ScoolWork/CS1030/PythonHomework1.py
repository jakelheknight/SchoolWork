# Prompts and varables.

name = input("Employee Name: ")
basePay = input("Hourly Rate: ")
baseHours = input("Regular hours this pay period: ")
overtimePay = input("Overtime rate: ")
overtimeHours = input("Overtime hours this pay period: ")
taxRate = 0.12

# Calculate wage and tax.

try:
    grose = float(basePay)*float(baseHours) + float(overtimePay)*float(overtimeHours)
    net = grose*(1-taxRate)
    sucess = 1
    
except ValueError:
    grose = "Invalid Input"
    sucess = 0

# Display

print()
print()
print(name + "'s pay summery:")
if sucess == 1:
    print("Base pay rate: %.2f" %(float(basePay)))
    print("Regular hours worked: %.2f" %(float(baseHours)))
    print("Overtime pay rate: %.2f" %(float(overtimePay)))
    print("Overtime hours worked: %.2f" %(float(overtimeHours)))
    print("Grose pay: %.2f" %(float(grose)))
    print("Tax deductions: %.2f" %(grose*.12))
    print("Net pay after tax and deductions: %.2f" %(net))
    
else:
    print(grose)
