dic = {
    'Ala':10,
    'Eli':7,
    'Ilo':7,
    'Oli':5,
    'Uta':10
}
dic1 = {}
for i in dic:
    score = dic[i]
    if score >= 10:
        dic1[i] = 'Outcomming'
    elif score >=6:
        dic1[i] = 'OK'
    else:
        dic1[i] = 'Fail'
print(dic1)
