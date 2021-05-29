"""
满足以下两个条件的整数才可以称为闰年：
 1. 普通闰年：能被4整除但不能被100整除（如2004年就是普通闰年
 2. 世纪闰年：能被400整除（如2000年是世纪闰年，1900年不是世纪闰年)
"""

year, month, day, result = 0, 0, 0, 0
days_per_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year(y):
    """
    :param y: int, year
    :return: bool
    """
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400) == 0:
        return True
    else:
        return False


# read input and check compliance(number of inputs must be 3, input type must be int..)
while True:
    try:
        entry = input("Please input the date, separated by space：")
        year, month, day = map(int, entry.split())
    except ValueError as e:
        print("Error: Please check your input: %s" % e)
        continue

    if is_leap_year(year):
        days_per_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if year <= 0 or month <= 0 or day <= 0:
        print("Error: input must > 0, try again")
        continue
    if not (month <= 12 and day <= 31):
        print("Error: Month or Day is not valid")
        continue
    if day > days_per_month[month - 1]:
        print("Error: No such day in the month you input")
        continue
    break

result = day
if month > 1:
    for m in range(1, month):
        result += days_per_month[m-1]

print("The result is: %i" % result)
