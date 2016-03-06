import time
from datetime import date

today = date.today()

my_name = "Tony"
my_age = 29
my_dob = "29/12/1986"
my_height = "6'2\""
dob_array = map(int, my_dob.split("/"))
dob_date = date(dob_array[2], dob_array[1], dob_array[0])


def years_ago(years, from_date=None):
    if from_date is None:
        from_date = today
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=2, day=28, year=from_date.year-years)

def noy_since_dob(dob, end=None):
    # calculate number of years since date of birth

    if end is None:
        end = today
    noy_since_dob = int((end - dob).days / 365.25)
    if dob > years_ago(noy_since_dob, end):
        return noy_since_dob - 1
    else:
        return noy_since_dob

def nod_since_last_bd(dob):
    # calculate number of days since last birthday




    pass

def t_funk(name, age, height):
    output_str = (
        "Hi %s, so you're %d years old and will be %d years old when you are twice that!\n"
        "Today is %s and the time is %s"
    ) % (name,
         age,
         age * 2,
         date.strftime(today, "%A the %d of %B"),
         date.strftime(today, "%I:%M %p")
         )
    return output_str

print t_funk(my_name, noy_since_dob(dob_date), my_height)