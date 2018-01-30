#build a calculator

print("This program calculates mpg")

while True: 
    miles_driven = float(input("Enter miles driven:"))
    gallons_used = float(input("Enter gallons used:"))
    mpg = miles_driven / gallons_used

    print("Your miles per gallon is", mpg)

    answer=input("Do you need to calculate another mpg? Y/N")

    if answer == "Yes" or answer == "y" or answer == "Y" or answer == "yes":
        continue
    else:
        break 
