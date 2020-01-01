from datetime import date,timedelta
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(year,month,nth=4,weekday=3):
    d = date(year,month,1)
    if nth < 0:
        next_month = d.replace(day=28) + timedelta(days=4)
        d = next_month - timedelta(days=next_month.day)
        day1 = d.weekday()
        if day1 >= weekday:
            return date(year,month,(d.day - (((abs(nth) - 1) * 7) + (day1 - weekday))))
        else:
            return date(year,month,(d.day - (((abs(nth) * 7) + (day1 - weekday)))))
    else:        
        day1 = d.weekday()
        if day1 <= weekday:
            return date(year,month,((weekday - day1) + ((nth - 1) * 7 + 1)))
        else:
            return date(year,month,((weekday - day1) + (nth * 7 + 1)))
