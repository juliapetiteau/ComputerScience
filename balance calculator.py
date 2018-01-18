#this program calculates the time that the balance of a bank account will take to double

initial_balance = 1000
target = initial_balance * 2
rate = 1.2

year = 0
balance = initial_balance


print("Your initial balance is", initial_balance)

while balance < target:
    year = year + 1
    interest = balance * rate /100
    balance = balance + interest
print("Your investment doubled after", year, "years.")

#this program calculates the monthly charge of a telephone bill given a number of minute of calls

minutes = float(input("Enter the number of minutes of calls for this month"))
base_price= 29.95
tax = base_price * 1.125

if minutes <= 300:
    cost = base_price + tax
    print('Your total cost for this month is', cost)

if minutes > 300: 
    total_minutes = minutes - 300
    other_cost = total_minutes * 0.45
    tax_total = (base_price + other_cost) * 1.125
    print('Your total cost for this month is', tax_total)


#this program calculates the cost of fuel

trip_distance =float(input("Enter the trip distance in miles"))
fuel_efficiency = float(input("Enter fuel efficiency in miles per gallon"))
gas_price= float(input("Enter the gas price per gallon"))
cost_of_fuel = trip_distance / fuel_efficiency * gas_price
print('Your cost of fuel is', cost_of_fuel)

#this program calculates gas mileage then converts to metric

current_reading = float(input("Enter your current odometer reading in miles"))
previous_reading= float(input("Enter the previous odometer reading in miles"))
gas_added= float(input("Enter the amount of gas added to the tank in gallons"))
gas_price= float(input("Enter the gas price per gallon"))

dis_traveled= current_reading - previous_reading
miles_gallon =  dis_traveled / gas_added
print("Your gas mileage is", miles_gallon, "miles per gallon")

unit_cost = miles_gallon / gas_price
print("Your unit cost is", unit_cost, "per dollar")

dis_traveled_m = dis_traveled * 1.60934
gas_added_l =  gas_added * 3.78541
miles_gallon_m = dis_traveled_m / gas_added_l
print("Your gas mileage is", miles_gallon_m, "kilometers per liter.")






 
