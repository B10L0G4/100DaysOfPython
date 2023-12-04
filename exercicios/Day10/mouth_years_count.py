def count_years(year):

    four = year % 4
    hundred = year % 100
    four_hundred = year % 400

    print(four, hundred, four_hundred)

    if four == 0:
        while hundred >= 0:
            while four_hundred >= 0:
                print(f'The year {year} is Leap')
                hundred = - 1
                four_hundred = - 1
    else:
        return(f'The year {year} is Not Leap')


year = int(input('Which year you want to check? '))
# mounth = int(input('Which mounth you want to check'))

count_years(year)