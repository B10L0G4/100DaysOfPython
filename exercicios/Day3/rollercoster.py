print(" Welcome to the Rollercoster! ")

height = float(input('Whats is your height in cm? '))

if height >= 120:
    print('You able to ride in the rollercoaster! Buy your ticket')
    bill = 0
    age = int(input('What is your age?  '))
    if age >= 18:
        bill = 18
        print(f'Your ticket is ${bill}')
    elif age < 12:
        bill = 7
        print(f'Your ticket is ${bill}')
    else:
        bill = 12
        print(f'Your ticket is ${bill}')
    photo = input('You want a photo? Y or N  \n')
    photo = photo.upper()
    if photo == 'Y':
        bill = bill + 3
        print(f'Your ticket is ${bill}')
    else:
        print(f'Your ticket is ${bill}')
else:
    print('You unable to ride! Sorry, you have to grow taller before you can ride. ')