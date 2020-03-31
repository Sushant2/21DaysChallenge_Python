# Functions

def hello_func():
    pass

print(hello_func)

print(hello_func())

def hello_func():
    print('Hello Function 1')

hello_func()

# DRY - Don't Repeat Yourself

# return

def hello_func():
    return 'Hello Function 2'

print(hello_func())

# return is like a datatype, what is return all goes to the function

def hello_func():
    return 'Hello Function'
print(hello_func().upper())

# Using argument

def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func("Hello"))

# With default Value

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi'));

# Positional and Keywords arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
# They allow us to accept an arbitrary no. of positional or keyword arguments

student_info('Math', 'Art', name = 'John', age = 22)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22 }

student_info(courses, info)
student_info(*courses, **info)

#########################
print('Practice')

# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, false for non leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return no of days in that month in that year"""
    if not 1 <=month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(is_leap(2017))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2021, 6))
print(days_in_month(2022, 5))