# List, Tuples & Sets + Dictionary

#List

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))

# Indexing

print(courses[0])
print(courses[3])

print(courses[-1])
print(courses[0: 2])
print(courses[:2])
print(courses[2:4])
print(courses[2:])

# Append
courses.append('Art')
print(courses)

# To add an element at specific location
courses.insert(1, 'SST')
print(courses)

# To add one list element in another list
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
# courses.insert(0, courses_2)
courses.append(courses_2)
print(courses)

# Using Extend() method
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)


# Remove() / POP()

courses.remove('Math')
print(courses)

popped = courses.pop()
print(popped)

#  Reverse()
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

# Sort()
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)

# Sorted function
nums = [1, 5, 2, 4, 3]
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)

# Using min(), max(), sum()
print(min(nums))
print(max(nums))
print(sum(nums))

# to find the index of an element from the list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('Math'))

# For checking the item in list
print('Art' in courses)
print('History' in courses)

# For Loop
for item in courses:
    print(item)

# To access the index as well with values, for this we use enumerate function()

for index, course in enumerate(courses):
    print(index, course)

# if we want to print the index acc. to u
print("#############")
for index, item in enumerate(courses, start=1):
    print(index, item)

# List into Strings with ', ' separated

courses_str = ', '.join(courses)
print(courses_str)
course_str1 = ' - '.join(courses)
print(course_str1)

# Now, String to List

new_list = courses_str.split(', ')
print(new_list)

print("#####################TUPLES#####################")
# Example of list

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Example of tuple

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)


# tuple_1[0] = 'Art'
# print(tuple_1)
# It shows error that object does not support item assignment

print('###############SETS###############')

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

# How sets remove duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

# to check
print('Math' in cs_courses)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# How to Create Empty List,Tuples & Sets

#empty Lists
empty_list = []
empty_list1 = list()

#empty tuples
empty_tuple = ()
empty_tuple1 = tuple()

#empty sets
empty_set = set()


print('##############Dictionary#################')

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print(student['name'])
print(student['courses'])

student = {1: 'John', 'age': 25}
print(student)
print(student[1])
print(student['age'])

#print(student['phone'])
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('name'))

#with default value in place of error

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('phone', 'Not Found'))

# To Add in the dictionary
student['phone'] = '555-555'
print(student.get('phone', 'Not Found'))

# To update the value of key
student['name'] = 'Jane'
print(student)

# To update the multiple keys in
student.update({'name': 'Jojo', 'age': 26, 'phone': '666-666'})
print(student)

#To delete a specific key
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
del student['age']
print(student)

# or using pop
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student.pop('age')
print(age)

print(len(student))

print(student.keys())
print(student.values())

# If we want to see both keys and values

print(student.items())

#Looping
for key in student:
    print(key)

# if we want to print keys and value together

for key, value in student.items():
    print(key, value)
