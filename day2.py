# Data types

# String

# Integer
# writing long numbers, _ replaces the commas
123_456_789

num_char = len(input('What is your name?'))

# returns <class 'int'>, use to investigate data types you are working with 
print(type(num_char))

# converts to string
str(num_char)

# converts to float
print(70 + float('100.58'))

# convert to int
print(70 + int(100.58))

# mathematical calculations
6 + 3
6 - 3
6 * 3

# returns a float
6 / 3

# returns int
6 // 3

6 ** 3

# PEDMASLR
print(3 * ((3 + 3) / 3) - 3)

# rounding numbers
print(round(8 / 3))

# round to number of decimals
print(round(8 / 3, 3))

# using f-strings
score = 0
height = 1.8
isWinning = True

print(f'your score is {score}, your height is {height}, you are winning is {isWinning}')
