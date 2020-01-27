from datetime import date
from calendar import monthrange

class Month:

    __slots__ = ['year', 'month']

    def __init__(self,year,month):
        super().__setattr__('year', year)
        super().__setattr__('month', month)

    def __setattr__(self, name, value):
        raise NotImplementedError

    def __delattr__(self, name):
        raise NotImplementedError

    def __str__(self):
        return f"{self.year}-{self.month:02}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self,other):
        if not isinstance(other,Month):
            return NotImplemented
        if self.year == other.year and self.month == other.month:
            return True
        else:
            return False

    def __gt__(self,other):
        if not isinstance(other,Month):
            return NotImplemented
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        elif self.month > other.month:
            return True
        elif self.month < other.month:
            return False
        else:
            return False

    def __ge__(self,other):
        if not isinstance(other,Month):
            return NotImplemented
        if self.year >= other.year:
            return True
        elif self.year < other.year:
            return False

    def __hash__(self):
        return hash((self.year, self.month))

    @property
    def first_day(self):
        return date(self.year,self.month,1)

    @property
    def last_day(self):
        return date(self.year,self.month,monthrange(self.year,self.month)[1])
    
    @staticmethod
    def from_date(dt):
        return Month(dt.year, dt.month)

    def strftime(self, fmt):
        return self.first_day.strftime(fmt)
