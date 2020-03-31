# Conditionals and If,Else, & elif statements

#If-Else

language = 'Java'
if language == 'Python' :
    print('Language is Python')
else:
    print('Language is Java')

# elif

language = 'Go'
if language == 'Java':
    print("Language is Java")
elif language == 'Go':
    print("Language is Go")
else:
    print("Language Not Found")

# Python doesn't have a switchcase

# Booleans

# and or not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin'  or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

# is comparisons
# here "is" doing comparisons between ids of comparators

a = [1, 2, 3]
b = [1, 2, 3]
if a is b:
    print('Equal')
else:
    print(id(a))
    print(id(b))
    print('Not Equal')

# All FALSE value evaluated in python

# False, None, Zero (0), Any empty sequence example (), [], ''
# any empty mappin example {}

condition = False
if condition:
    print("Evaluated to TRUE")
else:
    print("Evaluated to False")

condition = None
if condition:
    print('True')
else:
    print('False')

condition = 0
if condition:
    print('True')
else:
    print('False')

condition = 10
if condition:
    print('True')
else:
    print('False')


# condition = '' / [] /()
if condition:
    print('True')
else:
    print('False')

condition = {}
if condition:
    print('True')
else:
    print('False')
