import math
import random

def welcome( ):
    menu= input("Welcome! Press 1 for basic operation and Press 2 for more advanced operations")
    if menu == "1":
        calculate_basic( )

    elif menu == "2":
        calculate_adv( )

def calculate_basic( ):
    operation = input('''
Please type the math operation you would like to complete
+ for addition
- for subtraction
* for multiplication
% for modulus
/ regular division
// integer division
''')
    firstnumber = float(input("Please enter the first number:"))
    secondnumber = float(input("Please enter the second number:"))

    if operation == '+':
        print("{} +{} =".format (firstnumber, secondnumber))
        print(firstnumber + secondnumber)

    elif operation == "-":
        print("{} - {}=" .format(firstnumber, secondnumber))
        print(firstnumber - secondnumber)

    elif operation == "*":
        print("{} * {} =".format (firstnumber, secondnumber))
        print(firstnumber * secondnumber)
        
    elif operation == "%":
        print("{} % {} =".format (firstnumber, secondnumber))
        print(firstnumber % secondnumber)

    elif operation == "/":
        print("{} / {} =".format (firstnumber, secondnumber))
        print(firstnumber / secondnumber)
        
    elif operation == "//":
        print("{} // {} =".format (firstnumber, secondnumber))
        print(firstnumber // secondnumber)

    else:
        print("You have not typed a valid operator. Run program again")
        runagain( )

def calculate_adv( ):
    operation_adv = input('''
Please type the math operation you would like to complete
cir for area of a circle
rec for area of a rectangle
tri for area of a triangle
pent for area of a pentagon
cos for cosine of x
tan for tangent of x
sin for sine of x
''')

    if operation_adv == 'cir':
        radius = float(input("Please enter the length of the radius:"))
        print(" 3.14 * { } = A".format (radius))
        area_of_circle = 3.14 * radius
        print(area_of_circle)

    elif operation_adv == "rec":
        height = float( input("Please enter the length of the height:"))
        length = float( input("Please enter the length:"))
        print( "{} *{} = A".format (height, length))
        area_of_rec = height * length
        print(area_of_rec)

    elif operation_adv == "tri":
        base = float( input("Please enter the length of the base:"))
        height1 = float( input("Please enter the length of the height:"))
        print( "({} * {}) / 2 = A" .format(base, height1))
        area_of_tri = (base * height1) /2 
        print(area_of_tri)
        
    elif operation_adv == "pent":
        apothem = float( input("Please enter the length of the apothem:"))
        side_length = float( input("Please enter the length of the side length:"))
        perimeter = side_length * 5
        print("({}*{}) /2 = A" .format(apothem, perimeter))
        area_of_pent = (apothem * perimeter) /2
        print( area_of_pent)

    elif  operation_adv == "cos":
        x = float(input("Please enter the value of x:"))
        cos = math.cos(x)
        print(cos)
        
    elif  operation_adv == "tan":
        x = float(input("Please enter the value of x:"))
        tan = math.tan(x)
        print(tan)

    elif  operation_adv == "sin":
        x = float(input("Please enter the value of x:"))
        sin = math.sin(x)
        print(sin)
        
    else:
        print("You have not typed a valid operator. Run program again")
        runagain( )

def runagain( ):
    again= input("Do you want to calculate again? Y/N")
    if again.upper( ) == "Y":
        print( )
        welcome( )
    elif again.upper( )== "N":
        print("Exit")

    else:
        runagain( )

welcome( )


