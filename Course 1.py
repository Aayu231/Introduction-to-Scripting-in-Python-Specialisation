"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """" no of days in month """
    if(month in (1, 3, 5, 7, 8, 10, 12)):
        return 31
    elif(month in (4, 6, 9, 11)):
        return 30
    else:
        if(year%100 == 0):
            if(year%400 == 0):
                return 29
            else:
                return 28
        elif(year%4 == 0):
            return 29
        else:
            return 28

def is_valid_date(year, month, day):
    """ is it a valid date """
    if(year >= datetime.MINYEAR and year <= datetime.MAXYEAR):
        if(month > 0 and month < 13):
            maxi = days_in_month(year, month)
            if(day > 0 and day <= maxi):
                return True
            else:
                return False
        else:
            return False
    else:
        return False  

def days_between(year1, month1, day1, year2, month2, day2):
    """ how many days are between """
    if(is_valid_date(year1, month1, day1)):
        if(is_valid_date(year2, month2, day2)):
            d_0 = datetime.date(year1, month1, day1)
            d_1 = datetime.date(year2, month2, day2)
            delta = d_1 - d_0
            if(delta.days > 0):
                return delta.days
            else:
                return 0
    else:
        return 0
    
def age_in_days(year, month, day):
    """ what is your age now """
    d_12 = str(datetime.date.today())
    y_1 = d_12[0:4]
    y_1 = int(y_1)
    m_1 = d_12[5:7]
    m_1 = int(m_1)
    d_1 = d_12[8:10]
    d_1 = int(d_1)
    return days_between(year, month, day, y_1, m_1, d_1)
