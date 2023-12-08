# Printing Text
print('Hello World!')

# Printing on new line
print('Hello world\nHello world\nHello world')

# Concatenating strings
print('Hello ' + 'Dean')

# Prompt user to enter data
input('What is your name?')

# The inner function is run first
print('Hallo ' + input('What is your name? '))

# Calculate length of string
print(len(input('What is your name? ')))

# Using tuple unpacking to swap variables
a = 10
b = 20

a, b = b, a

print(a,'\n',b)