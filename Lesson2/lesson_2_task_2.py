def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap(1982))
