# importing modules

import my_modules
import sys
import random, math, datetime, calendar, os
courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_modules.find_index(courses, 'Math')
print(index)


# there are many ways to call/import a module
    # import my_modules as mm
    # from my_modules import find_index
    # from my_modules import find_index, test
    # from my_modules import find_index as fi, test
    # from my_modules import  *

# How to find that where to find this module path
    # we've to import sys module

print(sys.path)

# Now to import predefined modules
random_courses = random.choice(courses)
random_courses1 = random.choices(courses)
print(random_courses)
print(random_courses1)

# math module

rad = math.radians(90)
print(rad)
print(math.sin(rad))

# date and time & calendar module
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# Now importing OS

print(os.getcwd())

print(os.__file__) # here __file__ is set to its path
