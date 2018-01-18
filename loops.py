#how do you stop this loop

name= ' '
while name != 'your name':
        print('Please type your name.')
        name= input( )
print('Thank you')

#to stop loop, type 'your name'

#using break( ) in a loop

while True:
    print('Please type your name')
    name = input( )
    if name == 'your name':
        break

#using continue( ) and break ( ) to control the loop

while True:
    print('Enter your username')
    name = input ( )
    if name != "julia":
        continue
     #this will continue the loop if the username entered is not julia --- it will ask for the username again

#when the username is entered correctly, the program continues:

    print('Hello Julia, what is your password?')
    password = input( )
    if password == "banana":
        break
print('Welcome!')
    
