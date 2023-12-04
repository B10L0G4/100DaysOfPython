def count_years(year):

    four = year % 4
    hundred = year % 100
    four_hundred = year % 400

    print(four, hundred, four_hundred)

    if four == 0:
        while hundred >= 0:
            while four_hundred >= 0:
                return True
    else:
        return False

def odd_even(month):
    month = month % 2

if month == 0:
    par = True
    return par
else:
    impar = False
    return impar

def days_in_month(year, month):
    month_day = [31,30,29,28]
    months= [Jan, Fev, Mar, Abril, Maio, Jun, Jul, Ago, Set, Out, Nov, Dez]

    for m in month_day:
        print(m)
        print(month_day)

year = int(input('Which year you want to check? '))
mounth = int(input('Which mounth you want to check'))
count_years(year)
