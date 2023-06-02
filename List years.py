from datetime import date


def list_years(dates: list):
    year_list = []
    for item in dates:
        year_list.append(item.year)
    year_list.sort()
    return year_list


date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)
