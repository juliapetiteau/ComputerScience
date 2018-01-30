#code for luggage weight price

weight = float(input("How much does your luggage weigh?"))
if weight >120:
    print("Your luggage is too heavy for this flight")
elif weight > 50:
    print ("There is a $25 fee for this luggage")
else:
    print("Your luggage is accepted as is")
