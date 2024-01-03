print('welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('How old are you? '))
    
    price = 0
    
    if age < 12:
        price += 5
    elif age >= 12 and age <= 18:
        price += 7
    elif age >= 45 and age <=55:
        print('you can ride for free')
    else:
        price += 12
        
    add_photos = input('Would you like to take pictures? (Y/N): ')
    if add_photos == 'Y':
        price += 3
        
    print(f'Your total fee is ${price}')
else:
    print('sorry you have to grow taller before you can ride.')