# 4 different data types

# integer
3
#float
3.0
#string
'hello'
#variable
price = 3

#2

(4 < 5) (5 < 6) #output = true

#4

total = 0
for number in range (100):
    total = total + number
    print(total) #sum = 4950

#5

'hello' == 'Hello' #false
True != False #true
42 == '42' #false

myage = 29
myage>= 15 #true
myage == 15 #false

#program that dispalys all the even numbers in range 1 to 30

for number in range(30):
    if number%2==0:
        print(number, 'is even')

#program that displays all the even numbers from 15 to 30

for number in range(15,30):
    if number%2==0:
        print(number, 'is even')
