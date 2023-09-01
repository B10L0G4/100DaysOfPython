print(" Welcome to the Rollercoster! ")

height = float(input('Whats is your height in cm? '))

if height >= 120:
    print('You able to ride in the rollercoaster! Buy your ticket')
    age = int(input('What is your age?  '))
    if age >= 18:
        print('Your ticket is $18')
    elif age < 12:
        print('Your ticket is $7')
    else:
        print('Your ticket is $12')
else:
    print('You unable to ride! Sorry, you have to grow taller before you can ride. ')