# calculate the area of a rectangle

print("This program will calculate the area of a rectangle")

while True:
    width = float(input("Enter the width of the rectangle"))
    length = float(input("Enter the length of the rectangle"))

    area = length * width

    print("The area of the rectangle is", area)
    answer = input("Would you like to calculate the area again?")

    if answer == "Yes" or answer == "yes":
        continue
    else:
        break
