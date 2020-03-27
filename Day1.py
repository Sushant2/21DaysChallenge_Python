print('Hello World')

#with variable
my_message = 'Bobby World'
print(my_message)

my_message = 'Bobby\'s world'
print(my_message)

# to print multiple lines

message = """Bobby's world was a
good cartoon in the 1990s"""
print(message)

#length of the string
message = 'Hello World'
print(len(message))

#accessing strings characters by indexing
message = "Hello World"
print(message[10])

#string Slicing
message = "Hello World"
print(message[0:5])
print(message[6:11])
print(message[:5])
print(message[6:])

#methods
message = "Hello World"
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))

#replace
new_message = message.replace('World', 'Universe')
print(new_message)

#add multiple strings
greeting = 'Hello'
name = 'Sushant'
message = greeting + name
print(message)
message = greeting + ' ' + name
print(message)

#Another Example
greeting = 'Hello'
name = 'Sushant'
message = greeting + ", " + name + ". Welcome!"
print(message)

#or

greeting = 'Hello'
name = 'Sushant'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#using fstrings

greeting = 'Hello'
name = 'Sushant'
message = f'{greeting},{name}. Welcome!'
print(message)

#dir() function
print(dir(name))

#help() function
print(help(str))
