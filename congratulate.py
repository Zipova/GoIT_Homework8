from datetime import date
from collections import defaultdict

users = [{'name':'Vasia', 'birthday':'07-06-1992'}, {'name':'Yurii', 'birthday':'05-06-1982'}, {'name':'Bogdan', 'birthday':'06-06-1997'}, {'name':'Maria', 'birthday':'03-05-1980'}, {'name':'Anya', 'birthday':'23-09-2001'}, {'name':'Kiril', 'birthday':'11-04-1978'}, {'name':'Pavlo', 'birthday':'23-02-1999'}, {'name':'Sasha', 'birthday':'11-06-1983'}, {'name':'Nikita', 'birthday':'17-06-2000'}, {'name':'Olena', 'birthday':'13-06-2001'}, {'name':'Oleg', 'birthday':'12-06-1991'}]

def congratulate(users):
    our_delta = {0:range(5, 12), 1:range(4, 11), 2:range(3, 10), 3:range(2, 9), 4:range(1, 8), 5:range(0, 7), 6:range(-1, 6)}
    current = date.today()
    bdays_this_week = defaultdict(list) 

    for user in users:
        bday_str = user['birthday']
        bday_list = bday_str.split('-')
        
        if current.month > int(bday_list[1]) or int(bday_list[1]) == 1:
            bday_this_year = date(day=int(bday_list[0]), month=int(bday_list[1]), year=current.year+1)
        else:
            bday_this_year = date(day=int(bday_list[0]), month=int(bday_list[1]), year=current.year)   
      
        delta = bday_this_year - current
       
        if delta.days in our_delta[current.weekday()]:
            bday_weekday = bday_this_year.weekday()
            if bday_weekday == 0 or bday_weekday == 5 or bday_weekday == 6:
                bdays_this_week['Monday'].append(user['name'])
            elif bday_weekday == 1:
                bdays_this_week['Tuesday'].append(user['name'])
            elif bday_weekday == 2:
                bdays_this_week['Wednesday'].append(user['name'])
            elif bday_weekday == 3:
                bdays_this_week['Thursday'].append(user['name'])
            elif bday_weekday == 4:
                bdays_this_week['Friday'].append(user['name'])

    for k, v in bdays_this_week.items():
        value = ', '.join(v) 
        print(f'{k} : {value}')    

        
congratulate(users)
