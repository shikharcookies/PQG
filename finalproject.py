import datetime

def days_in_month(year, month):
    if month < 12:
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    else:
        return (datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)).days

def is_valid_date(year, month, day):
    if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= days_in_month(year, month):
                return True

    return False

def days_between(year1, month1, day1, year2, month2, day2):
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0

    days = (datetime.date(year1, month1, day1) - datetime.date(year2, month2, day2)).days


    if days < 0:
        return -days

    return 0

def age_in_days(year, month, day):
    if not is_valid_date(year, month, day):
        return 0
       
    age_days = (datetime.date.today() - datetime.date(year, month, day)).days

    if age_days > 0:
        return age_days

    return 0

year_input = int(input (" Please write the year you want to calculate "))
month_input = int(input (" Please give the number of the month "))
print("Total Days in Month is :", days_in_month(year_input, month_input))

# Add the year, month, day for parts 1
year_input1 = int(input (" Please write the year you want to check "))
month_input1 = int(input (" Please give the number of the month for finalise checking "))
day_input1 = int(input (" Please give the date for Checking "))
print("Given date is :", is_valid_date(year_input1, month_input1, day_input1))

# Add the year, month, day for parts 2
year_input2 = int(input (" Please write the year from where you want to calculate "))
month_input2 = int(input (" Please write the month from where you want to calculate " ))
day_input2 = int(input (" Please write the date from where you want to calculate "))

# Add the year, month, day for parts 3
year_input3 = int(input (" Please write the end year where you want to calculate "))
month_input3 = int(input (" Please write the end of the month where you want to calculate "))
day_input3 = int(input (" Please write the end date where you want to calculate "))
print("Distance Between The Given Dates :", days_between(year_input2, month_input2,
day_input2, year_input3, month_input3, day_input3))

# Add the year, month, day for parts 4
year_input4 = int(input (" Please write the year of birth "))
month_input4 = int(input (" Please write the month of birth "))
day_input4 = int(input (" Please write the date of birth "))
print("Persons age in days :", age_in_days(year_input4, month_input4, day_input4))