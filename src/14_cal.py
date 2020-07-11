"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
from datetime import date


'''theValues = [x for x in input(
    'Enter two comma seperated integers for the calendar, the month (1-12) followed by the year: ').split(',')]'''

if(len(sys.argv) == 1):
    # no values given, give current date and time
    defaultDate = date.today()
    dateToString = defaultDate.strftime("%m-%d-%Y")
    mydatelist = [int(x) for x in dateToString.split('-')]
    theMonth = mydatelist[0]
    theYear = mydatelist[2]
    c = calendar.TextCalendar(calendar.SUNDAY)
    finalS = c.formatmonth(theYear, theMonth)
    print(finalS)
    sys.exit(0)
elif(len(sys.argv) < 3):  # assume the value we got was for the month
    numVals = [x for x in sys.argv]
    numValtoInt = int(numVals[1])
    if(numValtoInt < 1 or numValtoInt > 12):
        print("we need values of 1-12 for the month and valid 4 digit year")
        sys.exit(0)
    else:
        defaultDate = date.today()
        dateToString = defaultDate.strftime("%m-%d-%Y")
        mydatelist = [int(x) for x in dateToString.split('-')]
        theYear = mydatelist[2]
        c = calendar.TextCalendar(calendar.SUNDAY)
        finalS = c.formatmonth(theYear, numValtoInt)
        print(finalS)
else:
    numVals = [x for x in sys.argv]
    monthToInt = int(numVals[1])
    yearToInt = int(numVals[2])
    if(monthToInt < 1 or monthToInt > 12):
        print('we need values of 1-12 for the month and a valid 12 month year')
        sys.exit(0)
    else:
        c = calendar.TextCalendar(calendar.SUNDAY)
        finalS = c.formatmonth(yearToInt, monthToInt)
        print(finalS)
