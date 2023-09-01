
year = int(input('Which year you want to check? '))

four = year % 4
hundred = year % 100
four_hundred = year % 400

if  four == 0:
    while four == 0:
        while hundred >= 0:
            while four_hundred >= 0:
                print(f'The year {year} is Leap')
                four =- 1
                hundred =- 1
                four_hundred =- 1
else:
    print(f'The year {year} is Not Leap')