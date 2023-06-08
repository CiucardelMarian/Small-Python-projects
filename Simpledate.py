class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __getdays(self):
        days = self.day + self.month * 30 + self.year * 360
        return days

    def __getdate(self, numberofdays: int):
        year = int(numberofdays / 360)
        month = int((numberofdays - year * 360) / 30)
        day = int((numberofdays - year * 360 - month * 30))
        return day, month, year

    def __eq__(self, another):
        return self.__getdays() == another.__getdays()

    def __ne__(self, another):
        return self.__getdays() != another.__getdays()

    def __gt__(self, another):
        return self.__getdays() > another.__getdays()

    def __lt__(self, another):
        return self.__getdays() < another.__getdays()

    def __add__(date, days: int):
        new_date = SimpleDate(date.day, date.month, date.year)
        convertdays = new_date.__getdays()
        convertdays += days
        date = new_date.__getdate(convertdays)
        return SimpleDate(date[0], date[1], date[2])

    def __sub__(date1, date2):
        date1 = SimpleDate(date1.day, date1.month, date1.year)
        date2 = SimpleDate(date2.day, date2.month, date2.year)
        days1 = date1.__getdays()
        days2 = date2.__getdays()
        return abs(days1 - days2)


d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2 - d1)
print(d1 - d2)
print(d1 - d3)
