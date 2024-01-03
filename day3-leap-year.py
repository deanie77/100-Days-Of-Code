# is a year a leap year?
# normal year = 365, leap year = 366 with an extra day in february
# a leap year is divisible by 4, skip centuries, unless divisible by 400

year = int(input('Which year do you want to check? '))

if (year % 4 == 0):
    print('checking')
    if (year % 100 == 0):
        if (year % 400 == 0):
            print('It\'s a leap year')
        else:
            print('It\'s not a leap year')
    else:
        print('leap year')
else:
    print('Not a leap year')