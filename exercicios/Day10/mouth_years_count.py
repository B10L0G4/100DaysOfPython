def count_years(year):

    four = year % 4
    hundred = year % 100
    four_hundred = year % 400

    if four == 0:
        while hundred >= 0:
            while four_hundred >= 0:
                return True
    else:
        return False

def odd_even(mounth):
    mounth = mounth % 2

    if mounth == 0:
        par = True
        return par
    else:
        impar = False
        return impar

def days_in_month(year, mounth):
    
    month_day = [31,30,29,28]
    months=['Jan', 'Fev', 'Mar', 'Abril', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    a = ''
    for mon in months:
        mon = mon + a
    mes=months[mounth -1]
        
    for m in month_day:
        continue
        
    par = month_day[1]
    impar= month_day[0]
    fev_par = month_day[2]
    fev_impar = month_day[3]

    if count_years(year) == True:
        if odd_even(mounth) == True:
            if mounth == 2:
                print(f'O mês de {mes} tem {fev_par} dias e o ano de {year} é bissexto')
            else:
                print(f'O mês {mes} tem {par} dias e o ano de {year} é bissexto')
        else:
            print(f'O mês {mes} tem {impar} dias e o ano de {year} é bissexto')
    else:
        if odd_even(mounth) == True:
            if mounth == 2:
                print(f'O mês de {mes} tem {fev_impar} e o ano de {year} não é bissexto')
            else:
                print(f'O mês {mes} tem {par} dias e o ano de {year} não é bissexto')
            
        else:
            print(f'O mês {mes} tem {impar} e o ano de {year} não é bissexto')

       
        

year = int(input('Which year you want to check? '))
mounth = int(input('Which mounth you want to check'))

days_in_month(year, mounth)


       

