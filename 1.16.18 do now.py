n=1
m=-1
if n < -m:
    print(n)
else:
    print(m)

from math import sqrt
x=sqrt(2.0)
y=2.0
if x*x==y:
    print(x)

else:
    print(y)

#using input( ) to make an interactive program

from math import sqrt
x= float(input('Enter the number you want to get the square root for'))
num_squared= sqrt(x)
print('Your number is' , num_squared)
