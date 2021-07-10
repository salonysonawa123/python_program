# Figure out your age

import datetime
currentDate = datetime.datetime.now()
#print(currentDate)

#Birth  Kb_Se
deadline= input ('Plz enter your date of birth (dd/mm/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%d/%m/%Y')

#End    Kb_tk
#current= input ('Plz enter your date of birth (dd/mm/yyyy) ')
#currentDate= datetime.datetime.strptime(current,'%d/%m/%Y')

daysLeft = currentDate - deadlineDate

years = ((daysLeft.total_seconds())/(365.242*24*3600))  #daysLeft.total_seconds() CHANGE daysLeft's YY MM DD HH MIN into Seconds and put Remaider seconds atfer its Converting Second.

yearsInt=int(years)

months=(years-yearsInt)*12

monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)

daysInt=int(days)

print('You are {0:d} years, {1:d}  months, {2:d}  days'.format(yearsInt,monthsInt,daysInt))
