#VACATION APP

print("Welcome!")
while True:
    days = int(input("How many nights are you planning to stay at a hotel?"))
    print("Room types: 1 bed, family, 1 bed suite, or family suite")
    roomtype = input("What kind of room would you like to stay in?")
    
    def hotel_cost():
        if roomtype == "1 bed":
            return (75 *days)
        elif roomtype == "family":
            return (90 * days)
        elif roomtype == "1 bed suite":
            return (109 * days)
        elif roomtype == "family suite":
            return (135 * days)
   
    print( '''Here are the travel destinations provided by this airline:

    - Los Angeles
    - San Francisco
    - Miami
    - Chicago
    - Washington D.C.
    - Honolulu
    - Kauai
    ''')
    city = input("Enter which city you want to travel to:")

    familysize = int(input("How many people will be flying?"))
    
    def plane_ride_cost():
        if city == "Los Angeles":
            return (512 * familysize) 

        elif city == "San Francisco":
            return (498 * familysize)

        elif city == "Miami":
            return (374 * familysize)

        elif city == "Chicago":
            return (258 * familysize)
    
        elif city == "Washignton D.C.":
            return (154 * familysize)

        elif city == "Honolulu":
            return (612 * familysize)

        elif city == "Kauai":
            return (586 * familysize)
           

    def rental_car_cost():
        cost = 55 * days
        if days > 7:
            cost = cost - 55
        elif days >= 3 and days<7:
            cost = cost - 15
        return cost       

    total = hotel_cost() + plane_ride_cost() + rental_car_cost()

    userInput = input("Do you have a discount code?")
    if userInput == "10OFF":
        new_total = total * 0.9
    else:
        new_total = total * 1

    tax = 1.08
    total_tax = int(new_total * tax)

    print(" ")
    print("VACATION COSTS")
    print(".........................................................")
    print("Your hotel cost for", days,"days would be", hotel_cost())
    print("Your plane ride cost to", city, "would be", plane_ride_cost())
    print("Your rental car cost for", days," days would be", rental_car_cost())
    print(" ")
    print(" Your total trip cost would be", total_tax, "dollars")

    answer = input("Would you like to book your trip?")
    if answer == "Yes" or answer == "yes":
        creditcard = input("Enter your credit card information:")
        print("Thank you for booking your trip to", city, ". You will be charged", total_tax, "dollars.")
        break 



