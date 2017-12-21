#initial variable constants
INITIAL_BALANCE = 800
TARGET = INITIAL_BALANCE * 3
RATE=3.0

#initialize variable used with the loop
balance = INITIAL_BALANCE
year = 0

#count the three years required for the investment to triple
while balance < TARGET:
    year  = year + 1
    interest =balance * RATE / 100
    balance = balance + interest

 #print and run
print ("The investment tripled after", year, "years.")
