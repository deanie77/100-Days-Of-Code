print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision = input('Which direction are you going? (left/right): ')

if decision.lower() == 'left':
    decision = input('You are now at a river.\nAre you going to swim or wait for a boat? (swim/wait): ')
    if decision.lower() == 'wait':
        print('A boat has come to pick you up and taken you to an island. There is a deserted little house with three doors.')
        decision = input('Which door will you choose to open? (red/blue/yellow): ')
        if decision.lower() == 'yellow':
            print('You Win!')
        elif decision.lower() == 'red':
            print('Burned by fire.\nGame over.')
        elif decision.lower() == 'blue':
            print('Eaten by beasts.\nGame over')
        else:
            print('Game Over')
    else:
        print('Game over! Attacked by trout!')
else:
    print('Fall into a hole. Game over!')